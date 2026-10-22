# D03 web-ui-design

The "vibe-coded" look of AI-built websites and apps: the shared visual and structural defaults of pages made with v0, Lovable, Bolt, shadcn/ui and Tailwind-based prompting, from colour and type through layout, icons, motion and trust furniture. Rounds 1 and 2 are merged. Round 1 (breadth) reduced 28 candidates to 13 tells and 9 not-a-tells; round 2 (depth) added evidence to five existing tells (D03-002, D03-005, D03-006, D03-008, D03-009) and produced no new tells. Most tells here are "choose deliberately": the individual element is fine, and the signal is an unchosen default or several defaults stacked. The one measured source is Adrian Krebs's scoring of 1,590 Show HN submissions with a DOM/CSS pattern check: 22% showed 4+ patterns, 32% showed 2-3, 46% showed 0-1, and his own manual QA puts false positives at roughly 5-10%. His repo README describes a different check (14 pattern files, false positives tested on about 150 labelled sites), so quote his numbers by version. One match is weak evidence; stack signs.

Citation map (round 2): the guide cluster (signs-of-ai-design README, impeccable.style, Sailop, uxskill, solodesign, 925studios) is one citation chain, because the README cites the others and acknowledges prior efforts, so it counts as one source.
None of the cluster cites Krebs, and Krebs cites no guide, so Krebs, the cluster and Anthropic (a vendor prompt, one author across the cookbook and every SKILL.md version) are three separate sources.

## Checklist
- [Choose deliberately · strong] Put a hero badge, eyebrow, section kicker or 01/02/03 marker only where it announces something real or the content is a true sequence. (D03-001)
- [Choose deliberately · strong] Choose the typeface for the subject; keep Inter only with a reason, and treat its popular replacements the same way. (D03-002)
- [Choose deliberately · strong] Size feature cards and tiles by content: use the item count you have, vary sizes, and change the shadcn tokens (radius, shadow, colour). (D03-003)
- [Choose deliberately · strong] Pick hues from the brand, not Tailwind's default indigo; use a gradient (hero, CTA, headline text) only if it does a job. (D03-005)
- [Choose deliberately · moderate] Build the palette and headline style from the brief, not from the cream, terracotta, italic-serif accent-word "tasteful" look. (D03-004)
- [Choose deliberately · moderate] Use glow, orbs and glass only where there is a real light source or layering problem, and keep body text contrast high on dark themes. (D03-006)
- [Avoid · moderate] Show only testimonials, logos, user counts and badges you can verify; otherwise cut the section. (D03-007)
- [Avoid · moderate] Use a coloured card edge only to mark a state, and remove nested cards and ghost-card shadows. (D03-008)
- [Choose deliberately · moderate] Choose icons for the content; do not default to the usual Lucide five, an arrow on every CTA, or emoji as icons. (D03-009)
- [Choose deliberately · moderate] Use one deliberate motion moment, not the same fade-up on every section and a hover on every card. (D03-010)
- [Avoid · moderate] Write copy that could only describe this product; cut buzzword headlines and formula closers. (D03-011)

## Tells

### D03-001 Hero badge, eyebrow and numbered kicker scaffolding
- Label: Choose deliberately
- Confidence: strong (3: Krebs measured pattern check, Anthropic SKILL.md, the 2026 guide cluster counted as one)
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: Generators add a "New" pill above the centred headline, a tracked-out all-caps label above every section heading, and 01/02/03 markers whether or not there is anything to announce or any real sequence. The ornament is applied by template, not by need.
- Fix: Keep the pill only when it announces a real change and links to it; drop repeated kickers that echo the heading; number only genuine steps or timelines; use caps and monospace only for code or data labels (developer-tool brands can keep them).
- Fixable: yes by prompting/editing
- Sources: S-D03-002, S-D03-001, S-D03-003, S-D03-007
- Flag: Round 2 found only an anecdotal HN comment on this (S-D03-026, "superfluous numbers"), not counted. The current SKILL.md version is S-D03-001; check which version supports which facet before citing it.

### D03-002 Unchosen default typeface (Inter)
- Label: Choose deliberately
- Confidence: strong (4: Krebs, Anthropic counted as one across cookbook and SKILL.md, guide cluster counted as one, Pimp my Type essay)
- Dated: noted from 2024, still cited in 2026. Anthropic named Inter in the Oct 2025 cookbook and the Dec 2025 SKILL.md, but the Jun 2026 and Sep 2026 SKILL.md versions do not (one source, however many versions). Web Almanac 2025 (primary data) calls Inter a notable climber at about 1.4-1.5% of pages. Pimp my Type, May 2026.
- Why it reads as AI: Inter is the default of the shadcn and Tailwind stack and is adopted through frameworks, so a page that never chose a face looks like every other generated page, especially with Inter on every centred hero headline. It is not the most-used webfont: the Web Almanac puts it on about 1.4-1.5% of pages, behind Roboto, Font Awesome, Poppins, Open Sans and Montserrat. That low overall share makes Inter left on default a stronger signal, not a weaker one. The typeface is good; the signal is that nobody picked it. Its popular replacements have the same problem (see D03-004).
- Fix: Pick a face for the subject and give it a considered scale and weight; if Inter stays, keep it knowingly.
- Fixable: yes by prompting/editing (swap the font, change the scale)
- Sources: S-D03-002, S-D03-001, S-D03-005, S-D03-003, S-D03-018, S-D03-019, S-D03-022, S-D03-023
- Flag: Sailop's claim "Inter is the most-used webfont on the indexed web" (S-D03-005) is wrong against the Web Almanac chapter (S-D03-022) and contradicts Sailop's own Almanac paraphrase on the same page; it is removed here. Defenders of Inter's quality are search-only (see D03-N01). Sailop's claim that shadcn defaults to Inter was not checked. The Web Almanac chapter was read only to its first 100,000 characters. Pimp my Type's only outside source is a podcast it links but the gatherer did not open.

### D03-003 Uniform card grid (the triptych, equal-tile bento, untouched shadcn card)
- Label: Choose deliberately
- Confidence: strong (3: Krebs, Anthropic SKILL.md, guide cluster counted as one; see flag on which facets Krebs covers) Lead review 20 Oct (r2): strong holds for the untouched shadcn and card-grid facets. The bento and triptych layout facets rest on the guide cluster alone (Krebs's checker has no file for them), so treat those facets as moderate.
- Dated: noted from 2024, still cited in 2026
- Why it reads as AI: Exactly three identical cards with an icon on top, or a bento grid of equal-sized tiles, forces content into a template and gives the layout no hierarchy. Using the shadcn card with one large radius and the default shadow, unchanged, adds to the effect: no token was touched. In Krebs's earlier 500-post run, 23.5% of sites used shadcn with no customisation (via GIGAZINE), so most shadcn sites did change it.
- Fix: Use the number of items the content has; size tiles by priority; vary radius and shadow by hierarchy; change theme tokens rather than dropping shadcn.
- Fixable: yes by prompting/editing (token changes, layout edit)
- Sources: S-D03-002, S-D03-001, S-D03-005, S-D03-003, S-D03-029
- Flag: The bento facet rests on the signs README alone among fetched sources; other bento criticism is search-only listicles (Brainy.ink, Setproduct, Succo Design, Syed Aoun Raza), and some sources still promote bento when tile size follows content priority. Krebs's checker repo has no bento or triptych check among its 14 pattern files (S-D03-024), so his support likely covers the shadcn and card facets, not the layout facets; the lead may want to drop strong to moderate for the layout facets. The 23.5% figure is second-hand through GIGAZINE (S-D03-029, derivative of Krebs, adds no independence). The round-1 search snippet figure of 4.3% for unmodified shadcn was wrong.

### D03-004 Second-wave "tasteful" defaults (cream and terracotta palette, italic-serif accent word, Geist/Space Grotesk/Instrument Serif)
- Label: Choose deliberately
- Confidence: moderate (lead review 20 Oct: Krebs covers only the accent-word facet; the palette and new-fonts facets rest on 2 sources, Anthropic SKILL.md and the guide cluster counted as one)
- Dated: noted from 2025, still cited in 2026; the Sep 2026 SKILL.md still lists a "terracotta or warm-clay accent" as a generic default (same vendor as before, no new author)
- Why it reads as AI: After purple and Inter became jokes, a second look became the reflex: a warm cream background with a terracotta or amber accent, a serif display face, one headline word set in italic or a contrasting colour, and newer "safe" faces. It reads as tasteful but is as unchosen as the first wave; Sailop says Geist stayed fresh for only about eight months.
- Fix: Name four to six colours and give each a role from the subject; set the headline in one treatment; use an accent word only where the meaning needs the emphasis; check how often a face recurs in generated pages before choosing it.
- Fixable: yes by prompting/editing
- Sources: S-D03-001, S-D03-002, S-D03-003, S-D03-007, S-D03-005
- Flag: Serif and warm neutrals are legitimate for editorial, food and craft brands (see D03-N01); Anthropic's own skill says these traits suit some briefs. Round 2 found no new independent evidence, so the lead review note stands.

### D03-005 Default indigo/purple gradient (hero, CTA, headline text)
- Label: Choose deliberately
- Confidence: strong (3: Krebs measured pattern check, Anthropic counted as one across cookbook and SKILL.md, guide cluster counted as one; lead review: judgement call, see flag). Tailwind's docs show where the hue comes from but are not counted as a source that it reads as AI. Lead review 20 Oct (r2): strong accepted. Krebs (measured), Anthropic (any version) and the guide cluster are three separate origins. A low overall indigo share on the web makes the default stand out more, not less.
- Dated: noted from about 2024 ("the canonical UI tell of 2024" per the signs README), still cited in 2026; the signs README says it is already being replaced by the cream palette (D03-004). Origin chain: Tailwind v1 palette (2019) has indigo-500 as #667eea; the #6366f1 hex the tell literature quotes is the v2 value (v2 released 18 Nov 2020; v2 docs show indigo-500 as #6366F1, fetched by the lead; v3 docs agree). Anthropic's cookbook (21 Oct 2025) and the Dec 2025 SKILL.md name purple gradients on white backgrounds; the Jun 2026 and Sep 2026 SKILL.md versions do not (one source, however many versions). Adam Wathan's X post apologising for the Tailwind UI buttons is dated 7 Aug 2025 but second-hand (see flag).
- Why it reads as AI: A gradient from Tailwind's default indigo/violet/purple on the hero, buttons and CTAs, or clipped into headline text, is what generators emit when no colour is specified. Tailwind's palette supplies the hues, and Anthropic's own prompt lists purple gradients as a default to avoid, so the vendor recognises the habit. Gradient fill on headings or big numbers is decorative and usually carries no meaning.
- Fix: Choose hues from the brand with a reason for each; a purple that was chosen is fine. Use a solid colour for headings, and if a gradient is kept, use it on one meaningful element with a solid fallback.
- Fixable: yes by prompting/editing
- Sources: S-D03-002, S-D03-003, S-D03-006, S-D03-005, S-D03-008, S-D03-018, S-D03-019, S-D03-014, S-D03-015, S-D03-016, S-D03-017, S-D03-020, S-D03-021, S-D03-029
- Flag: Upgraded from moderate to strong by the count rule (Krebs, Anthropic, cluster); the lead should confirm, because the Anthropic wording was removed from the two latest SKILL.md versions and the prevalence data runs against the claim. Counter-data: Sailop, citing the HTTP Archive Web Almanac 2025 (second-hand; the Almanac CSS chapter was not fetched), puts indigo-500 on only 0.54% of pages and says the rise tracks Tailwind's growth, not AI choice. The lead's earlier question on Sailop's "purple gradients" wording is settled: it matches the Oct 2025 cookbook and Dec 2025 SKILL.md, which Sailop does not link. The Wathan "formally apologize" quote is second-hand (925studios and a search snippet; the X post returned HTTP 402), and it points at the paid Tailwind UI kit, so the route is copy-paste from a kit, not the framework default. The README's claim that Tailwind shipped indigo as its demo accent in 2019 is in no Tailwind doc read. Krebs's gradient share: the 500-post run had 28% with a gradient (via GIGAZINE, S-D03-029, derivative of Krebs); the 1,590-site post reports no gradient share, and the round-1 figure of 4.3% was wrong. The gradient-text rule (S-D03-008) is search only. Krebs's checker has gradients.js (S-D03-024), thresholds not read. The Tailwind v2 docs page is search-only in the gatherer's file; the lead fetched it.

### D03-006 Glow, orbs, glass and neon-on-dark atmosphere
- Label: Choose deliberately
- Confidence: moderate (2: Krebs, guide cluster counted as one; the contrast facet also has an anecdotal HN comment, not counted)
- Dated: noted from 2025, still cited in 2026; contrast comment 23 Apr 2026
- Why it reads as AI: Blurred gradient orbs behind the hero, coloured box-shadow glows, frosted backdrop-blur cards on every surface and a perma-dark theme with neon accents are decoration with no content function. The dark house style also often pairs with medium-grey body text that fails contrast, which is a real accessibility fault.
- Fix: Cut the orbs, or let light come from the content (product image, data highlight); use glass only where content sits over imagery or a real layer; keep dark mode if the product suits it with one restrained accent, and raise body text contrast to meet WCAG.
- Fixable: yes by prompting/editing
- Sources: S-D03-002, S-D03-004, S-D03-003, S-D03-027, S-D03-031
- Flag: Krebs's own verdict is "not really bad, just uninspired"; Linear and Raycast built the dark-glow look by hand before generators existed (see D03-N05). Glass and orbs also appear in some human agency work, so the orb signals the AI-company branding trend as much as machine authorship. Round 2 found no fetched independent evidence for the glow and glass facets: the HN commenter (S-D03-027) says most dark-mode sites are done badly, which supports only the contrast facet. UIDesignPrompts, BSWEN (HTTP 403) and LogRocket are search only and not cited. NN/G's glassmorphism article (S-D03-031, search only) treats glass as a legitimate layering tool.

### D03-007 Fabricated social proof and trust furniture
- Label: Avoid
- Confidence: moderate (2: Krebs for the stat-banner layout, guide cluster counted as one for the fabrication claims)
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: Testimonial walls of first-name-only people with generated headshots and no specifics, grey logo bars for customers who may not exist, round-number stat banners, and compliance badges or "audited" claims for audits that never happened. The trust section appears because the median page has one, whether or not the facts exist.
- Fix: Show only testimonials you can attribute with a use case, logos you may display, and numbers you can check; never use a generated face to imply a real customer; otherwise cut the section.
- Fixable: partly (layout can be edited; invented trust cannot be fixed by design)
- Sources: S-D03-003, S-D03-005, S-D03-002
- Flag: Krebs lists stat banner rows as a layout pattern only, not as fabricated; the fabrication claims rest on the guide cluster. A logo bar of real customers is standard human practice. The FTC fake-review rule and Baymard trust research were only seen in search summaries and are not cited. Round 2 fetched nothing new here.

### D03-008 Decorative card chrome (coloured edge stripe, cards inside cards, ghost cards)
- Label: Avoid
- Confidence: moderate (2: Krebs, guide cluster counted as one; two HN comments are anecdotal and not counted)
- Dated: noted from 2025, still cited in 2026; Krebs 20 Apr 2026, HN comments 23 Apr 2026
- Why it reads as AI: A 3-4px coloured left or top border sprayed on ordinary cards (copied from alert components), boxes nested inside boxes, and a hairline border plus wide diffuse shadow on the same card make a layout look organised without making hierarchy decisions.
- Fix: Use the stripe only to mark a state (error, warning, selected); remove one layer of containment per block and group with spacing and type; pick one edge treatment.
- Fixable: yes by prompting/editing
- Sources: S-D03-002, S-D03-004, S-D03-003, S-D03-024, S-D03-025, S-D03-026
- Flag: Krebs's checker repo lists accent-stripe.js among its pattern files, but the file body was not opened, so its thresholds are unknown and it is not confirmed to target this exact pattern; no prevalence figure is published. The blog's coloured-border point is still a designer's remark he relays. One HN commenter says people used coloured borders for years before generators, so the stripe is also a human habit; another says AI sites "add coloured left borders, tags and superfluous numbers" (anecdotal). The stripe is correct on real alerts; the Avoid label covers decorative use only.

### D03-009 Stock icon vocabulary (the usual Lucide five, arrow on every CTA, emoji and sparkle as icons)
- Label: Choose deliberately
- Confidence: moderate (2: Anthropic SKILL.md for the appended arrow, guide cluster counted as one for the rest; the NN/G sparkle study is a third voice but shows the sparkle is not read as AI, so it narrows the claim)
- Dated: noted from 2024, still cited in 2026; NN/G study 20 Sep 2024, before the 2026 guides
- Why it reads as AI: The same few Lucide picks recur (Sparkles for AI, Zap for fast, Shield for secure, Check, BarChart3), an arrow gets appended to every link and button, and emoji stand in for designed icons. The icon choice follows the library default, so the set becomes a signature. In NN/G's study (n=107) no respondent read the sparkle as artificial intelligence; they read it as favourite, effects or special. The sparkle therefore marks an AI feature by designer convention, not machine authorship.
- Fix: Choose icons for the content or a set with its own silhouette; use arrows only to show direction; label AI features in words or use the sparkle as part of a consistent label system; keep emoji only where the brand voice uses them. Do not count a sparkle as evidence a page was machine-made.
- Fixable: yes by prompting/editing
- Sources: S-D03-001, S-D03-005, S-D03-003, S-D03-009, S-D03-010, S-D03-011, S-D03-030
- Flag: The emoji facet rests on the signs README and search-only sources (S-D03-009, S-D03-010; titles not re-checked). S-D03-011 (NN/G) is now fetched. The README cites NN/G, so NN/G is a source the cluster uses, not a copy of it. Smashing Magazine (S-D03-030) is search only. The sparkle is a shared convention across AI products, so it signals "AI feature", not AI authorship. Lucide itself is a good set.

### D03-010 Uniform motion (same scroll-reveal everywhere, hover on every card, bounce easing)
- Label: Choose deliberately
- Confidence: moderate (2: Anthropic SKILL.md, guide cluster counted as one)
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: The same fade-and-slide-up entrance on every section, a hover transition on every card and springy easing on dialogs are the animation-library defaults applied everywhere, with no single moment of emphasis.
- Fix: Orchestrate one entrance moment, animate only where motion shows the effect of an action, and use standard easing; respect reduced motion.
- Fixable: yes by prompting/editing
- Sources: S-D03-001, S-D03-003
- Flag: The signs README itself rates the fade-in "weak alone"; real teams use it constantly. Motion that answers a user action is fine (D03-N07). Round 2 fetched nothing new here.

### D03-011 Weightless marketing copy inside the design
- Label: Avoid
- Confidence: moderate (2: Anthropic SKILL.md, guide cluster counted as one)
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: Headlines such as "Transform how you work", a buzzword layer ("seamless", "robust", "empower"), and a formula closer at the end of each section could describe any product, and copy this generic makes a page feel as templated as the layout does.
- Fix: Write specific copy in the customer's words that could only describe this product; use plain verbs and sentence case.
- Fixable: yes by prompting/editing (copy edit)
- Sources: S-D03-001, S-D03-003, S-D03-005, S-D03-007
- Flag: Label is the lead's call. The signs README says density, not occurrence, is the signal, and good human writers use every one of these devices. Copy is partly outside the visual domain. Round 2 fetched nothing new here.

### D03-012 Template page order and flat spacing rhythm
- Label: Choose deliberately
- Confidence: anecdotal (guide cluster only, counted as one: signs README, Sailop, uxskill)
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: The same section sequence (hero, logos, three features, testimonials, stats, pricing, FAQ, footer) with identical padding between every section, so nothing is compressed or given room for emphasis. Sailop's composite page even ends on a "Built with care" footer.
- Fix: Derive the section order from the reader's question, cut sections that do not earn their place, and vary spacing to group related blocks and give key sections room.
- Fixable: yes by prompting/editing
- Sources: S-D03-003, S-D03-005, S-D03-006
- Flag: Three guide pieces, now confirmed as one citation chain (the README cites Sailop and others), so one source. The signs README itself says this is also the standard human landing-page playbook and the signal comes from zero deviation plus other fingerprints. Krebs's checker has a faq-accordion.js file, but a file name shows a checker exists, not that an FAQ accordion reads as AI, so it is not used.

### D03-013 Generator attribution left in the page
- Label: Avoid
- Confidence: anecdotal (guide cluster only: signs README, Sailop)
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: A "Built with v0", "Built on Lovable" or "Made in Bolt" line or floating badge is near-conclusive and the easiest tell to check.
- Fix: Remove it where the plan allows; where the free tier imposes it, upgrade or accept it knowingly.
- Fixable: yes by prompting/editing (where the plan permits removal)
- Sources: S-D03-003, S-D03-005
- Flag: Platform-imposed on some free plans, so it is a weaker signal of the author's choices than footer text the author wrote.

## Not a tell

### D03-N01 A chosen typeface, whether Inter, another sans, or an expressive serif for an editorial or craft brand
- Why it is fine: The tell is the unchosen default, not the font. Inter's quality is accepted even by its critics (the Web Almanac calls it highly regarded), and serif or expressive display type is legitimate when the brand calls for it.
- Sources: S-D03-003, S-D03-001, S-D03-007, S-D03-012, S-D03-013, S-D03-022

### D03-N02 Generous whitespace and clean spacing
- Why it is fine: Whitespace is the quality floor; the tell is one spacing value with no rhythm (D03-012).
- Sources: S-D03-003, S-D03-001

### D03-N03 Accessible contrast, visible focus, reduced motion and responsive layout
- Why it is fine: These are the quality floor. Generator-default sites are often technically clean, accessible and fast. Low-contrast grey body text is a different fault (D03-006).
- Sources: S-D03-001, S-D03-005

### D03-N04 Three-column layouts, centred heroes and card grids when the content fits
- Why it is fine: Humans also default to a clean, responsive layout, and the centred hero is an effective conversion layout. The fault is forcing content into the structure with no deviation (D03-003); the fix is variation, not avoidance.
- Sources: S-D03-003, S-D03-005

### D03-N05 Dark mode with glow as a deliberate house style
- Why it is fine: Linear, Raycast and others built it by hand years before generators. Krebs's verdict: "Not really, just uninspired."
- Sources: S-D03-003, S-D03-002

### D03-N06 Tailwind and shadcn/ui as a base
- Why it is fine: Sailop says slop is not a Tailwind, shadcn or generator problem; it comes from accepting defaults. The same tools in the hands of people who push back are not distinguishable from hand-built work. Tuning the tokens is the fix (D03-003). In Krebs's earlier 500-post run, only 23.5% of sites used shadcn without customisation (via GIGAZINE, second-hand), and one HN commenter said they would not use shadcn as an AI barometer.
- Sources: S-D03-005, S-D03-029, S-D03-028

### D03-N07 Motion that answers a user action
- Why it is fine: Opening, expanding or confirming with motion shows what changed. Uniform scroll-reveal is the tell (D03-010). Anthropic's cookbook says to use animations for effects and micro-interactions.
- Sources: S-D03-001, S-D03-018

### D03-N08 A brand colour that was chosen, including purple
- Why it is fine: The README calls purple a legitimate brand colour; the tell is the unchosen default hue in a gradient (D03-005).
- Sources: S-D03-003

### D03-N09 Plain, sentence-case copy
- Why it is fine: Sentence case and plain verbs are recommended copy style; Title Case on everything is the weak signal.
- Sources: S-D03-001, S-D03-003

## Sources
S-D03-001 | Anthropic frontend-design SKILL.md (current main; the Sep 2026 version names neither Inter nor purple gradients) | https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md | undated (read as on main 2026-10-20) | policy | | fetched
S-D03-002 | Adrian Krebs, Scoring Show HN submissions for AI design patterns (blog says 16 patterns and 1,590 sites, false positives "maybe 5-10%" from manual QA; his repo README says 14 patterns and about 150 labelled sites for the false-positive check, and the repo has 14 pattern files; quote numbers by version) | https://www.adriankrebs.ch/blog/design-slop/ | 2026-04-20 | blog | | fetched
S-D03-003 | febbhav, Signs of AI design (README) | https://github.com/febbhav/signs-of-ai-design | commits 2026-07-22 to 2026-07-31 | guide | | fetched
S-D03-004 | impeccable.style slop catalogue | https://impeccable.style/slop/ | 2026 (no exact date; cannot be placed relative to Krebs) | guide | | fetched (excerpt)
S-D03-005 | Sailop, AI Slop in 2026: A Field Guide to the AI-Generated Web | https://www.sailop.com/blog/ai-slop-2026-state-of-the-ai-generated-web | 2026-04-28 (updated 2026-10-18) | guide | Web Almanac 2025 figures second-hand; only the figures the current version sources are used; its "most-used webfont" claim is wrong (see D03-002); names Anthropic's frontend prompt without a link; an earlier teardown of 47 sites was withdrawn | fetched
S-D03-006 | uxskill, Why v0, Bolt, and Lovable all ship the same look | https://uxskill.laithjunaidy.com/blog/ai-app-builders-generic-design.html | 2026-05-29 | blog | | fetched
S-D03-007 | solodesign, AI design slop: the tells, and how I built a tool to catch them | https://solodesign.cc/blog/ai-design-slop-the-tells/ | 2026-06-06 | blog | | fetched
S-D03-008 | stopslop issue 87 (rule SLOP052, gradient text) | https://github.com/mgiovani/stopslop/issues/87 | undated | forum | | search only
S-D03-009 | Sikora Software, AI website design tells | sikora.software/blog/ai-website-design | undated | blog | | search only
S-D03-010 | Google Design, AI sparkle icon research | https://design.google/library/ai-sparkle-icon-research-pozos-schmidt | undated | study | | search only (title not re-checked)
S-D03-011 | Kate Kaplan, The Proliferation and Problem of the Sparkles Icon (NN/G; quantitative study, n=107) | https://www.nngroup.com/articles/ai-sparkles-icon-problem/ | 2024-09-20 | study | | fetched
S-D03-012 | Matt Westcott, An ode to the Inter typeface | https://mattwestcott.org/blog/an-ode-to-the-inter-typeface | undated | blog | | search only
S-D03-013 | HN comment thread on Inter at small sizes | https://news.ycombinator.com/item?id=28009663 | c. 2021 (date from search result, not checked) | forum | | search only
S-D03-014 | Tailwind CSS v1 docs, Background Color (indigo-500 is #667eea) | https://v1.tailwindcss.com/docs/background-color | 2019 release | policy | | fetched
S-D03-015 | Adam Wathan, Tailwind CSS v2.0 release post | https://tailwindcss.com/blog/tailwindcss-v2 | 2020-11-18 | blog | | fetched
S-D03-016 | Tailwind CSS v2 docs, Customizing Colors (indigo-500 is #6366F1) | https://v2.tailwindcss.com/docs/customizing-colors | undated | policy | | fetched by the lead (search only in the gatherer file)
S-D03-017 | Tailwind CSS v3 docs, Customizing Colors (indigo-500 is #6366f1) | https://v3.tailwindcss.com/docs/customizing-colors | undated (footer 2025) | policy | | fetched
S-D03-018 | Anthropic, claude-cookbooks, prompting_for_frontend_aesthetics.ipynb (first commit; names Inter and purple gradients; current file has the same lines) | https://raw.githubusercontent.com/anthropics/claude-cookbooks/ec30522b67e58b6ea54e0a3bf63a65c5180a144b/coding/prompting_for_frontend_aesthetics.ipynb | 2025-10-21 | policy | | fetched
S-D03-019 | Anthropic frontend-design SKILL.md version history (4 Dec 2025 version names Inter and purple gradients; 9 Jun 2026 and 3 Sep 2026 versions name neither; same author as S-D03-001 and S-D03-018) | https://github.com/anthropics/skills/commits/main/skills/frontend-design/SKILL.md | 2025-12-04, 2026-06-09, 2026-09-03 | policy | | fetched (three commits)
S-D03-020 | Adam Wathan, X post apologising for the Tailwind UI buttons | https://x.com/adamwathan/status/1953510802159219096 | 2025-08-07 | forum | wording from a search result and quoted in 925studios | search only (fetch returned HTTP 402)
S-D03-021 | 925studios, AI slop design tells | https://www.925studios.co/blog/ai-slop-design-tells | 2026-06-14 | guide | quotes the Wathan apology without a link; cited by the signs README | fetched (text)
S-D03-022 | HTTP Archive, Web Almanac 2025, Fonts chapter | https://almanac.httparchive.org/en/2025/fonts | 2025 edition (published 2026-01-15 per Sailop) | study | | fetched (first 100,000 characters)
S-D03-023 | Oliver Schöndorfer, Pimp my Type, about AI design | https://pimpmytype.com/about-ai-design/ | 2026-05-06 (updated 2026-05-07) | blog | | fetched
S-D03-024 | Adrian Krebs, design-slop-cop checker repository, src/patterns file listing (accent-stripe.js, gradients.js, faq-accordion.js; no bento or triptych file) | https://github.com/AdrianKrebs/design-slop-cop/tree/main/src/patterns | undated | study | | fetched (listing only; file bodies not opened)
S-D03-025 | Hacker News comment ("I've been using colored borders as design for ages") | https://news.ycombinator.com/item?id=47875417 | 2026-04-23 | forum | | fetched (Algolia API)
S-D03-026 | Hacker News comment (coloured left borders, tags and superfluous numbers) | https://news.ycombinator.com/item?id=47872336 | 2026-04-23 | forum | | fetched (Algolia API)
S-D03-027 | Hacker News comment (dark-mode sites done badly) | https://news.ycombinator.com/item?id=47873197 | 2026-04-23 | forum | | fetched (Algolia API)
S-D03-028 | Hacker News comment ("I wouldn't use that as an AI barometer") | https://news.ycombinator.com/item?id=47871458 | 2026-04-23 | forum | | fetched (Algolia API)
S-D03-029 | GIGAZINE, article on Krebs's design-slop work (28% gradient and 23.5% unmodified shadcn, both from an earlier 500-post run) | https://gigazine.net/gsc_news/en/20260423-design-slop/ | 2026-04-23 | press | derivative of Krebs; credits his blog under an earlier title | fetched
S-D03-030 | Smashing Magazine, New EU Guidelines For AI Labelling | https://www.smashingmagazine.com/2026/08/eu-guidelines-ai-labelling/ | 2026-08 | press | | search only
S-D03-031 | NN/G, glassmorphism best practices | https://www.nngroup.com/articles/glassmorphism/ | undated | study | | search only
