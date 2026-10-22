# unclank

Agent skills that take the clank out of your work.

"Clanker" is what people now call a robot that's trying too hard to pass. Clanky work is the same thing in a project: the starter favicon nobody changed, the quiz where the right answer is always the longest, the fantasy cast all called Elara, the AI placeholder art that shipped and got found by players on day one. None of it proves AI was used. All of it tells the reader that nobody checked.

unclank gives your coding agent checklists for those tells, so it can catch them before your users do, and avoid them while it builds.

## What's different

There are plenty of anti-slop skills already. unclank is built for being right rather than strict:

- **Every check has evidence.** Each tell has an ID, sources, the date it was seen and a confidence rating. The skill can show its reasoning when you push back.
- **"Not a tell" lists.** Things that get blamed on AI but are just good practice: clean grammar, equal-length quiz options, a framework's normal behaviour, disclosing AI use. The skills are told not to "fix" them.
- **Clusters, not single hits.** One em dash proves nothing. The skills report how many tells turn up together, because that's what readers react to.
- **It doesn't accuse anyone.** The checks are for your own work. Human work gets flagged as AI all the time.
- **Platform rules come dated.** Steam, itch.io, Kickstarter, Apple and Google rules change. The skills give the date each rule was checked and send you to the live page before you submit.

## Skills

| Skill | Checks | Status |
|---|---|---|
| `unclank-launch` | Visible defaults before launch: favicon, page title, link preview, 404 page, builder badges, placeholder text, README | Draft |
| `unclank-quiz` | Quiz and flashcard items: longest-option keys, answer-position skew, cues, wrong or doubled keys, weak distractors, feedback | Draft |
| `unclank-store` | Games and creative work going onto a store: AI asset register, Steam, itch.io, Kickstarter, Apple, Google Play and art-site AI rules, store page and trailer, names and voices | Draft |
| `unclank-pixels` | Pixel art and sprite sets | Planned |
| `unclank-images` | Reviewing AI images and illustrations | Planned |
| `unclank-ui` | Web design looks | Planned |
| `unclank-prose` | General writing | Planned |
| `unclank` | The umbrella: picks the skills that apply, plus the cross-domain patterns and marketing copy, naming and tagline tells | Planned |

## How the skills work

Each skill has two modes:

- **Audit mode.** Ask your agent to check, review or audit something. It reports the hits first, worst first, with the file and line, and changes nothing until you ask. The report ends with a fixed block that tests can read:

  ```
  UNCLANK-AUDIT
  D08-002 | Avoid | index.html:7 | title is "Vite + React"
  END-UNCLANK-AUDIT
  ```

- **Build mode.** While your agent is making something, it applies the checklist as it goes and mentions briefly what it set.

Each checklist line has a label and a confidence:

- **Avoid**: fix it. **Choose deliberately**: fine if chosen, a signal when it's an unchosen default.
- **Strong**: 3+ independent sources. **Moderate**: 2. **Anecdotal**: one opinion, so treat it as a hint.

## Install

The skills are plain `SKILL.md` folders, so any agent that reads skills can use them.

- **Claude Code:** load the plugin from a local clone with `claude --plugin-dir path/to/unclank`. A marketplace install will follow the first release.
- **Other agents (Codex, Cursor and others):** copy the folders in `skills/` into the folder your agent loads skills from. Each skill works on its own; the links from `references/evidence.md` into `research/` only work in a full clone.

Agents load a skill when your request matches its description. Smaller models sometimes skip that step on a large project, so if you're using one, name the skill: "use unclank-launch to check this before I ship it".

## The research

`research/` holds the full record behind the skills: ten domains, about 130 tells, 60 Not-a-tells and 570 source records, gathered in October 2026. Start with `research/README.md`. Each skill's `references/evidence.md` is generated from it, so the skills and the research can't drift apart.

## Checks

`scripts/check.py` runs the static checks: tell IDs exist, labels and confidence match the research, evidence files are current, skills stay within their size budget, quotes stay short, and no private paths or addresses slip in. `python -m unittest discover -s scripts` tests the checker. Model-based example tests live in `evals/`.

## Keeping it current

Tells fade and platform rules change. Each skill shows a "Last reviewed" date, each tell keeps the date it was seen, and the research gets a light re-check every three months. Changes are listed in `CHANGELOG.md`.

## Licence and credits

Written content is CC BY 4.0 and code is MIT; see `LICENSE`. Ideas taken from other projects are credited in `CREDITS.md`.

Researched and built with Claude.
