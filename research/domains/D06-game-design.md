# D06 game-design

What makes a game itself, not its art, read as low-effort AI output: the LLM fantasy name set, repetitive or forgetful NPC dialogue, quests that exist only as text, one-prompt browser games shipped unpolished, narrow content pools, generated assets that ship, and one default voice for every character. Store-page copy overlaps D01 and art style overlaps D04/D05, so only the game-specific angle is kept here. AI-disclosure rates at Steam Next Fest describe how common AI use is, not a tell: Eurogamer's count, reported by Engadget on 16 Jun 2026, is 1,704 tagged games of about 8,700 (19.5%), and PCGamesN found 10 of the top 100 demos. Later reports of an October count reuse the June numbers. Evidence is thin for most tells: many sources are vendor blogs or opinion pieces and are marked as such. Rounds 1 (breadth), 2 (depth) and 3 (depth on names, primary reviews, disclosure counts, voices, quest breakage) merged. The lead merged round 2 directly, because the PC was over its memory budget for helpers.

## Checklist
- [Avoid · strong] Do not let one fantasy name pool (Elara, Elias, Mara, Elena, Clara, Voss, Vance) fill the cast; derive names from each culture in the setting, count name frequency across all game text before shipping, and re-check after a model change. (D06-001)
- [Avoid · strong] Do not ship generated stand-in or prop assets; track each as a ticket and gate demos and releases on replacing it. (D06-002)
- [Avoid · moderate] Test runtime-generated NPC dialogue with a set of different player inputs and fix any character that gives the same reply shape or repeats lines. (D06-004)
- [Avoid · moderate] Give runtime AI characters a fixed fact sheet and a running memory of what they said and what the player did, then ask the same question several times and after a long session to catch forgetting and contradiction. (D06-012)

## Tells

### D06-001 Default fantasy name set
- Label: Avoid
- Confidence: strong (4 fetched, non-vendor origins: Read's measured book count, Thomas's informal test, Wattenberg's own chatbot test, and Hamilton and Mimno's measured count over 20,000 stories; plus one game's store page, Synvelia, as game-specific support. Wattenberg's book counts repeat Read's and the Cornell Chronicle article repeats the paper, so neither is counted separately. Evidence is from fiction, not games, except the one game page.) Lead review 20 Oct (r2): upgraded from moderate on Wattenberg's fetched page. Round 3 adds the measured study and a game cast, so the level stays strong on a firmer base.
- Dated: noted from Aug 2025 (Max Read), named a 2025 Name of the Year in Dec 2025 (Wattenberg), measured May 2026 (Hamilton and Mimno), covered by Cornell in Oct 2026
- Why it reads as AI: Models draw protagonists and NPCs from a small pool of high-probability names, so the same sounds recur across unrelated characters and readers now take them as a default, not a choice.
- Fix: Write a naming culture per region or faction, derive names from it, and run a name-frequency check over the whole game's text, including the cast list. Banning one name is not enough, because the model drifts to a neighbour with the same sound, and the pool differs by model, so a clean result on one model does not carry over to another.
- Example done well: none given
- Sources: S-D06-001, S-D06-002, S-D06-003, S-D06-004, S-D06-052, S-D06-053, S-D06-054
- Flag: Read (fetched, lead-spot-checked) gives measured data: 62 Amazon books credited to Elara Voss, and recurring names such as Elara Voss, Elias Vance and Aris Thorne. Wattenberg (fetched) reports 120 AI-generated Goodreads titles with an Elara character; her own test of three chatbots and 15 names paired Elena and Clara with Voss or Vance. Hamilton and Mimno (arXiv preprint, fetched; Section 3 figures checked in the HTML version) found Elias in 26.5% of 20,000 stories (5,294), Mara in 16.7% (3,345) and Elara in 13.1% (2,627), across Claude Haiku 4.5, Gemini 3.1 Flash-Lite, GPT-5.4-Mini and OLMo 7b Thinking, with preferences differing by model. These are small, cheap models and the prompts were story prompts, not game briefs. A Pith review (search only) says the paper's preference-data explanation lacks shown counts or controls, so cite the paper for the counts, not for the cause. The Cornell Chronicle piece (fetched) gives no name-level figures. Synvelia (fetched, developer's own itch.io page, adult content; only the cast list and the disclosure field are cited) lists four Voss characters (Elara, Marcus, Izabella, Milan) among five cast members, plus Lina Marlowe, and its AI-disclosure field tags Text as AI-assisted. It is one game's page, so one origin: it shows the pattern exists in a shipped game, not how common it is. The page's description says writing is credited to a human, so the disclosure field and description do not fully agree, and neither shows how the names were chosen. Kael has no source and is removed from the pool; Thorne rests only on Read's "Aris Thorne". S-D06-004 (the 76% blocklist figure) is still unverified and not counted; a search snippet gives 763 of 1,000 openings, which matches only if the snippet is accurate. Forbes (S-D06-049) is search only and no research behind it was identified, so it is no longer cited here.

### D06-002 Generated stand-in and prop assets that ship
- Label: Avoid
- Confidence: strong (4 independent, fetched press items: Kotaku's trend piece, PCGamesN's count, the Pearl Abyss case via Engadget, the Clair Obscur case via Indiecator). Lead review 20 Oct (r2): upgraded from moderate. The lead spot-checked Kotaku (Zwiezen, 15 Jun 2026) and PCGamesN (Sledge, 24 Feb 2026).
- Dated: noted from Feb 2026, still cited Oct 2026
- Why it reads as AI: Generated stand-ins are often visibly generic, so one left in a demo or release tells players that nobody checked, and one slipped asset makes them doubt the rest.
- Fix: Log every stand-in as a ticket with a replacement gate before any demo or release, and disclose any generated content that stays.
- Fixable: no, replace with hand-made or commissioned assets
- Sources: S-D06-016, S-D06-017, S-D06-018, S-D06-019, S-D06-041, S-D06-042, S-D06-050
- Flag: PCGamesN's figure is narrower than it sounds. 10 of the top 100 Next Fest demos disclosed generative AI, and 4 of those 10 said it was for placeholder images or music. That is 4 in 100, all self-reported, not a count of visible tells. Kotaku is opinion on the trend, with no count: on a personalised hub, 10 of the 16 games Zwiezen opened carried an AI disclosure. Pearl Abyss called the Crimson Desert props early-iteration assets "unintentionally included", not placeholders, so that case is a slip. The Clair Obscur case is second-hand. Vapor World's AI cutscenes were pulled within days after backlash (search only). Placeholder use is honest when disclosed and replaced (see Not a tell, D06-N04).

### D06-003 "Not X, it's Y" reframes in game text and store copy
- Label: Avoid
- Confidence: anecdotal (lead review 20 Oct: downgraded from moderate; all three sources are search only, none is about games, and the two guides may share one list. The prose tell itself is covered in D01; this entry only notes it also shows up in game text.)
- Dated: noted 2025, still cited Oct 2026
- Why it reads as AI: The contrast construction is a statistically common model default, so it shows up in blurbs, item descriptions and flavour text and is now recognised as machine-written.
- Fix: Lead with the concrete thing and its use; keep a contrast sentence only when the contrast carries information.
- Sources: S-D06-024, S-D06-025, S-D06-026
- Flag: All three sources are search only, and none is about games; the game-specific angle (item text, blurbs) is inferred. S-D06-024 concerns an AI-generated book's blurb. Humans use the construction too, so one instance is not a tell; repetition across many texts is. See also: D01, and D06-010 (dropped), whose generic-text point now lives here.

### D06-004 Repetitive, flat NPC dialogue
- Label: Avoid
- Confidence: moderate for repetition in runtime-generated dialogue (2 fetched origins: critic reviews of AI2U cited on its Wikipedia page, and a player thread on Formamorph; HowWorks's itch.io quotes may overlap with the second, so they are not counted separately). Anecdotal for the "one flat voice / therapy-speak" half (1 opinion piece plus one search-only demo anecdote). Lead review 20 Oct (r2): upgraded from anecdotal for the repetition half only. Round 3 kept moderate: the primary AI2U Steam reviews, now fetched, are partial counter-evidence (see Flag), and the new Formamorph thread replaces them as the second origin.
- Dated: noted from July 2025 (Wayline); AI2U reviews from Jan 2025; Formamorph thread June 2025; player complaints collected Aug 2026
- Why it reads as AI: Runtime models fall back on the same reply shape, so a character answers alike whatever the player says, and pattern completion averages voices, so the cast sounds like one writer.
- Fix: Write a voice sheet per speaker (vocabulary, what they never say, how they deflect), hand-write any line that must carry subtext, and test each character with a set of different player inputs to catch identical replies. Keep a short log of recent replies per character and reject a reply that matches a recent one.
- Sources: S-D06-005, S-D06-006, S-D06-007, S-D06-044, S-D06-045, S-D06-051, S-D06-057, S-D06-058, S-D06-059
- Flag: Counter-evidence on repetition: the AI2U Steam top-rated reviews (S-D06-057, fetched, ten reviews) do not mainly complain about repeating dialogue. They complain that the AI forgets, contradicts itself, is censored or does not know the game world, and some praise the open-endedness; the one review that mentions loops also says one question got five contradictory answers. Treat them as evidence for D06-012, not for this tell. Wikipedia (S-D06-044) says critics criticised repetitiveness, which is the secondary basis for the repetition half; the critics' own reviews were not fetched. Formamorph (S-D06-058, fetched) is a player thread in which the developer blamed local-model memory settings and possibly the Android build, so the repeat may be a configuration fault. HowWorks's vendor status was not checked, and its examples include AI roleplay chat products as well as games. Repeated lines also happen in fully recorded games (HN comment, search only), so the tell is sameness under varied input, not repetition as such. The VR study (search only) reports unnatural flow and uninformative answers, which supports the general complaint only. Mason's write-up (S-D06-059) is search only (fetch returned 403) and is not counted; no GDC Vault or schedule entry for a talk on repetitive NPC dialogue was found, so any claim that a GDC 2026 talk covered it is unverified and is not made here.

### D06-005 Quests written as prose, not working state
- Label: Avoid
- Confidence: anecdotal (1 vendor blog; 1 search-only patch round-up; plus one fetched forum thread about a different failure, below. The measured study is about text quality, not quest state.)
- Dated: GPT-2 quest study online Dec 2022; AI Roguelite thread Dec 2022; noted for AI RPGs June to Sep 2026
- Why it reads as AI: A text generator describes a quest without building its trigger, objective check, flags or gated reward, so the quest breaks in play (early rewards, wrong objective checks, stranded branches).
- Fix: Build the state machine first (steps, flags, reward once), write text against it, then play every quest to its end. Do not let a generation call gate a quest step; gate each step on a check that does not depend on generated text.
- Sources: S-D06-008, S-D06-040, S-D06-047, S-D06-060
- Flag: S-D06-008 is a vendor blog (SummerEngine) and says hand-written quests break in play too, so the tell is untested content, not AI drafting. The "1 in 5 acceptable" figure comes from Värtinen et al. (IEEE Transactions on Games, 2024; 349 players; a fine-tuned GPT-2), not the arXiv scoping review (S-D06-009). It measures the quality of quest descriptions on a 2022-era model, not whether quests work. The Arcanum round-up of NPCs failing after being killed is search only. The AI Roguelite thread (S-D06-060, fetched Steam forum) is a runtime generation failure, not AI-written quest state: quests could not be started after the first few because the local generation server ran out of GPU memory and saves held long generated text; the developer shipped two patches and said the cause was only partly found. It supports the "quest depends on generated text" point only, and the game was clearly being played, so the failure was found in play. The thread predates the October 2023 release that Arcanum's search snippet lists, so the game was probably in early access or a demo; its status was not checked.

### D06-006 Unpolished one-prompt ("vibe-coded") game
- Label: Avoid
- Confidence: anecdotal (press accounts and forum comments; no measured data)
- Dated: noted March 2025, still discussed April 2026
- Why it reads as AI: Output matches the literal ask and little beyond it, so the first prompt-built version runs but has a tiny content pool, rough feel and little playtesting, and the defaults show through.
- Fix: Add one mechanic at a time and playtest each step, write the content list by hand, and treat feel (timing, feedback, juice) as a human pass. A prototype labelled as one is fine (see Not a tell, D06-N02).
- Sources: S-D06-010, S-D06-011, S-D06-012, S-D06-013, S-D06-014
- Flag: Decrypt (S-D06-010) only partly supports this: it reports a repetitive 10-word list and a lack of polish and optimisation in a first prompt-built version, and never calls the game shallow or generic. Cite it only for repetitive content and no polish in a first version. Slate (S-D06-011) calls the result weird and bad but names no design fault. The two Hacker News items are search only, second-hand comments. Klimek (S-D06-014) is blog (opinion) and says prototypes come fast but feel needs iteration. Playable AI-built games exist, so the tell is shipping unplayed first-pass output.

### D06-007 Narrow content pool presented as variety
- Label: Avoid
- Confidence: anecdotal (1 fetched example; 1 fetched opinion piece with no named games)
- Dated: procedural repetition is long-standing; noted 2025-2026 for AI-era content
- Why it reads as AI: A small pool recombined looks like breadth at first and repeats within minutes.
- Fix: Count the pool (words, templates, room types, quest beats) before shipping, and hand-author the parts players see most.
- Sources: S-D06-010, S-D06-015, S-D06-043
- Flag: The Decrypt typing game (about ten words) is also the thin evidence for D06-006. PokGaiGamer (fetched) is opinion with no named games. Insider Gaming (S-D06-015, now fetched) is about Starfield's hand-built locations and does not mention AI. It shows that players complain about repetition whatever made the content. The tell is the repeat, not AI origin. A Stanford "Digital Economy Lab" figure (18% lower sales) is excluded: the blog page that cites it (fetched in round 3) gives no paper title, authors or link, and searches found no such games study. Procedural generation itself is not the tell (see D06-N01).

### D06-008 Mixed or unreviewed art style across one game
- Label: Avoid (unreviewed mix of store and generated assets); Choose deliberately (one cohesive pack, see D06-N03)
- Confidence: anecdotal (2 vendor blogs, search only, which may repeat each other)
- Dated: noted 2026
- Why it reads as AI: Store and generated assets each have a default look; combined without direction they clash, and players infer nobody led the art.
- Fix: Pick one style target and hand-finish every asset to it, or start from one cohesive pack.
- Fixable: partly (a hand style pass; the visual domains judge the image-level fixes)
- Sources: S-D06-020, S-D06-021
- Flag: Both sources are dev-tool company blogs (vendor) seen only as search snippets, and likely repeat each other, so they count as one. Inconsistency alone is not proof of AI: a developer denied claims drawn from art that looked too clean (see D06-N04). See also: D04, D05.

### D06-009 Store-page and trailer tells (game-specific angle)
- Label: Avoid (default generated key art); Choose deliberately (hand-composed art with a reason)
- Confidence: anecdotal (2 search-only press items)
- Dated: noted 2026
- Why it reads as AI: Default generator output has a glossy, uncanny look that players now recognise, and it makes them suspect the whole game.
- Fix: Commission or hand-compose the capsule and show real gameplay in the trailer, not only key art.
- Sources: S-D06-022, S-D06-023
- Flag: Both items are search only. S-D06-022 is Pocketpair's John Buckley as quoted in Creative Bloq (the fetch of that page returned boilerplate), and calls AI capsule art an immediate turn-off. A single trailer accused of being generated is weak evidence, since false accusations on a "too clean" look are common (see D06-N04). See also: D01, D04.

### D06-010 Generic lore and item descriptions (dropped in round 2)
- Label: Avoid
- Confidence: dropped (lead review 20 Oct, r2). Its only supports are a hypothetical example (Wayline) and a satire page (Mojo Games), and round 2 found no game-specific evidence. The general point, generic text with no specifics, is covered by D06-003 and D01. Reviewed AI-drafted lore is not a tell (D06-N08).
- Sources: S-D06-005, S-D06-027

### D06-011 One default synthetic voice for every character
- Label: Choose deliberately (a single narrator is a valid design; a default text-to-speech voice applied to the whole cast is the tell)
- Confidence: anecdotal (1 fetched review with a disclosed conflict of interest, plus one narrower fetched press case, Arc Raiders, that does not show a whole cast on one voice)
- Dated: noted Sep 2026; Arc Raiders voice lines drew objections from launch in Oct 2025 and were partly re-recorded by Mar 2026
- Why it reads as AI: When one default text-to-speech narrator reads every line, a whole town sounds like one person and the cast loses its distinct voices.
- Fix: Give each main character a distinct voice, or keep a single narrator only as a deliberate, switchable choice, keep text-to-speech to minor, disclosed lines, and listen to a scene through to check.
- Sources: S-D06-046, S-D06-061, S-D06-062, S-D06-063
- Flag: The Arcanum review (S-D06-046) is single-source: the reviewer had free access from the developer, which the review discloses, and the narrator can be switched off. It is a voice-design point and does not show that AI writing is the cause. Arc Raiders (Kotaku, fetched, 13 Mar 2026) is a narrower case: text-to-speech built on licensed actor audio was used mainly for location-ping lines, not the story cast; players and some actors objected, and the developer re-recorded some lines with actors and kept text-to-speech for select lines. The developer says it uses AI as a production tool and not to cut costs, which is its own claim. Engadget and GameSpot report the same replacement and are search only; with Kotaku they count as one origin. The Arc Raiders attribution is to Kotaku, not Eurogamer, whose article was not found. See D06-N09 for the one-disclosed-AI-voice counterpart.

### D06-012 Runtime AI characters that forget and contradict themselves
- Label: Avoid
- Confidence: moderate (2 fetched, non-vendor player-comment origins in two different games: top-rated Steam reviews of AI2U, where memory or dialogue problems appear in 3 to 4 of 10 reviews, and a Formamorph itch.io thread reporting the model acts as if the player had just started, even with notes added. Lead call 20 Oct: one game's reviews alone would be anecdotal; a second game backing the failure makes it moderate. The Formamorph evidence covers forgetting, not contradiction.) Lead review 20 Oct (r3): moderate accepted at the minimum. Two games' players, both fetched; AI2U covers forgetting and contradiction, Formamorph only forgetting. Drop to anecdotal if no third game turns up.
- Dated: AI2U reviews undated (Early Access since 23 Jan 2025, per a search snippet); Formamorph thread June 2025
- Why it reads as AI: A runtime model keeps no fixed record of what a character said, what the player did or what the game world contains, so facts change between asks, earlier events vanish and the character shows no sense of its own world. Players describe this as the AI being dumb, more often than as repetition.
- Fix: Write a fixed fact sheet per character and for the world and send it every turn, keep a running summary of what the player did and what the character stated, and test by asking the same question several times and again after a long session.
- Sources: S-D06-057, S-D06-058, S-D06-067
- Flag: Neither source is a controlled test. Both are self-selected player posts, and the AI2U page is one game's reviews, so it is one origin. Several AI2U negatives are about censorship, cost and voice input, not memory, and some reviewers praise the open-endedness. The Formamorph developer blamed local-model memory settings and possibly the Android build, so the failure may be configuration, not design. The fetch tool returns a model summary of each page, so paraphrase is used and the wording was not checked against the page text. Store totals (about 88% positive from about 1,950 reviews) are search only. Roguelite quest failure (D06-005) is a different fault, a generation crash, and is not counted here.

## Not a tell

### D06-N01 Procedural generation as a technique
- Why it is fine: A hand-authored core with generated periphery is a long-standing, respected design (for example Caves of Qud's hand-made towns and story with generated dungeons and history). Critics target narrow pools, not the technique (see D06-007).
- Sources: S-D06-028, S-D06-029

### D06-N02 Simple mechanics and small scope
- Why it is fine: One loop, a short run and a narrow scope are legitimate design choices; a small two-person game and a solo-made poker roguelike both did well. The tell is unexamined defaults inside a small scope.
- Sources: S-D06-030, S-D06-031

### D06-N03 One cohesive art pack
- Why it is fine: A single consistent free or store pack gives a unified style for prototypes and jams. Unmodified use can read as a template, so finish or modify the assets (see D06-008).
- Sources: S-D06-032, S-D06-033

### D06-N04 Disclosing AI use; judging a game by a "clean" look
- Why it is fine: A store-page disclosure is honesty, not a quality signal. Steam has required one since January 2024; a vendor blog (search snippet only, so unconfirmed) says Valve rewrote the rules on 17 Jan 2026 so that dev tools need no disclosure while live-generated content does, which should be checked against Valve's own documentation before it is cited. Disclosure wording varies and is self-reported, and false accusations are common (a developer denied claims against a game whose art and writing were human-made). Disclosure rates only show how common AI use is: Eurogamer's count, via Engadget, is 1,704 tagged demos of about 8,700 (19.5%) at the June 2026 Next Fest. The Kotaku piece gives no visual or textual tell its author spotted himself, only developers' disclosures. Do not count a disclosure as a tell, and do not treat clean art as proof of AI.
- Sources: S-D06-016, S-D06-021, S-D06-034, S-D06-035, S-D06-036, S-D06-066

### D06-N05 Em dashes in fiction, alone
- Why it is fine: One writer argues em dashes are a weak signal in fiction and uses them himself. Other sources list them among AI tells, so count them only together with other patterns such as D06-003.
- Sources: S-D06-037, S-D06-024

### D06-N06 One uncommon fantasy-sounding name
- Why it is fine: A single use of a name like Elara is harmless; the tell is clustering across a cast or project (D06-001), not presence of one name. Some parents chose Elara before AI. In one interactive-fiction jam thread, a single Elara Voss was noticed, but two of the three people who looked did not read the writing as AI, and the jam allows AI brainstorming; one Steam visual novel has a protagonist named Elara and no Voss household, and its plot comes from a novel.
- Sources: S-D06-002, S-D06-003, S-D06-055, S-D06-056

### D06-N07 Following a popular genre formula
- Why it is fine: Making a Balatro-like, roguelike or deckbuilder is not an AI tell; a crowded micro-genre is a discoverability issue. Clone-by-prompt is a copying concern, not a tell in the game itself.
- Sources: S-D06-038, S-D06-039

### D06-N08 AI-drafted lore and item text that a team edits
- Why it is fine: One developer-consultant guide calls drafting item descriptions and background lore among the least controversial uses, provided the shipped text has one consistent voice and has been reviewed for tone and continuity. Text that still reads unedited is the problem, not drafting. Single source, vendor-like.
- Sources: S-D06-048

### D06-N09 One disclosed AI voice for one character, with a stated reason
- Why it is fine: In Active Matter, one character is voiced by generative AI and every human character by real actors; the store page says so, and the developer describes it as an artistic choice, not a cost cut. A single disclosed AI voice does not make a cast sound like one speaker, so it falls outside D06-011. It is not free of cost: the press called the notice distasteful and an edgy joke, and one review (search only) found the voice jarring when it repeats lines. Treat it as a deliberate choice that still has to earn its reason with players, not as an endorsement.
- Lead note 20 Oct (r3): contested. Press criticised the choice, so this shows that disclosure plus a stated reason is the floor, not that it passes. Read with D06-011 (Choose deliberately).
- Sources: S-D06-064, S-D06-065

## Sources
S-D06-001 | Who is Elara Voss? (Max Read); attributes the name's pull to two MMO characters, Lilian Voss (World of Warcraft) and Elara Dorne (Star Wars: The Old Republic), as a plausible explanation and not proof | https://maxread.substack.com/p/who-is-elara-voss | 2025-08-07 | blog | | fetched (lead-verified)
S-D06-002 | The Elara problem (Chris Thomas) | https://microblog.christhomas.co.uk/blog/the-elara-bias | 2026-06-05 | blog | | fetched
S-D06-003 | The 2025 Name of the Year is Elara (Laura Wattenberg, Namerology) | https://namerology.com/2025/12/15/2025-name-of-the-year-is-elara-the-favorite-name-of-ai/ | 2025-12-15 | blog | | fetched (r2)
S-D06-004 | TomLikesRobots blocklist experiment (1,000 story openings; 76% figure, unverified; a search snippet gives 763 of 1,000) | https://x.com/TomLikesRobots/article/2074504762448339243 | about July 2026 | blog | | search only (page returned HTTP 402 twice)
S-D06-005 | The Uncanny Valley of AI Dialogue (Gemma Ellison, Wayline), blog (opinion), hypothetical examples | https://www.wayline.io/blog/uncanny-valley-ai-dialogue-video-games | 2025-07-05 | blog | | fetched
S-D06-006 | Aftermath on Nvidia, Convai, Inworld and Ubisoft AI NPC demos | https://aftermath.site/ai-npcs-nvidia-unity-ubisoft-convai-inworld/ | date not captured | press | | search only
S-D06-007 | Dialogs with GenAI NPCs: Exploring Player Interactions with Speech Agents in a VR Game | https://www.tandfonline.com/doi/full/10.1080/10447318.2026.2620647 | 2026 | study | | search only
S-D06-008 | AI Quest Generator for Games (Summer Team, SummerEngine) (vendor) | https://www.summerengine.com/blog/ai-quest-generator | 2026-06-06 | blog | | fetched
S-D06-009 | Large Language Models and Video Games: A Preliminary Scoping Review (Sweetser) | https://arxiv.org/pdf/2403.02613 | 2024 | study | | abstract fetched in r2; it does NOT contain the "1 in 5" quest figure (see S-D06-040); no longer cited for it
S-D06-010 | Does Vibe Coding Really Work? We Built a Game With Claude (Jose Antonio Lanz, Decrypt) | https://decrypt.co/311183/we-built-game-vibe-coding-ai-claude | 2025-03-23 | press | | fetched
S-D06-011 | Slate on a browser game built with Claude Code | https://slate.com/technology/2026/04/ai-vibe-coding-video-game.html | 2026-04-05 | press | | fetched
S-D06-012 | Hacker News: Mmorpg World of ClaudeCraft, vibe coded | https://news.ycombinator.com/item?id=48509143 | 2026 | forum | | search only
S-D06-013 | Hacker News: I'm helping my dog vibe code games | https://news.ycombinator.com/item?id=47139675 | 2026 | forum | | search only
S-D06-014 | Can I vibe code a game in 2026? (Maurice Klimek, Gamedev Diary), blog (opinion) | https://gamedevdairy.substack.com/p/can-i-vibe-code-a-game-in-2026 | 2025-12-29 | blog | | fetched
S-D06-015 | Insider Gaming (Andrew Highton): ex-Starfield dev on repeated locations and lack of procedural content; hand-built content, no AI | https://insider-gaming.com/ex-starfield-dev-doesnt-think-game-is-great-and-blames-lack-of-procedural-content/ | 2026-08-05 | press | | fetched (r2)
S-D06-016 | Kotaku (Zack Zwiezen): Exploring Steam Next Fest with an AI-blocking extension is very depressing | https://kotaku.com/exploring-steam-next-fest-with-an-ai-blocking-extension-is-very-depressing-2000706695 | 2026-06-15 | press (commentary) | | fetched (lead-verified r2)
S-D06-017 | PCGamesN (Ben Sledge): top 100 Next Fest demos, 10 disclose generative AI, 4 of those for placeholders | https://www.pcgamesn.com/steam/next-fest-2026-generative-ai | 2026-02-24 | press | | fetched (lead-verified r2)
S-D06-018 | Engadget (Jackson Chen): Crimson Desert developer apologises and promises to replace AI-generated art (other outlets covering the same statement count as one) | https://www.engadget.com/gaming/crimson-desert-developer-apologizes-and-promises-to-replace-ai-generated-art-183716439.html | 2026-03-22 | press | | fetched (r2)
S-D06-019 | PC Gamer on Vapor World's AI cutscenes ("quintessential slop") | URL not given in raw file | 2026 | press | | search only
S-D06-020 | Soonlab guide to Steam AI games (vendor) | https://www.soonlab.ai/blog/steam-ai-games/ | 2026 | blog | | search only
S-D06-021 | StraySpark: Steam AI disclosure rules 2026, indie developer guide (vendor); a search snippet says Valve rewrote its disclosure rules on 17 Jan 2026 | https://www.strayspark.studio/blog/steam-ai-disclosure-rules-2026-indie-developer-guide | 2026-03 | blog | | search only
S-D06-022 | Creative Bloq on Next Fest, quoting Pocketpair's John Buckley on AI capsule art | URL not given in raw file | 2026-02 | press | | search only
S-D06-023 | PC Gamer: AI-made games are easy to spot, capsule art has an uncanny sheen | URL not given in raw file | 2026 | press | | search only
S-D06-024 | ABC News (Cam Wilson) on an AI-generated book about him | https://www.abc.net.au/news/2026-10-10/cam-wilson-ai-book-copyright-laws/107220714 | 2026-10-10 | press | | search only
S-D06-025 | tropes.fyi list of AI writing tropes | https://gist.github.com/ossa-ma/f3baa9d25154c33095e22272c631f5a1 | 2026-10 | guide | | search only
S-D06-026 | Peter Yang's open-source no-ai-slop skill | https://github.com/petergyang/no-ai-slop | 2026 | guide | | search only
S-D06-027 | Mojo Games satirical "AI Slop" Steam page | URL not given in raw file | 2026-06 | other (satire) | | search only
S-D06-028 | Tapping into the potential of procedural generation in Caves of Qud (Game Developer) | https://www.gamedeveloper.com/design/tapping-into-the-potential-of-procedural-generation-in-caves-of-qud | about 2023 (date not captured) | press | | search only
S-D06-029 | RPG Codex review on procedural generation | https://rpgcodex.net/article.php?id=12491 | 2024 | forum | | search only
S-D06-030 | GamesRadar on Combolands (97% positive Steam reviews) | URL not given in raw file | 2026-09-24 | press | | search only
S-D06-031 | Balatro (Wikipedia) | URL not given in raw file | date not captured | other | | search only
S-D06-032 | Kenney game assets (itch.io) | https://kenney.itch.io/kenney-game-assets | date not captured | other (developer site) | | search only
S-D06-033 | Kenney vs Quaternius: best free CC0 game assets (3dxdev) | https://3dxdev.com/kenney-vs-quaternius-the-best-free-cc0-game-assets/ | 2026 | guide | | search only
S-D06-034 | Techdirt on Kotaku's pre-judging of AI in gaming coverage | https://www.techdirt.com/2026/06/23/kotakus-pre-judging-ai-in-gaming-coverage-is-getting-very-dumb/ | 2026-06-23 | blog | | search only (page returned HTTP 403)
S-D06-035 | Vice: Steam reviews have a serious AI problem that needs to be fixed | https://www.vice.com/en/article/steam-reviews-have-a-serious-ai-problem-that-needs-to-be-fixed/ | 2025-12-17 | press | | search only
S-D06-036 | Steam AI disclosure policy and community threads (required since Jan 2024) | URL not given in raw file | 2024-01 | policy | | search only
S-D06-037 | Kevin Hess, Substack, on em dashes in fiction | URL not given in raw file | date not captured | blog | | search only
S-D06-038 | 2025 Next Fest roundup and Rock Paper Shotgun satire on the crowded Balatro-like genre | URL not given in raw file | 2025 | press | | search only
S-D06-039 | Kotaku on people vibe-coding clones of developers' games | URL not given in raw file | 2026-07 | press | | search only
S-D06-040 | Generating Role-Playing Game Quests With GPT Language Models (Värtinen, Hämäläinen, Guckelsberger), IEEE Transactions on Games 16(1); 349 players, fine-tuned GPT-2 | https://research.aalto.fi/en/publications/generating-role-playing-game-quests-with-gpt-language-models/ | 2024 (online 2022-12-12) | study | | fetched (portal abstract)
S-D06-041 | Indiecator (MagiWasTaken): Steam Next Fest has an AI problem; Clair Obscur placeholder art; Eurogamer disclosure count (its 8,682 total, also on a ResetEra post, is not the figure Eurogamer reports via Engadget; see S-D06-066) | https://indiecator.org/2026/06/16/steam-next-fest-has-an-ai-problem-and-players-cant-filter-it-out/ | 2026-06-16 | blog | via Eurogamer (counts) | fetched
S-D06-042 | GamesRadar: Crimson Desert replaces AI-generated assets left in by accident (patch 1.01.00) | https://www.gamesradar.com/games/rpg/crimson-desert-replaces-ai-generated-assets-left-in-the-game-by-accident-as-part-of-ongoing-visual-improvements-alongside-improvements-to-loading-and-controls/ | 2026 | press | | search only
S-D06-043 | PokGaiGamer: AI-generated games 2026 (opinion, no named games) | https://www.pokgaigamer.com/p/aigengames2026 | 2026-09-22 | blog | | fetched
S-D06-044 | AI2U: With You 'Til The End (Wikipedia; reviews by Twisted Voxel, Indie Game World, IXBT and Anime News Network cited there; says critics criticised repetitiveness) | https://en.wikipedia.org/wiki/AI2U:_With_You_%27Til_The_End | 2025 | other (reference) | via the cited reviews | fetched
S-D06-045 | HowWorks: 6 things players actually complain about in AI roleplay (quotes itch.io comments) | https://howworks.ai/blog/ai-roleplay-complaints | 2026-08-07 | blog (vendor status not checked) | via itch.io | fetched
S-D06-046 | Arcanum RPGs (Rukka): AI Roleplay With Voice (2026); free access from the developer, disclosed | https://arcanumrpgs.com/blog/ai-rpg-voice/ | 2026-09-13 | blog | | fetched
S-D06-047 | Arcanum RPGs: AI RPG news round-up, 29 Sep 2026 (NPC and quest-state bugs in patch notes) | https://arcanumrpgs.com/blog/ai-rpg-news-2026-09-29/ | 2026-09-29 | blog | | search only
S-D06-048 | StraySpark: Steam AI disclosure examples for indie devs (example 7, drafted lore and item text) | https://www.strayspark.studio/blog/steam-ai-disclosure-examples-indie-developers-2026 | 2026-05-18 | blog (vendor-like consultant) | | fetched
S-D06-049 | Forbes (Lance Eliot): why AI keeps inventing the same fake names. Not cited by any tell: the research behind it is not identified, and a Startup Fortune rewrite (fetched) cites studies that are not about names | https://www.forbes.com/sites/lanceeliot/2026/06/21/solution-to-the-curious-mystery-of-why-ai-keeps-inventing-the-same-fake-names-over-and-over-again/ | 2026-06-21 | press | | search only (HTTP 403)
S-D06-050 | Everything Edinburgh: Vapor World Steam AI cutscene backlash | https://everythingedinburgh.com/games/news/vapor-world-steam-ai-cutscene-backlash/ | 2026 | press | | search only
S-D06-051 | Hacker News comment: any world of recorded civilians repeats lines (counter-evidence) | https://news.ycombinator.com/item?id=36522665 | 2023 | forum | | search only
S-D06-052 | Hamilton and Mimno, "Elias in the Lighthouse, Again? Diagnosing Low Diversity in LLM Stories" (Cornell; arXiv 2605.26492v1; counts checked in the HTML version, https://arxiv.org/html/2605.26492v1) | https://arxiv.org/abs/2605.26492 | 2026-05-26 | study | | fetched (abstract and Section 3)
S-D06-053 | Cornell Chronicle: Who is Elias the lighthouse keeper? (reports the same paper; names the models only as ChatGPT, Claude, Gemini and OLMo and gives no name-level figures; counts as one origin with S-D06-052) | https://news.cornell.edu/stories/2026/10/who-elias-lighthouse-keeper-ai-fiction-tells-same-old-story | 2026-10-19 | press | | fetched
S-D06-054 | Synvelia (itch.io developer page); adult content, only the cast list and the AI-disclosure field are cited | https://synveliastudio.itch.io/synvelia | 2026-10 | other (developer store page) | | fetched
S-D06-055 | Interactive Fiction Community Forum: Beneath the Exhibition and Elara Voss (Text Adventure Literacy Jam 2026 entry) | https://intfiction.org/t/beneath-the-exhibition-and-elara-voss/80429 | 2026-05-30 to 2026-05-31 | forum | | fetched
S-D06-056 | Elara (visual novel, LoveOtheRing), Steam store page; protagonist named Elara, AI-assisted visuals and voice, plot from a novel | https://store.steampowered.com/app/3634400/Elara/ | 2025-04-28 | other (store page) | | fetched
S-D06-057 | AI2U: With You 'Til The End, Steam community top-rated reviews (ten reviews read) | https://steamcommunity.com/app/2880730/reviews/?browsefilter=toprated | date not captured | forum (store reviews) | | fetched
S-D06-058 | Formamorph itch.io community thread: the AI are dumb and lot of repeat dialogue | https://itch.io/t/4968507/the-ai-are-dumb-and-lot-of-repeat-dialogue | 2025-06-09 | forum | | fetched
S-D06-059 | Hilary Mason, "The State of AI-Native Games: Lessons from the Frontier" (Medium; described as a write-up of a GDC 2026 talk, not verified) | https://medium.com/@hmason/the-state-of-ai-native-games-lessons-from-the-frontier-3e696a9e3279 | date not captured | blog | | search only (HTTP 403)
S-D06-060 | AI Roguelite, Steam community thread "Cannot start quests any more" | https://steamcommunity.com/app/1889620/discussions/0/3711558744932916702/?ctp=3 | 2022-12-03 | forum | | fetched
S-D06-061 | Kotaku: Arc Raiders replacing AI-generated voices with human actors | https://kotaku.com/arc-raiders-replaced-ai-generated-content-human-recorded-dialogue-voices-2000678774 | 2026-03-13 | press | | fetched
S-D06-062 | Engadget: Arc Raiders replaced some of its AI-generated voice lines with professional actors | https://www.engadget.com/gaming/arc-raiders-replaced-some-of-its-ai-generated-voice-lines-with-professional-actors-184915627.html | 2026 | press | | search only
S-D06-063 | GameSpot: Arc Raiders now has fewer AI voices as dev re-recorded lines amid controversy | https://www.gamespot.com/articles/arc-raiders-now-has-fewer-ai-voices-as-dev-re-recorded-lines-amid-controversy/1100-6538780/ | 2026 | press | | search only
S-D06-064 | GamingOnLinux: Active Matter developers put up an incredibly distasteful AI notice on Steam | https://www.gamingonlinux.com/2026/09/active-matter-developers-put-up-an-incredibly-distasteful-ai-notice-on-steam/ | 2026-09-11 | press | | fetched
S-D06-065 | Thumb Culture: Active Matter PC review (finds the AI voice jarring when it repeats lines) | https://www.thumbculture.co.uk/active-matter-pc-review | date not captured | press | | search only
S-D06-066 | Engadget (Anna Washenko): around a fifth of Steam Next Fest demos have a generative AI disclosure (reports Eurogamer's count: 1,704 of about 8,700) | https://www.engadget.com/2195840/around-a-fifth-of-steam-next-fest-demos-have-a-generative-ai-disclosure/ | 2026-06-16 | press | via Eurogamer (counts) | fetched
S-D06-067 | AI2U: With You 'Til The End, Steam store page (about 88% positive from about 1,950 reviews) | https://store.steampowered.com/app/2880730/AI2U_With_You_Til_The_End/ | date not captured | other (store page) | | search only
