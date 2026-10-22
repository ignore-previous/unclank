---
name: unclank-store
description: Pre-release check for a game or creative project going onto Steam, itch.io, Kickstarter, the Apple App Store, Google Play or an art site. It covers the game's own content (default fantasy names, flat or forgetful AI dialogue, quests that don't work, unreviewed AI placeholders, mismatched art and voices), the store page, capsule, trailer and screenshots, and the AI-disclosure rules on those platforms and on Lospec, DeviantArt, ArtStation and art communities, plus covers and ads. Use it when someone is about to submit, publish, crowdfund or announce a game or creative project, wants it checked before a store release, asks about AI-disclosure rules, or asks why players might call their game AI slop. It also covers making these choices during a build.
---

# unclank-store

Checks what a player or backer meets before they play: the store page, the trailer, the disclosure answers, and the game's names, text and voices. Using AI is not the problem. Most players are neutral about generative AI in games, and the platforms allow disclosed use, though some players still react [D10-N03] [D10-N06]. The backlash goes to AI that was unchecked or undisclosed: a placeholder that shipped, art that doesn't match the disclosure, or a note added only after players found the AI [D10-012] [D10-019]. This skill finds those gaps. It doesn't lecture about whether to use AI, and it doesn't give legal advice.

Every check here comes from evidence-backed research. Each one has a tell ID (e.g. [D10-012]). The reasoning, dates and sources are in `references/evidence.md`. Read an entry there before telling someone that a hit matters, when they push back, or when you need the fix details.

## Modes

- **Audit mode** (the default when asked to "check", "review" or "audit"). Report the hits first and change nothing until the user asks for fixes. Follow "How to audit" below.
- **Build mode** (when making or finishing a game or page). Apply the checklist as you go. Start the asset register on day one and log each AI-touched asset as it enters. Mention briefly what you set. Don't produce an audit report or the UNCLANK-AUDIT block. List anything you couldn't finish (a file you can't create or delete, a fact to verify) as next steps for the user.

## Not a tell: don't flag or "fix" these

- Disclosing AI use. A disclosure is honesty, not a quality signal. Don't call clean art proof of AI either [D06-N04] [D10-N03].
- AI development and efficiency tools on Steam. The survey is about content players see or hear. This is a soft exclusion, not a formal one [D10-N01].
- Procedural generation, pathfinding and dynamic music. itch.io exempts them, and procedural content with a hand-made core is respected design [D10-N02] [D06-N01].
- Behind-the-scenes AI such as programming help or difficulty tuning. Objection follows what players see or hear [D10-N07].
- Real app UI inside listing marketing. Only images showing something the app can't do are the problem [D10-N04].
- Google Play apps that only summarise non-AI content, or use AI to enhance an existing feature [D10-N05].
- Simple mechanics, small scope, or a popular genre formula [D06-N02] [D06-N07].
- One cohesive art pack, as long as it is finished or modified [D06-N03].
- One uncommon fantasy-sounding name. The tell is a cluster across the cast [D06-N06].
- Em dashes in fiction, alone [D06-N05].
- AI-drafted lore or item text that a person edited into one voice [D06-N08].
- One disclosed AI voice with a stated reason. Press criticised this, so it is a deliberate choice, not a pass [D06-N09].

## Checklist

Labels: **Avoid** means fix it before launch. **Choose deliberately** means it's fine if it was chosen, and a signal when it's an unchosen default. Confidence: **strong** means 3+ independent sources, **moderate** means 2 (for a platform rule, one fetched policy page), **anecdotal** means one opinion, so treat it as a hint.

Platform rules change. The rule lines below were checked on 20 Oct 2026, except where a line says a point is from press or a page wasn't opened. That is the research date, not today. Before the user submits, open the platform's live policy page and re-check, and never present a rule here as current. Say what the rule asks and point to the page. Don't advise on legal effect.

### Asset register (do this first)
- [Avoid · strong] **No AI asset register, or a build that wasn't checked against it** [D10-012]. Keep a list of every AI-touched asset: art, portraits, props, textures, voices, music, text, cutscenes, store art. Give each a status (ships, disclosed, to replace, replaced) and a replacement plan. Before launch, check the build and store page against it. Players found shipped placeholders in several recent games and the reaction was strong, and "we forgot to replace it" reads as indifference. One counter-case: a game with such a slip still sold well, so the cost isn't always sales.
- [Avoid · strong] **Generated stand-ins or props that ship** [D06-002]. Log each as a ticket with a gate: replace it before any demo or release, or disclose it if it stays. Search the final build, not just the source folders.
- [Avoid · anecdotal] **Disclosure added only after players found the AI** [D10-019]. Write the disclosure before launch. Say what is AI-made and what will be replaced, and make the store page match the build. A disclosure alone didn't stop complaints in one case, so check the build too.

### Platform rules (each line: checked 20 Oct 2026; re-check the live page)
- [Avoid · moderate] **Steam AI content survey doesn't match what ships** [D10-001]. Valve's survey asks about AI content that ships and that players see or hear. It splits pre-generated content from live-generated content, and live-generated content needs a description of guardrails. The rule that answers must match the build and store page comes from press and older wording, not the fetched page. Compare each survey answer with the asset register. Page: Steamworks "Content Survey" documentation.
- [Avoid · moderate] **AI in store capsule, key art, cover or trailer** [D10-002]. Treat store assets as in scope. Use real-build or human-made art there, or disclose. Valve's page doesn't say marketing art is covered; only press reports do. The audience reaction is well documented.
- [Avoid · moderate] **itch.io asset page with AI and no tag** [D10-003]. Tag the AI Disclosure section for any asset that contains generative AI, even after hand edits. The guidelines say asset pages are strictly enforced and an untagged one may be delisted, and mass-produced AI listings count as spam. The November 2024 start date is from press.
- [Avoid · moderate] **itch.io game with AI and no tag** [D10-004]. Games are covered too. The grace period delays enforcement, it doesn't waive the rule. Tagged games appear on an AI Assisted page. Page: itch.io quality guidelines.
- [Avoid · moderate] **Kickstarter AI section missing or vague** [D10-005]. The help article asks creators to name the AI tools, how the output enters the project and which elements AI makes, and says the creative work must come from humans. Projects that build AI tools face a consent question. The rules page and creator FAQ couldn't be opened, and reports of 2026 rule changes are from press only; read the live rules page.
- [Avoid · moderate] **Apple: AI content creation app without safeguards** [D10-006]. Only for apps with generative features. Guideline 1.2 asks for filtering, reporting, blocking and contact details. Guideline 5.1.2(i) covers sharing personal data with third-party AI. Apple updated its guidelines on 16 Oct 2026. Press claims about a new anti-bait-and-switch line are not on the page we read, so re-read 1.2 and 2.5.19 the day you submit.
- [Avoid · anecdotal] **Apple: AI-made screenshots that misrepresent the app** [D10-007]. Apple has no AI-specific screenshot rule on the pages read. Guideline 2.3.3 asks for screenshots showing the app in use. The AI angle comes from one blog. Check each screenshot against the binary.
- [Avoid · moderate] **Google Play: generative AI app without output safeguards** [D10-008]. Only where AI is a central feature, such as a chatbot. The policy holds developers responsible for offensive or deceptive output. Blog claims of a label or declaration date weren't on Google's page, so don't rely on them.
- [Avoid · moderate] **AI-touched work submitted to Lospec's gallery** [D10-009]. Lospec's 2023 announcement says no AI in the process. The submit page was seen only as a search snippet. Post AI-assisted pixel work elsewhere, labelled.
- [Avoid · anecdotal] **AI work posted on a handmade-art community** [D10-010]. Newgrounds and Fur Affinity banned AI art in 2022, per press; the current rule pages were not opened. Read each site's rules before posting.
- [Choose deliberately · moderate] **DeviantArt AI work without the "Created using AI tools" label** [D10-011]. The Terms require it for content offered for sale and recommend it otherwise. The Terms' effective date wasn't in the fetched text.
- [Choose deliberately · moderate] **ArtStation AI work without the CreatedWithAI tag** [D10-018]. The help article (dated 2 Sep 2026) requires the tag for Marketplace content and says viewers can filter AI work out. The Terms may be broader for portfolio posts, which is unresolved, so tag AI pieces to be safe.
- [Choose deliberately · moderate] **AI covers and cover copy in publishing** [D10-015]. Record AI use per asset. Disclose it where an award or contract rule applies. One awards body disqualified two titles over AI covers.

### Store page, capsule and trailer
- [Avoid · anecdotal] **Default generated key art or capsule** [D06-009]. Glossy, uncanny generator output makes players suspect the whole game. You can't judge the look from text, so report a hit only when the register, credits or store notes say the art is AI-made; otherwise list it under "Check this". Commission or hand-compose the capsule, and show real gameplay in the trailer. A hand-composed piece with a reason is fine. Don't accuse a clean look of being AI, because false accusations are common.
- [Avoid · anecdotal] **AI images in a trailer or showcase** [D10-013]. Fans check trailers frame by frame. Use footage from the real build, and label any AI-made still.
- [Choose deliberately · moderate] **AI-made ad not checked** [D10-014]. Check it for uncanny faces, motion and props, and on a phone with the sound off. Disclose where audiences may react. One brand pulled an AI ad within days. Data on how disclosure changes reaction is mixed.
- [Avoid · anecdotal] **Mixed or unreviewed art style across one game** [D06-008]. Mixed store and generated assets clash. Pick one style target and finish every asset to it, or start from one cohesive pack.
- For the look of pixel art or generated images, use `unclank-pixels` and `unclank-images` once they're released (planned). Don't repeat those checks here.

### Names, text and voices in the game
- [Avoid · strong] **Default fantasy name set** [D06-001]. Elara, Elias, Mara, Elena, Clara, Voss, Vance and similar fill the cast. The tell is a cluster: two or more of these names, or a Voss, Vance or Thorne surname. One common name such as Clara or Elena isn't a tell [D06-N06]. Count name frequency across all game text, including the cast list. Derive names from each culture in the setting. The pool differs by model, so re-check after a model change.
- [Avoid · anecdotal] **"Not X, it's Y" reframes in game text and store copy** [D06-003]. One instance is not a tell. Repetition across many texts is. Lead with the concrete thing. General prose tells belong to `unclank-prose`, not here.
- [Avoid · moderate] **Repetitive, flat NPC dialogue** [D06-004]. For runtime-generated dialogue, test each character with different player inputs and fix identical reply shapes or repeated lines. The cause can be a settings fault, not design. Sameness under varied input is the tell, not repetition as such.
- [Avoid · moderate] **Runtime AI characters that forget or contradict themselves** [D06-012]. Give each a fixed fact sheet and a running memory. Ask the same question several times and again after a long session.
- [Avoid · anecdotal] **Quests written as prose, not working state** [D06-005]. Build the state machine first (steps, flags, reward once), then write text against it. No generation call should gate a quest step. Play every quest to its end.
- [Avoid · anecdotal] **Unpolished one-prompt game** [D06-006]. A first prompt-built version runs but has a tiny content pool and little feel. A labelled prototype is fine.
- [Avoid · anecdotal] **Narrow content pool presented as variety** [D06-007]. Count the pool (words, templates, room types, quest beats) before shipping and hand-author what players see most.
- [Choose deliberately · anecdotal] **One default synthetic voice for every character** [D06-011]. A single narrator is a valid design. A default text-to-speech voice on the whole cast is the tell. Give main characters distinct voices, keep text-to-speech to minor disclosed lines, and listen to a scene through.

### Trust and false flags
- [Choose deliberately · anecdotal] **Disclosure may cost some trust** [D10-016]. Advice for writing the disclosure, not an audit hit. One working paper and music studies say labelled AI lowers trust. This is search-only evidence. Disclose where a platform requires it, and say what a human did.
- [Choose deliberately · anecdotal] **Human work flagged as AI** [D10-017]. Advice, not an audit hit. Keep layered files and work-in-progress shots. Don't change good work only to dodge a false flag.

## How to audit

1. **Find the surfaces:**
   - the game repo: strings, dialogue and quest files, asset folders, credits;
   - any asset register, ticket list or licence notes;
   - the store-page text, screenshots list, capsule and trailer description, if they are in the repo or supplied;
   - the built game, if you can run or inspect it.
2. **Ask the user for what isn't in the files.** Typical gaps: the Steam content survey answers, the itch.io AI Disclosure setting, the Kickstarter AI section, Apple and Google submission answers, the store page text, the trailer description, and which assets used AI. Don't guess any of them. If the user can't supply one, or you can't ask (an unattended run), list it as "not checked" and go on.
3. **Run every check** in the checklist, register first. Compare each disclosure answer with the register and with what ships. A hit needs evidence you can point to, such as two files that disagree. Report a Choose deliberately item only when the files show the default; you can't see intent, so say it may be deliberate. When you can't see enough to judge (an asset the register names isn't in the repo, or you can't view an image or hear a voice), it isn't a hit: list it under "Check this" and keep it out of the audit block. An older "checked" date on a register that matches what you can see is a "Check this", not a hit.
4. **Re-check the live rules.** For each platform the user is submitting to, open its live policy page and compare it with the line above. If the live page differs, say so and use the live page. If you can't open web pages, give the user each page to re-check and don't claim a live check.
5. **Group hits that share a fix.** One missing register causes several hits.
6. **Write the report:**
   - Avoid hits first, worst first, then Choose deliberately. Give each hit its tell ID, file and line, what you saw, and the fix in one line.
   - Keep the tone neutral. Say what doesn't match, not that AI is bad.
   - List the checks that passed in one line, and the platform rules you re-checked live with the date, then the "Check this" items.
7. **End with the audit block,** exactly in this form. Use one line per hit, and leave out the "Check this" items. The label is exactly `Avoid` or `Choose deliberately`; for an inferred hit, start the note with `inferred:`. For a platform-level finding, give the file where the disclosure lives (for example the store-page text or a notes file), or `-` for the file and line if there is none. If there are no hits, write the two marker lines with nothing between them.

```
UNCLANK-AUDIT
D10-012 | Avoid | assets/portraits/guard.png:- | AI portrait in build, not in register
D10-001 | Avoid | steam-survey.md:- | survey says no AI content, build has AI voices
D06-001 | Avoid | data/npcs.json:14 | cast names are Elara, Elias, Mara, Voss
END-UNCLANK-AUDIT
```

## Ground rules

- Check your own or the user's work. Don't use these signals to accuse anyone of using AI: human work gets flagged as AI too [D10-017].
- Don't flag anything on the Not a tell list. When unsure, say "check this" rather than calling it a hit.
- Never present a platform rule as current. Give the "checked" date and send the user to the live page. Don't give legal advice.
- In audit mode, change nothing until the user asks.
- For site defaults use `unclank-launch`. For the look of pixel art and AI images, `unclank-pixels` and `unclank-images` are planned.

Last reviewed: 21 Oct 2026. Platform rules last checked: 20 Oct 2026. Evidence: `references/evidence.md`. Full research: `research/domains/D10-audience-platform-reaction.md` and `research/domains/D06-game-design.md`.
