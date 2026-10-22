# Saltmarsh Signal

A radio-repair puzzle game from Tern Lantern Studio. You fix old shortwave sets
for the people of a drowned delta town and listen to what they tell you.
Built in Godot 4. Steam release next week, itch.io the same day.

## Layout

- `data/npcs.json`: the cast
- `data/quests.json`: quest steps, flags and rewards
- `data/dialogue/`: hand-edited dialogue
- `assets/ASSET_REGISTER.md`: every AI-touched asset, with status
- `store/`: Steam page text, content survey answers, itch.io page

## How the game was made

- Code: written by the team, with an AI coding assistant for boilerplate and
  refactors. None of its output is shown or heard by players.
- Maps: the marsh channels are generated procedurally from a seeded noise
  function, around hand-built town blocks.
- Art: hand-drawn by Ines Okonkwo-Bell. Three background plates began as
  image-model drafts and were painted over; they are disclosed in the register.
- Voice: one AI-voiced radio announcer, disclosed on the store pages. All
  other characters are text only.
- Dialogue: first drafts of some ambient lines came from a language model.
  Every line was rewritten by Tomasz Wierzbicki into the game's voice.

## Status

- [x] All 9 quests played start to finish
- [x] Asset register checked against the build on 14 Oct
- [x] Steam survey and itch.io disclosure match the register
