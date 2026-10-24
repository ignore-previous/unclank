# Changelog

Dates are when a change was made. Skills also show their own "Last reviewed" date.

## 0.1.0 (24 Oct 2026)

First release.

### Added
- `unclank-launch`, `unclank-quiz` and `unclank-store` skills (drafts), each with a generated `references/evidence.md`.
- `.claude-plugin/marketplace.json`, so Claude Code can install the plugin straight from this repo.
- `evals/`: planted, clean and unrelated test cases for each skill, plus a build case for `unclank-launch`.
- Links for the sources in `research/sources.md` wherever the research recorded one.
- `research/`: ten research domains, the master patterns and the source list (research run of 19 to 21 Oct 2026).
- `scripts/check.py` static checks and their tests, and `scripts/build_evidence.py`.
- Licences: CC BY 4.0 for content, MIT for code.

### Changed
- All three skills: a hit needs evidence in the files; what can't be seen goes under "Check this" and stays out of the audit block. Audit block labels are exactly `Avoid` or `Choose deliberately`.
- Narrower checks after an adversarial review, such as the longest-key rule (about a quarter longer), the answer-position rule (sets of 12 or more), name clusters in game writing, and dated platform rules that say which points come from press.
