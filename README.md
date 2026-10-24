# Unclank

Agents keep getting more capable. What still makes work good is a person testing it against what users need. Clanky work skipped that step: it looks fine until someone tries to use it. Unclank puts that step in your agent's hands.

Runs: [inside Claude Code or Codex](#install) · Sends: [only what that app already sends](SECURITY.md#what-counts) · Won't: [add tracking](skills/), or [change files until you ask](#how-the-skills-work)

## What clanky work looks like

Agents can build a site, a quiz or a store page in an afternoon. The result often looks finished, then trips up the first real person who uses it. The browser tab still shows the default icon. You can guess the quiz answers without reading the questions. The store page misses a rule that gets it taken down.

Using AI isn't the problem. Shipping its defaults is. Unclank gives your agent checklists for these gaps, so the work fits the people who'll use it.

## What's different

There are plenty of anti-slop skills already (skills that steer an agent away from careless AI output). Unclank is built to be right:

- **Every item has evidence.** Each tell (one sign of clanky work) has an ID, a confidence rating and the date it was seen. Each tell links to its sources, so you can check the reasoning.
- **Not every default is a problem.** Each skill lists things that look like defaults but are good practice: clean grammar, equal-length quiz options, a framework's normal behaviour, saying you used AI. The skills are told to leave them alone.
- **Clusters count.** One em dash on its own means little. The skills report how many tells turn up together, because that's what readers react to.
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

Agents load a skill when your request matches its description. Smaller models sometimes skip that step on a large project, so if you're using one, name the skill: "use unclank-launch to check this before I ship it".

## Install

The skills are ordinary `SKILL.md` folders, so any agent that reads skills can use them.

- **Claude Code:** add this repo as a plugin marketplace, then install the plugin:

  ```
  /plugin marketplace add ignore-previous/unclank
  /plugin install unclank@unclank
  ```

  To try a local clone instead, start Claude Code with `claude --plugin-dir path/to/unclank`.
- **Other agents (Codex, Cursor and others):** copy the folders in `skills/` into the folder your agent loads skills from. Each skill works on its own; the links from `references/evidence.md` into `research/` only work in a full clone.

## The research

`research/` holds the full record behind the skills: ten domains, about 130 tells, 60 Not-a-tells and 570 source records, gathered in October 2026. Start with `research/README.md`. Each skill's `references/evidence.md` is generated from it, so the skills and the research can't drift apart.

## Checks

`scripts/check.py` confirms that tell IDs exist, labels and confidence match the research, evidence files are current, skills stay within their size budget, quotes stay short, and no private paths or addresses slip in. `python -m unittest discover -s scripts` tests it. Model-based example tests live in `evals/`.

## Keeping it current

Tells fade and platform rules change. Each skill shows a "Last reviewed" date, each tell keeps the date it was seen, and the research gets a light re-check every three months. Changes are listed in `CHANGELOG.md`.

## Licence and credits

Unclank uses two licences:

- Written content is under CC BY 4.0 (`LICENSE`). This covers the skills (`skills/`), the research (`research/`), the eval cases and fixtures (`evals/`) and the other documentation. To credit it, name "Unclank", link the repository, and say if you changed it.
- Code is under the MIT License (text in `scripts/LICENSE`). This covers the scripts in `scripts/` and any other code.

Third-party sources cited in `research/` belong to their authors. Unclank links to them and paraphrases them; it doesn't relicense them. Ideas taken from other projects are credited in `CREDITS.md`.

To report a security problem, see `SECURITY.md`.

Built with Claude.
