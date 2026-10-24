# Security

## Reporting a problem

Email security@ignoreprevious.dev. Please don't open a public issue for a security problem.

Say what you found, which file or skill it is in, and how to reproduce it. You'll get a reply when the report has been read. The fix is listed in `CHANGELOG.md`, without your name unless you ask for it.

## What counts

unclank is a set of skills (instructions your coding agent reads) and a few Python scripts for checks and evals. Report it if:

- a skill tells the agent to run a command, change files outside the project it is auditing, or send anything off your machine;
- a skill could make the agent read out or copy a secret, such as a key or token in the project it audits;
- text in a skill, a research file or an eval fixture tries to give the agent instructions it shouldn't follow;
- a script in `scripts/` or an eval `scaffold.sh` can be made to run code, or writes outside the repository or the eval workspace.

## What doesn't

A check that misses something, or flags something that's fine, is a quality problem. Open a normal issue for it.
