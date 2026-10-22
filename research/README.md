# Anti-slop checklists

What makes creative and product work read as "AI slop", across ten domains, with evidence. It was built from 19 to 21 Oct 2026 in one research run: three rounds, 133 tells, 573 source records. Each tell is labelled, rated for confidence and dated.

## How to use the checklists

1. **Pick the domains** your work touches from the [domain index](#domain-index). A Steam page touches D01, D04 or D05, D06 and D10. A landing page touches D01, D03, D07 and D08.
2. **Run the `## Checklist`** at the top of each domain file. Each line points to a tell with its evidence, dates and a fix.
3. **Read the label:**
   - **Avoid**: fix it.
   - **Choose deliberately**: fine in itself, but a strong signal when it is the unchosen default. Keep it if you can say why; change it if you can't.
   - **Not a tell**: often blamed on AI, but it's just good practice. Don't "fix" it. See the [combined list](#not-a-tell-combined).
4. **Weigh by confidence:**
   - **Strong** means 3+ independent sources. Act on it.
   - **Moderate** means 2 sources, or 1 with good data. Act on it unless you have a reason not to.
   - **Anecdotal** means one opinion. Treat it as a hint to look closer.
5. **Check the date.** Tells drift: "delve" peaked in 2024, while em dashes and "it's not X, it's Y" peaked in 2025. Each tell has a `Dated:` line.
6. **Look for clusters, not single hits.** One surface feature proves nothing. Three or four from the master list below, in one piece of work, is what readers react to.
7. **Don't use the lists to accuse people.** Human work is regularly flagged as AI (D02-N05, D10-017), and cue flaws don't prove AI authorship (D09-N03). The lists are for checking your own work before release.

## Master list: patterns that recur across domains

These nine patterns cover most of the strong and moderate tells. Each line gives the tells behind it.

### 1. Default left on
The most consistent signal across the research. The problem isn't the tool, it's that nobody chose: the untouched favicon, title, typeface, gradient, card or model look.
- Web UI: D03-002 Inter as an unchosen default (strong), D03-005 default indigo or purple gradient (strong), D03-003 uniform card grid (strong), D03-001 hero badge scaffolding (strong), D03-004, D03-006, D03-009.
- Visible tech: D08-001 favicon (strong), D08-002 title and metadata (strong), D08-003 404 page (strong), D08-005 builder badges (strong), D08-004 social preview.
- Images: D04-012 the model's unprompted aesthetic (strong), D04-001 glossy over-rendered house look (strong), D04-002 yellow cast.
- Brand: D07-001 sparkle icon, D07-002 gradient orb marks.
- **Fix:** list every visible default and make each one a decision. Most fixes take minutes.

### 2. Placeholder or scaffold that ships
Work-in-progress that nobody removed. This is the pattern players and readers punish hardest, because finding it suggests nothing was checked.
- D10-012 shipped AI placeholders found by players (strong); D06-002 generated stand-in assets that ship (strong).
- D08-010 templated README that wasn't checked (strong, among developers); D08-013 leftover template or chatbot text; D08-007 placeholder content on a live page.
- D02-007 chatbot formatting leftovers; D03-013 generator attribution left in the page; D05-013 a decorative sprite sheet with no frame data.
- **Fix:** before release, search every user-facing surface for placeholder strings, "lorem", "[Insert", "Ask if you'd like", template captions and stand-in art.

### 3. Generic specificity: words that name nothing
Copy that sounds specific but could describe any product.
- D01-001 stock transformation verbs; D01-002 placeholder adjectives; D01-004 era and filler openers; D03-011 weightless copy inside the design.
- D02-003 stock AI vocabulary; D07-004 vague "Verb-ing X, Verb-ing Y" taglines; D07-003 the name families LLMs keep suggesting.
- D06-001 the default fantasy name set (strong); D09-009 explanations that never name the misconception.
- **Fix:** every claim names a feature, number, person or limit. If a sentence would fit a competitor's page unchanged, rewrite it.

### 4. Stock rhetorical shapes
Sentence shapes repeated so often that readers recognise them before reading the words.
- D01-003 fragment slogans in threes; D01-005 rhetorical-question hooks; D01-011 contrast reveals and negation lists.
- D02-001 stock hook formulas; D02-002 negative-parallel contrast; D06-003 "Not X, it's Y" in game text.
- Most are labelled Choose deliberately: one used on purpose is fine; the habit is the tell.

### 5. Fake proof
Social proof and trust signals with nothing behind them.
- D01-006 unsourced, round-number social proof; D03-007 fabricated trust furniture; D02-005 fabricated founders and testimonials; D02-004 generic automated replies (strong).
- **Fix:** use real, sourced numbers (D01-N02), or leave them out.

### 6. Looks right at a glance, fails on a closer look
Surface-correct output that breaks when someone zooms in, counts or checks.
- Pixel art: D05-001 a pixel filter over a high-resolution image, D05-003 mixels, D05-004 thousands of colours, D05-005 soft semi-transparent edges (all strong); D05-011 fails at 1x.
- Images: D04-006 garbled text, D04-007 hands, D04-004 plastic skin (all strong); D04-009 small details.
- Quiz items: D09-010 confident factual errors and wrong keys (strong); D09-004 multiple or no correct answers; D09-001 the longest option is the answer; D09-002 cues from stem to key.
- **Fix:** review at 1x, zoomed in and with the answer key hidden. Have a domain expert check every quiz item.

### 7. Inconsistent across a set
Each piece looks fine alone; the set doesn't hold together.
- D04-011 character drift; D05-002 animation frames that change shape; D05-006 outlines; D05-007 lighting; D05-008 tile seams.
- D06-012 runtime AI characters that contradict themselves; D06-008 mixed art style (anecdotal).
- **Fix:** before generating or drawing, lock a style sheet: palette, outline rule, light direction and proportions. Then review the set side by side.

### 8. Too even
Uniform rhythm, detail, tone or difficulty, with no hierarchy and no rough edges.
- D03-010 uniform motion; D03-012 template page rhythm; D04-010 uniform detail with no focal point; D01-014 uniformly upbeat copy with no stated limit.
- D09-007 recall-only items with flat, easy difficulty; D09-014 weak item discrimination; D09-011 repeated templates.
- **Fix:** decide what matters most and let it dominate. State one real limit.

### 9. Undisclosed AI where a platform has rules
Platform policy is the one place where AI use itself, not quality, is the issue.
- Steam: D10-001, D10-002. itch.io: D10-003, D10-004. Kickstarter: D10-005. Apple: D10-006. Google Play: D10-008. Lospec: D10-009. DeviantArt and ArtStation labels: D10-011, D10-018.
- Disclosure itself is not a tell (D10-N03, D02-N01, D06-N04), though one anecdotal source says it lowers trust (D10-016).
- Players are mostly neutral about generative AI in games (D10-N06). The backlash goes to undisclosed or unchecked use (D10-012, D10-019).
- **Fix:** read the platform rule on the day you submit, because the rules change (Apple updated on 16 Oct 2026).

## Not a tell (combined)

Don't avoid any of these because of AI worries. IDs point to the evidence.

**Good craft**
- Generous whitespace (D03-N02).
- Accessible contrast, focus states, reduced motion and responsive layout (D03-N03).
- Plain, sentence-case copy (D03-N09); clean grammar and spelling (D09-N01).
- Concrete detail and lived experience (D02-N02).
- Real, sourced numbers (D01-N02).
- Motion that answers a user action (D03-N07).

**Chosen styles**
- A chosen typeface, Inter included (D03-N01); a chosen brand colour, purple included (D03-N08).
- Dark mode with glow as a house style (D03-N05).
- Three columns, centred heroes and card grids when the content fits them (D03-N04).
- Painterly brushwork and soft light (D04-N01); bokeh (D04-N02); rim light (D04-N03); teal-and-orange grading (D04-N04).
- Deliberate symmetry in emblems and posters (D04-N05); irregular catchlights (D04-N06).
- Pixel art: hand-placed anti-aliasing (D05-N01), bounded dithering (D05-N02), deliberate grid-breaking (D05-N03), a one-pixel or selective outline chosen for the whole set (D05-N04), a large palette in a painterly style (D05-N05).
- Human-designed circle or geometric marks (D07-N03).
- One cohesive art pack (D06-N03).

**Tools and techniques**
- Tailwind and shadcn/ui as a base (D03-N06).
- A framework or a deploy host (D08-N01).
- Procedural generation (D06-N01, D10-N02).
- Simple mechanics and small scope (D06-N02); following a genre formula (D06-N07).
- AI as a drafting tool with human review (D02-N04, D06-N08).
- AI that works behind the scenes, or for development and efficiency (D10-N01, D10-N07); summarising features on Google Play (D10-N05).
- One disclosed AI voice used for a stated reason (D06-N09).
- Seams, gaps and fringes caused by engine settings rather than the art (D05-N06).
- Vite's single-page-app fallback (D08-N06); a favicon.ico file (D08-N07).

**Standard formats**
- A scannable Steam description structure (D01-N01).
- A README with working install steps and the usual sections (D08-N02).
- A few informative badges (D08-N03); standard legal wording (D08-N04).
- Standard quiz option formatting (D09-N02).
- Real app UI in store marketing (D10-N04).

**Single surface features, alone**
- Em dashes in ad copy (D01-N03) or fiction (D06-N05).
- One closing question or a P.S. (D02-N03).
- Emoji in READMEs, an old human habit (D08-N05).
- One uncommon fantasy name (D06-N06).
- Short coined names (D07-N01); -ly, -fy and -me suffixes (D07-N04); .ai for a real AI product (D07-N02).
- A realistic human presenter (D02-N06).

**Disclosure and accusation**
- Clear disclosure of AI use (D02-N01, D06-N04, D10-N03).
- Human work accused of being AI (D02-N05).
- Cue flaws treated as proof of AI authorship (D09-N03).
- Students rating AI-written items as no worse (D09-N04).
- Most players being neutral about generative AI (D10-N06).

## Open gaps

What this run couldn't establish. Treat these tells with more caution.

- **Reddit was unreachable.** Both WebFetch and WebSearch are blocked, so Reddit appears only through articles that quote it (marked `via`). A desktop browser pass is the planned follow-up and could move several anecdotal tells.
- **Most reader reactions come from developers.** Hacker News was the main source of first-hand reaction (D08-010, D05). How general visitors react is largely unmeasured.
- **D01 marketing copy:** no strong tells. There are no word-frequency data for marketing copy and nothing on emoji in store pages. The `unslop` skill already covers general writing tells.
- **D02 social and ads:** evidence on ad creatives is thin and vendor-heavy (MagicPost). TikTok, Harris and Sprout data were seen only in search results.
- **D04 images:** no measured study of the generator default look. D04-001 rests on commentary and is partly tool-specific. Kisser's essay was never read in full.
- **D05 pixel art:** no named pixel artist's complaint and no detection or perception study. D05-012 (fake transparency) rests only on vendors.
- **D06 game design:** 7 of 11 tells are anecdotal. Store-page and trailer tells for games are thin.
- **D07 branding and naming:** no strong tells. The evidence on name families and suffixes is anecdotal, and one suffix tell was retired.
- **D08 visible tech:** no measured sample of live AI-built sites. No visitor reaction to default 404 pages was found (D08-003 rests on the default being common and recognisable).
- **D09 education:** no teacher or student voices in the education press, and few studies of 2025–26 generators. The praise data (D09-008) depend heavily on the domain: low on factual tasks, high on open-ended ones. One widely repeated "31% needed revision" figure could not be traced to its cited paper and was dropped.
- **D10 platforms:**
  - Apple's guidelines (updated 16 Oct 2026) are only partly reconciled with press reports. The 2.5.19 "bait-and-switch" wording is not on the live page.
  - The current Newgrounds and Fur Affinity rules are verified only through 2022 reporting.
  - D10-014 (AI-made ads) is moderate at the minimum.

## Domain index

| Domain | File | Strong | Moderate | Anecdotal | Not a tell | Saturated |
|---|---|---|---|---|---|---|
| D01 Marketing copy | [domains/D01-marketing-copy.md](domains/D01-marketing-copy.md) | 0 | 8 | 6 | 3 | r2 |
| D02 Social posts and ads | [domains/D02-social-ads-marketing.md](domains/D02-social-ads-marketing.md) | 1 | 5 | 7 | 6 | r2 |
| D03 Web UI design | [domains/D03-web-ui-design.md](domains/D03-web-ui-design.md) | 4 | 7 | 2 | 9 | r2 |
| D04 Illustration and image generation | [domains/D04-illustration-image-gen.md](domains/D04-illustration-image-gen.md) | 5 | 4 | 6 | 6 | r3 |
| D05 Pixel and game art | [domains/D05-pixel-game-art.md](domains/D05-pixel-game-art.md) | 5 | 6 | 2 | 6 | r3 |
| D06 Game design | [domains/D06-game-design.md](domains/D06-game-design.md) | 2 | 2 | 7 | 9 | r3 |
| D07 Branding and naming | [domains/D07-branding-naming.md](domains/D07-branding-naming.md) | 0 | 4 | 3 | 4 | r2 |
| D08 Visible tech defaults | [domains/D08-tech-defaults-visible.md](domains/D08-tech-defaults-visible.md) | 5 | 2 | 6 | 7 | r3 |
| D09 Educational content | [domains/D09-educational-content.md](domains/D09-educational-content.md) | 1 | 10 | 4 | 4 | r3 |
| D10 Audience and platform reaction | [domains/D10-audience-platform-reaction.md](domains/D10-audience-platform-reaction.md) | 1 | 12 | 6 | 7 | r3 |
| **Total** | | **24** | **60** | **49** | **61** | |

Other files:
- [sources.md](sources.md): all 573 source records, compiled from the domain files.

## How the evidence was gathered

- **Workflow.** Haiku 5.5 gatherers searched and fetched sources. Sonnet 5.5 mergers deduplicated them and set labels and confidence. The Opus lead reviewed every merge.
- **Spot-checks.** The lead fetched at least two sources per gatherer result itself and corrected several helper errors that way. Each correction was logged in the run log, which is not published.
- **Counting rules.**
  - Vendors copying each other count as one origin; so does press repeating one announcement. A policy page is one origin.
  - A tell supported only by search results, never by a fetched page, stays at moderate or below.
- **Stopping rule.** A domain was saturated once a round added fewer than 3 new or upgraded strong or moderate tells. All ten were saturated by round 3.
- **Quoting.** Rules are paraphrased, with quotes of at most 15 words. Wikipedia's wording is never copied.
