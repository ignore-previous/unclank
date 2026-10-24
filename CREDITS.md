# Credits

unclank was researched and built with Claude.

## Research sources

Every tell in `research/` lists its sources: studies, platform policy pages, developer and player discussions, press and practitioner posts. They belong to their authors. unclank links to them and paraphrases; quotes are kept under 15 words. The full list is in `research/sources.md`.

## Prior art

These open-source skills covered the ground first, and unclank was planned after reading them. Where an idea below shaped unclank, it was rewritten in our own words; no text was copied. All are MIT-licensed unless noted.

| Project | What it does well | Idea unclank adapted |
|---|---|---|
| [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | Prose tells with separate detect and rewrite modes, plus evals | Keeping audit (report only) apart from fixing |
| [avoid-ai-design](https://github.com/funboy322/avoid-ai-design) | Design tells, each with a detection signal, rationale, fix and sources | Giving each tell a concrete detection step and a fix |
| [hallmark](https://github.com/Nutlope/hallmark) | UI generation with explicit quality gates | (to be reviewed for `unclank-ui`) |
| [stop-slop](https://github.com/hardikpandya/stop-slop) | Prose checklist with a scoring rubric | (to be reviewed for `unclank-prose`) |
| [unslop in pstack](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop) | Numbered prose rules | (to be reviewed for `unclank-prose`) |
| [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Names the default looks generated UIs fall into | (to be reviewed for `unclank-ui`) |

Rows marked "to be reviewed" will be read in full before the matching skill is written, and this table will say what was kept and what was left out.

## Test fixtures

The planted launch case (`evals/launch-audit-planted/`) copies Vite's default favicon, `vite.svg`, on purpose: the test checks that the starter icon gets noticed. It comes from the Vite project's starter templates, which are MIT-licensed. Vite and its logo belong to their owners.

## Licences used here

- CC BY 4.0 legal text from Creative Commons (`LICENSE-CC-BY-4.0.txt`).
- MIT License text (`LICENSE-MIT`).
