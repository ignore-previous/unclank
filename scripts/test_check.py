"""Tests for check.py: plant faults in a temporary copy of the repo and expect errors.

Usage: python -m unittest discover -s scripts
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = [".claude-plugin", "research", "scripts", "skills", "evals"]
# The planted private term and email are built up from parts so that this file,
# which is itself checked, doesn't contain them.
PLANTED = "Planted" + "name"


class CheckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        for name in COPY:
            shutil.copytree(ROOT / name, self.tmp / name,
                            ignore=shutil.ignore_patterns("__pycache__", "results"))
        (self.tmp / ".private-terms").write_text(PLANTED + "\n", encoding="utf-8")

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def run_check(self) -> tuple[int, str]:
        p = subprocess.run([sys.executable, str(self.tmp / "scripts" / "check.py")],
                           capture_output=True, text=True, encoding="utf-8")
        return p.returncode, p.stdout

    def edit(self, rel: str, old: str, new: str) -> None:
        path = self.tmp / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture text missing from {rel}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")

    def append(self, rel: str, line: str) -> None:
        with (self.tmp / rel).open("a", encoding="utf-8", newline="\n") as f:
            f.write(line + "\n")

    def test_clean_repo_passes(self) -> None:
        code, out = self.run_check()
        self.assertEqual(code, 0, out)

    def test_wrong_confidence(self) -> None:
        self.edit("skills/unclank-launch/SKILL.md",
                  "[Avoid · strong] **Starter favicon**", "[Avoid · moderate] **Starter favicon**")
        code, out = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("D08-001 is tagged Avoid · moderate", out)

    def test_excluded_tell(self) -> None:
        self.append("skills/unclank-quiz/SKILL.md", "- [Avoid · anecdotal] **x** [D09-015].")
        _, out = self.run_check()
        self.assertIn("cites D09-015, which is kept out of checklists", out)
        self.assertIn("unclank-quiz/references/evidence.md: out of date", out)

    def test_unknown_tell(self) -> None:
        self.append("skills/unclank-quiz/SKILL.md", "See [D09-999].")
        _, out = self.run_check()
        self.assertIn("cites unknown tell D09-999", out)

    def test_missing_last_reviewed(self) -> None:
        self.edit("skills/unclank-launch/SKILL.md", "Last reviewed:", "Reviewed:")
        _, out = self.run_check()
        self.assertIn("no 'Last reviewed", out)

    def test_private_text(self) -> None:
        long_quote = '"' + " ".join(["word"] * 15) + '"'
        email = "someone" + "@" + "gmail.com"
        self.append("skills/unclank-store/SKILL.md",
                    f"By {PLANTED}, C:\\Users\\someone, {email}. {long_quote}")
        _, out = self.run_check()
        for want in ("private term", "local file path", "email address", "quote of 15 words"):
            self.assertIn(want, out)

    def test_stale_scaffold(self) -> None:
        self.edit("evals/launch-audit-planted/fixture/index.html", "Vite + React + TS", "Tidepool")
        _, out = self.run_check()
        self.assertIn("launch-audit-planted/scaffold.sh: out of date", out)

    def test_scaffold_order_is_case_sensitive(self) -> None:
        # Same order on every OS: uppercase names sort before lowercase ones. This fails only on
        # Windows if the bug returns; on Linux, test_clean_repo_passes covers it.
        case = self.tmp / "evals" / "order-case"
        (case / "fixture").mkdir(parents=True)
        for name in ("app.js", "README.md"):
            (case / "fixture" / name).write_text("x\n", encoding="utf-8", newline="\n")
        scripts = str(ROOT / "scripts")
        if scripts not in sys.path:
            sys.path.insert(0, scripts)
            self.addCleanup(sys.path.remove, scripts)
        import build_scaffold
        text = build_scaffold.render(case)
        self.assertLess(text.index("'README.md'"), text.index("'app.js'"))

    def test_bad_frontmatter_name(self) -> None:
        self.edit("skills/unclank-launch/SKILL.md", "name: unclank-launch", "name: launch")
        _, out = self.run_check()
        self.assertIn("frontmatter name 'launch'", out)


if __name__ == "__main__":
    unittest.main()
