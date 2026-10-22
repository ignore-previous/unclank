# D01 marketing-copy

Landing pages, hero lines, feature blurbs, Steam/itch/app-store descriptions, launch emails and README-as-marketing. Rounds 1 and 2 are merged (round 1 breadth, round 2 depth). Evidence is mostly practitioner lists and vendor samples. No measured study of AI-written marketing text was found. One tell (D01-006) is rated strong on source count, helped by an agency conversion study that measures reader response, not AI authorship. The word-frequency studies (Kobak et al., Juzek and Ward, Geng et al.) measure academic abstracts and were not used to raise any confidence here. Word lists of the "AI words to avoid" kind tend to copy each other, so they are counted as one cluster. Tells that extend an existing `unslop` rule say so in their record.

## Checklist
- [Avoid · moderate] Give every social-proof figure a real count and source, or a named customer; drop round numbers you cannot back ("Trusted by 10,000+", "Join thousands"). (D01-006)
- [Avoid · moderate] Replace placeholder adjectives (seamless, robust, effortless, all-in-one, game-changer, "few clicks") with the feature, step count or time they stand in for. (D01-002)
- [Avoid · moderate] Replace stock transformation verbs (unlock, unleash, supercharge, elevate, empower, revolutionize, reimagine) with the named outcome and a number. (D01-001)
- [Avoid · moderate] Open with the audience or problem, not an era or filler opener ("In today's fast-paced world", "When it comes to", "Here's the thing"). (D01-004)
- [Choose deliberately · moderate] Use one fragment or three-beat slogan per section at most ("Fast. Simple. Effective."), and make the third beat specific. (D01-003)
- [Choose deliberately · moderate] Use a contrast reveal ("It's not X, it's Y") or a negation list ("No X. No Y. Just Z.") once per page at most, with both halves factual. (D01-011)
- [Avoid · moderate] Open launch emails with what launched, who it helps and the date or price, not "We're excited to announce" or "Say goodbye to X"; use at most one exclamation point. (D01-007)
- [Choose deliberately · moderate] Use a question hook ("Tired of X?", "The result?") only when the answer that follows is specific; never stack them, and keep FAQ questions as they are. (D01-005)

## Tells

### D01-001 Stock transformation verbs
- Label: Avoid
- Confidence: moderate (2 independent: the practitioner-list cluster counted as one, plus Stockton's separate fetched list; vendor pages also use the words in their own copy)
- Dated: noted from 2025-2026 lists (Stockton 7 Jul 2025; further lists Jul to Oct 2026); one 2026 blog says "unlock" was fine until 2024 and is now a giveaway; still cited in 2026
- Why it reads as AI: These verbs fill the verb slot of a hero line with a generic promise of change and never say what changes. They fit any product, so the line carries no information.
- Fix: Name the outcome and a number ("Cut the export step from 6 clicks to 1"). If there is no outcome to name, delete the verb and state the feature.
- Example done well: none in the raw file
- Sources: S-D01-001, S-D01-002, S-D01-003, S-D01-004, S-D01-005, S-D01-035, S-D01-037, S-D01-038, S-D01-039
- Flag: Sources are opinion lists that probably copy each other (the cluster counts as one); the vendor page shows AI-copy tools use the words but is not shown to be AI-written. Stockton (S-D01-035) is a personal list with no data and no outside list cited; the lead fetched it and confirmed it names these verbs. No measured marketing data. Kobak et al.'s academic excess-word lists do not show these verbs in their top common set, and are not used here. "Unlock" has long been ordinary human ad copy. S-D01-037 to S-D01-039 were seen as search snippets only and are not counted separately. Confidence drops to anecdotal if the lead does not count the vendor usage and treats Stockton as part of the cluster.

### D01-002 Placeholder adjectives that name no feature
- Label: Avoid
- Confidence: moderate (2 independent: the fetched marketingskills guide and Stockton's fetched list; the blog and template posts add reach but their independence is not shown; borderline strong if the lead counts Olivia Cal as independent)
- Dated: practitioner lists from 2025-2026 (Stockton 7 Jul 2025); guide file undated
- Why it reads as AI: Each word is true of almost any product, so it stands in for a missing feature description. The copy looks finished but says nothing a reader can check.
- Fix: Give the step count, time or feature. "Effortless" becomes "Import in one click, no account." "Game-changer" becomes what changes, for whom, by how much.
- Sources: S-D01-001, S-D01-006, S-D01-007, S-D01-008, S-D01-035, S-D01-037
- Flag: Tiwari's post and the Metaflow template may both descend from the same "stop slop" skill idea, so independence is not shown. Olivia Cal, Tiwari, Metaflow and FeedHive seen as search snippets only. Stockton's reasoning is that these words are clichés shared across brands; he also bans "robust" outright, stricter than this record needs. No source defends these words; the objection is vagueness, not the word. "Seamless" could be fine when tied to a measurable fact, but no source says so.

### D01-003 Fragment slogans in threes
- Label: Choose deliberately
- Confidence: moderate (six sources, but independence is not shown and two are general AI-tell lists, so counted conservatively)
- Dated: "snappy triads" named about Oct 2025; still cited in 2026
- Why it reads as AI: The marketing form of the rule of three stacks near-synonyms of equal length ("Fast. Simple. Effective."). Used as the default in every section, no item gets emphasis.
- Fix: Use as many items as the facts support, often one or two. If three, make the third specific and not a predictable continuation. At most one per section.
- Extends unslop: item 10 (rule of three). Kept because the fragment-slogan form and the per-section cap come from marketing sources.
- Sources: S-D01-001, S-D01-009, S-D01-010, S-D01-011, S-D01-012, S-D01-014
- Flag: Counter-evidence: a Wikipedia article on the rule of three says ad slogans use three-part form deliberately and well (S-D01-022, snippet only). A single slogan is good copy; the default across a page is the tell. The Wikipedia AI guide's rule-of-three entry was only a heading in the fetched text, so its weight is unverified (round 2 re-read part of that page but added nothing for this tell). Most sources search only.

### D01-004 Era and filler openers
- Label: Avoid
- Confidence: moderate (2 sources name the era openers; "When it comes to" and "Here's the thing" rest on one guide)
- Dated: era openers named about Oct 2025; guide undated
- Why it reads as AI: These are template openers that can start any product page. They spend the first line on nothing and delay the claim.
- Fix: Put the audience or the problem in the first sentence.
- Sources: S-D01-001, S-D01-009
- Flag: Guo's list is general AI slop, not marketing-specific. No frequency data for any opener in marketing copy. Round 2 found no new independent source (a further list is a copy of the marketingskills file).

### D01-005 Rhetorical-question hooks
- Label: Choose deliberately
- Confidence: moderate (the guide, Stockton's fetched list and three general AI-tell articles; the Forbes piece repeats a marketing influencer's post; the general articles are search only, so not counted as independent; borderline strong)
- Dated: cited June 2025 (Forbes), 7 Jul 2025 (Stockton), Feb 2026 (Cherryleaf), 2026 (Aborn)
- Why it reads as AI: A question posed and then answered ("The result?", "The goal?", "Tired of X?") manufactures a hook, and the answer is the claim the question was built to deliver.
- Fix: State the claim as the first sentence. Keep questions in FAQs, where they are natural.
- Sources: S-D01-001, S-D01-013, S-D01-014, S-D01-035, S-D01-040
- Flag: Label unsure. Raw suggested Avoid, but rhetorical questions are an old human ad device and only default use is cited, which fits Choose deliberately. Forbes, Cherryleaf and Aborn are general AI-writing articles, all search only; Aborn herself warns that treating such patterns as proof is misleading and that detectors misflag human writing. Stockton's list is a personal word list with no frequency data on product pages. No measured data.

### D01-006 Unsourced and round-number social proof
- Label: Avoid
- Confidence: moderate (lead review 20 Oct: kept at moderate rather than the merger's strong. Of the three sources, one is an unchecked forum claim, one a search snippet, and the Digital Applied study is a CRO vendor measuring conversion, not AI authorship.)
- Dated: HN thread about AI-built landing pages, approx. late July 2026; Digital Applied study 26 Apr 2026; TheNicheGuru approx. Oct 2026 (per snippet)
- Why it reads as AI: Models produce plausible round counts and generic attributions. A reader who checks finds nothing behind "Trusted by 10,000+", and trust drops.
- Fix: Give a real count with its source, a named customer with a quote, or drop the claim. Mark unverified stats as placeholders until real.
- Extends unslop: item 5 (vague attributions). Kept because the round-count and "Join thousands" forms come from marketing sources.
- Sources: S-D01-001, S-D01-015, S-D01-016, S-D01-041, S-D01-042
- Flag: Rated strong by source count only; the three sources are a fetched summary, a forum poster's unchecked claim (a traffic checker showing no traffic), and a search snippet, so the lead may prefer moderate. The Digital Applied study is by a CRO vendor, measures conversion only, and does not show any tested page was AI-written or that its claims were checked (its median lifts: named-customer count +22%, testimonial +14%, aggregate stat +9%, logo strip +8%, the aggregate lift falling sharply under 1,000). The Wikipedia guide is about encyclopedia text, so it supports the general pattern only. The raw claim also listed logo walls and invented testimonials, but no cited source covers them, so they are left out. Round numbers are often true, and the study's own +9% example is a specific-looking aggregate that performed; the tell is the missing source, not the number (see D01-N02).

### D01-007 Launch-email stock openers and hype punctuation
- Label: Avoid
- Confidence: moderate (a guide ban plus vendor sample outputs; the "say goodbye" and exclamation parts rest on the guide alone)
- Dated: practitioner advice undated; a real release note from 8 June 2026 uses the phrase
- Why it reads as AI: "We're excited to announce", "Say goodbye to X, hello to Y" and chummy openers are what email tools produce by default. They spend the first line on the announcement instead of the news.
- Fix: Lead with what is launching, the outcome and who it helps, with a concrete date or price. At most one exclamation point.
- Sources: S-D01-001, S-D01-017, S-D01-018, S-D01-019, S-D01-020
- Flag: Humans use the phrase in release notes and press releases (S-D01-020 is a real one), so this is a stock-phrase tell, not a machine-only one. Sample outputs are vendor-chosen. S-D01-017 is advice about reader scanning, not an AI claim. All but the guide are search only. No measured data. Not searched in round 2.

### D01-008 "Whether you're X or Y" and "Imagine" openers
- Label: Choose deliberately
- Confidence: anecdotal (one guide names it; vendor samples only show the phrase in use)
- Dated: no dated source names it as a tell
- Why it reads as AI: It sets up an audience or scene before saying anything, and it fits any product, so a page full of such openers feels templated.
- Fix: "For X who need Y." "Imagine" becomes the real before and after.
- Sources: S-D01-001, S-D01-021
- Flag: Only the marketingskills file calls this a tell. The vendor samples (one is a Wix "better" example that still uses it) show use, not that it is a tell. Human ad copy uses both openers; only default use across a page is suspect. Samples are search snippets only. Round 2 found no new source naming either opener a tell.

### D01-009 Platform or product as the actor
- Label: Choose deliberately
- Confidence: anecdotal (one guide; a directory example and a general Wikipedia note add little)
- Dated: practitioner advice 2025-2026
- Why it reads as AI: "Our platform empowers teams to..." hides who does what and turns the customer or player into an object.
- Fix: Make the customer the subject: "You import a CSV and see the totals in one screen."
- Sources: S-D01-001, S-D01-012, S-D01-016
- Flag: tropes.fyi gives one example sentence, seen only in a search snippet. The Wikipedia note is about promotional tone in general. Platform-as-actor is common in human B2B copy; only a page-wide default is cited. Round 2 found no new source naming it a tell.

### D01-010 Emoji bullets and checkmarks in feature lists
- Label: Choose deliberately
- Confidence: anecdotal (one guide; the Wikipedia source is the same page as S-D01-016; round 2 found no store-page evidence)
- Dated: first seen in chatbot output in 2025; defaults cut back in 2025-2026 (OpenAI release notes; PC World 5 May 2026); Wikipedia guide current Oct 2026; guide ban undated
- Why it reads as AI: Emoji or check symbols as bullet markers is a default layout from AI tools asked for a feature list. The Wikipedia guide says the habit is now less common than in 2025, so it dates a text as much as it flags one.
- Fix: Use the platform's own list formatting with feature-specific text. Keep emoji only where the brand is playful and the emoji carries meaning.
- Extends unslop: item 18 (decorative emojis). Kept as a separate record only to hold the store-page angle, which has no evidence of its own yet.
- Sources: S-D01-001, S-D01-016, S-D01-045, S-D01-046, S-D01-047
- Flag: Marketing evidence does not stand on its own. Two rounds found nothing on emoji bullets in Steam, itch or app-store copy, and the Steam Page Analyzer guide (S-D01-048) recommends bold headers and 4 to 6 bullets and never mentions emoji. The OpenAI and PC World items describe chat output, not product copy, and are search only; they date the habit and do not raise confidence. Label unsure: Avoid for B2B pages, Choose deliberately for a playful game page.

### D01-011 Contrast-reveal and negation-list slogans
- Label: Choose deliberately
- Confidence: moderate (2 independent marketing-specific sources for the contrast half: the marketingskills guide and Stockton's fetched post; the "No X. No Y. Just Z." list half has two further search-only lists)
- Dated: Stockton 16 Apr 2025; marketingskills guide undated; the "not X but Y" pattern is widely listed in 2025-2026; two list sites 2026
- Why it reads as AI: "It's not X, it's Y" and "No X. No Y. Just Z." let a slogan sound decisive without a claim; Stockton calls this borrowed depth, sounding sophisticated without being so. Left on default, the shape recurs in every section of a page.
- Fix: State the claim directly. If the contrast is the point, use it once and make both halves factual. Search a draft for "just" to find the pattern.
- Example done well: none. A 2025 ad line "This isn't just food" is cited as an early human use (S-D01-025).
- Extends unslop: item 9 (negative parallelisms). Adds the product-copy forms and the "No X. No Y. Just Z." list.
- Sources: S-D01-001, S-D01-023, S-D01-024, S-D01-025, S-D01-036, S-D01-043, S-D01-044
- Flag: Stockton describes the pattern as saturating LinkedIn, X and blogs, and his own advice is to use it sparingly and specifically, not to ban it, which is why the label stays Choose deliberately. Vollmer (S-D01-010) and aismells cite Stockton, so they are not independent of him and are not counted. The Antislop paper reports the pattern in functional writing and the EQ-Bench slop score weights it, but neither measures marketing copy, so they do not raise confidence. ContentBeta and Hunting the Muse are search snippets and may copy each other. The Antislop, EQ-Bench and HLTH items were seen as search results only, with no URL in the raw file. The pattern is old rhetoric; no measured marketing frequency was found.

### D01-012 Quotable sign-off instead of a call to action
- Label: Avoid
- Confidence: anecdotal (one guide)
- Dated: guide undated
- Why it reads as AI: A tidy quotable last line ends the page on a slogan where a reader needs the next step.
- Fix: End on a number, a customer, an offer or a call to action.
- Extends unslop: item 25 (generic conclusions). Adds the marketing fix (end on a call to action).
- Sources: S-D01-001
- Flag: Single source, a fetched summary. No independent marketing evidence. Round 2 found no source naming it a tell.

### D01-013 Bold-label colon feature lists as the page default
- Label: Choose deliberately
- Confidence: anecdotal (one source, the Wikipedia guide; the Steam guide recommends the layout and so counts against)
- Dated: Wikipedia guide current Oct 2026; Steam guide 18 Jan 2026
- Why it reads as AI: The Wikipedia guide names a vertical list with a bolded label and a colon before each explanation as a frequent chatbot pattern, often where the items have no real hierarchy. When every item carries one, the page looks assembled from a template.
- Fix: Use 3 to 6 bullets, each a complete thought with a number where one exists, and bold only what matters. A Steam guide puts it as "If everything is bold, nothing is".
- Sources: S-D01-016, S-D01-048
- Flag: The structure is standard Steam advice (see D01-N01); only the uniform default is the tell. The Steam quote comes from a summary and was not checked word for word. Wikipedia part is the same source as S-D01-016, so it adds no independence.

### D01-014 Uniformly upbeat copy with no stated limit
- Label: Choose deliberately
- Confidence: anecdotal (one source, the Wikipedia guide; the Steam guide only supports the numbers-over-praise fix)
- Dated: Wikipedia guide current Oct 2026; Steam guide 18 Jan 2026
- Why it reads as AI: The Wikipedia guide says an upbeat, wordy register is the model default and that readers may not notice it as robotic. A page that praises every feature in the same warm tone and names no limit, trade-off or non-audience gives the reader nothing to check.
- Fix: Name one limit, one trade-off, or who should not buy. Put the concrete figure where the copy would otherwise praise in general.
- Sources: S-D01-016, S-D01-048
- Flag: Same page as S-D01-016, so no extra independence. The guide itself says the habit may not register as robotic to general readers, and human product copy is often upbeat, so the tell may matter little to them.

## Not a tell

### D01-N01 Scannable Steam description structure
- Why it is fine: Short paragraphs, bold section headers and a stack of 3 to 6 features with 2 to 4 points each are standard Steam page advice for players who skim. What reads as AI is generic bullet content, not the list format. The same guides say to write benefits over specs ("Enemies that adapt to your tactics" over "over 200 enemies"). A further 2026 guide drawing on 405 sampled Steam pages recommends bold headers and 4 to 6 concrete bullets and says nothing marks the structure as AI; the uniform bold-label default is the warning (D01-013).
- Sources: S-D01-026, S-D01-027, S-D01-028, S-D01-029, S-D01-030, S-D01-031, S-D01-048

### D01-N02 Real, sourced numbers
- Why it is fine: Specific, checkable and attributed numbers are the fix for puffery. Only invented or suspiciously neat figures read as AI (see D01-006). An agency study found a specific aggregate stat ("Trusted by 12,400 marketing teams") lifted conversion, while vague "thousands" copy did not.
- Sources: S-D01-001, S-D01-016, S-D01-041

### D01-N03 Em dashes alone in ad copy
- Why it is fine: Human writers have always used the mark, so one em dash is not evidence of AI. Frequency across a text is the only signal the sources support. This is a detection point; the `unslop` skill's own style rule 13 (avoid em dashes) still applies to what we write.
- Sources: S-D01-032, S-D01-033, S-D01-034

## Sources
S-D01-001 | marketingskills copywriting reference ai-tells.md | https://github.com/coreyhaines31/marketingskills/blob/main/skills/copywriting/references/ai-tells.md | undated | guide | | fetched (WebFetch summary only)
S-D01-002 | Ruben Hassid, "It's not [X], it's [Y]" | https://ruben.substack.com/p/its-not-x-its-y | approx. spring 2026 | blog | | search only
S-D01-003 | useaiwriter.com, "300+ AI Words and Phrases to Avoid in 2026" | https://www.useaiwriter.com/articles/ai-words-to-avoid-2026 | 2026 | blog | | search only
S-D01-004 | Microcopy Examples, "Avoid landing page words" | https://microcopyexamples.substack.com/p/avoid-landing-page-words | undated | blog | | search only
S-D01-005 | Copy.ai landing page AI generator (vendor page) | https://www.copy.ai/blog/landing-page-ai-generator | approx. 2026 | blog | | search only
S-D01-006 | Olivia Cal, "How to Spot AI Writing Tells" | https://www.oliviacal.com/post/ai-writing-tells | 2026 | blog | | search only
S-D01-007 | Gaurav Tiwari, "Stop AI Slop" | https://gauravtiwari.org/stop-slop-ai-slop/ | undated | blog | | search only
S-D01-008 | Metaflow, best Claude skills for growth marketing (brand-voice template) | https://metaflow.life/blog/best-claude-skills-for-growth-marketing | approx. Oct 2026 | blog | | search only
S-D01-009 | Charlie Guo, "The Field Guide to AI Slop" | https://www.ignorance.ai/p/the-field-guide-to-ai-slop | approx. Oct 2025 | blog | | search only
S-D01-010 | Matthew Vollmer, "I Asked the Machine to Tell on Itself" | https://matthewvollmer.substack.com/p/i-asked-the-machine-to-tell-on-itself | undated | blog | | search only
S-D01-011 | Markets2Mountains, "Anti-Slop: 15 Patterns" | https://www.markets2mountains.com/posts/anti-slop-15-patterns | undated | blog | | search only
S-D01-012 | tropes.fyi directory | https://tropes.fyi/directory | undated | guide | | search only
S-D01-013 | Forbes (Charlie Fink), "The Seven Tells of AI Writing" | https://www.forbes.com/sites/charliefink/2025/06/12/the-seven-tells-of-ai-writing/ | 2025-06-12 | press | cites a marketing influencer's post | search only
S-D01-014 | Cherryleaf, indicators that something was written by AI | https://www.cherryleaf.com/2026/02/indicators-that-suggest-something-was-written-by-ai/ | 2026-02-13 | blog | | search only
S-D01-015 | Hacker News thread on AI-built landing pages (item 49024805) | https://news.ycombinator.com/item?id=49024805 | approx. late July 2026 | forum | | fetched (WebFetch summary; traffic claim is the poster's)
S-D01-016 | Wikipedia, "Signs of AI writing" | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | current Oct 2026 | guide | | fetched (WebFetch summaries across rounds 1 and 2; opening part of the page not read; round 2's deeper reading is the same source, not a new one)
S-D01-017 | WritingTools.ai, AI launch announcement email generator (vendor guide) | https://writingtools.ai/tools/ai-launch-announcement-email-generator | undated | blog | | search only
S-D01-018 | StoryLab.ai, sample AI email output (page title and URL not given in raw file) | no URL in raw file | undated | blog | | search only
S-D01-019 | Easy-Peasy.ai, sample AI email output (page title and URL not given in raw file) | no URL in raw file | undated | blog | | search only
S-D01-020 | PDQ release notes (real vendor release note using the phrase) | https://connect.pdq.com/hc/en-us/articles/10632822215835-Release-Notes | 2026-06-08 | guide | | search only
S-D01-021 | Sample landing-page copy from Copy.ai, Landingi, a Gumroad prompt pack and Wix | no URL in raw file | 2025-2026 | blog | | search only
S-D01-022 | Wikipedia, rule of three article (snippet) | no URL in raw file | undated | guide | | search only
S-D01-023 | Antislop paper, arXiv 2510.15061 | no URL in raw file | 2025 | study | | search only
S-D01-024 | EQ-Bench Slop Score (weights "not X but Y") | no URL in raw file | undated | study | | search only
S-D01-025 | HLTH, article citing the "This isn't just food" ad line | no URL in raw file | 2025 | blog | | search only
S-D01-026 | indiegamejoe.com, Steam page above-the-fold best practice | no URL in raw file | 2025-2026 | guide | | search only
S-D01-027 | presskit.gg, Steam page optimization 2026 | no URL in raw file | 2026 | guide | | search only
S-D01-028 | indieformer.com, Steam marketing guide | no URL in raw file | 2025-2026 | guide | | search only
S-D01-029 | gamedo.live, Steam store page guide | no URL in raw file | 2026 | guide | | search only
S-D01-030 | gamedevproducer.com, Steam page blueprint | no URL in raw file | 2025-2026 | guide | | search only
S-D01-031 | theorycraftmarketing.com, Steam page guide | no URL in raw file | 2026 | guide | | search only
S-D01-032 | The Ringer, argument that human writers always used em dashes | no URL in raw file | 2025-08-20 | press | | search only
S-D01-033 | Rolling Stone, similar point on em dashes | no URL in raw file | 2025-06-26 | press | | search only
S-D01-034 | Plagiarism Today, em dash test across chatbots | no URL in raw file | 2025-06-26 | blog | | search only
S-D01-035 | Blake Stockton, "Don't Write Like AI (4 of 101): Red Flag Words" (AI Writers Room; a personal list with no data or outside list cited; does not name "tapestry") | https://www.blakestockton.com/p/red-flag-words | 2025-07-07 | blog | | fetched (gatherer's summary; lead also fetched)
S-D01-036 | Blake Stockton, "Don't Write Like AI (1 of 101): 'It's Not X, it's Y'" | https://www.blakestockton.com/p/dont-write-like-ai-1-101-negation | 2025-04-16 | blog | | fetched (gatherer's summary; lead also fetched)
S-D01-037 | FeedHive AI Slop Detector (open-source slop list) | https://www.feedhive.com/tools/ai-slop-detector | approx. Oct 2026 (per snippet) | blog | | search only
S-D01-038 | EnhancePost, "The AI Slop Words and Phrases List (2026)" | https://enhancepost.com/blog/ai-slop-words-phrases-list/ | 2026-09-07 | blog | | search only
S-D01-039 | SlopDetector.org, "The AI Words List" | https://slopdetector.org/blog/ai-words-list | 2026-07-31 | blog | | search only
S-D01-040 | Emily Aborn, "AI Writing Tells & What They Cost You" | https://emilyaborn.com/ai-writing-tells-what-they-cost-you/ | 2026 | blog | | search only
S-D01-041 | Digital Applied, "Landing Page Conversion in 2026: 2,000 Pages Tested" (agency study; measures conversion, not AI authorship) | https://www.digitalapplied.com/blog/landing-page-conversion-study-2000-pages-tested-2026 | 2026-04-26 | study | | fetched (summary)
S-D01-042 | TheNicheGuru, "How to Create a Landing Page with AI in 8 Steps" | https://thenicheguru.com/blogging/how-to-create-a-landing-page/ | approx. Oct 2026 (per snippet) | blog | | search only
S-D01-043 | ContentBeta, "List of 300+ AI Words, Phrases and Sentences to Avoid (2026)" | https://www.contentbeta.com/blog/list-of-words-overused-by-ai/ | 2026 (updated approx. Oct 2026, per snippet) | blog | | search only
S-D01-044 | Hunting the Muse, "How to spot when writing is AI: 6 elements of a robot's style" | https://huntingthemuse.net/library/how-to-tell-if-writing-is-ai | undated | blog | | search only
S-D01-045 | OpenAI Help, "ChatGPT release notes" (dates emoji-heavy and reduced-emoji model changes) | https://help.openai.com/en/articles/6825453-chatgpt-release-notes | 2025-2026 | policy | | search only (dates from search summary)
S-D01-046 | OpenAI Help, "Model Release Notes" (dates emoji and list personalization controls) | https://help.openai.com/en/articles/9624314-model-release-notes | 2025-2026 | policy | | search only (dates from search summary)
S-D01-047 | PC World, "ChatGPT's new default model is dialing back the annoying emojis" | https://www.pcworld.com/article/3132088/chatgpts-new-default-model-is-dialing-back-the-annoying-emojis.html | 2026-05-05 (per search summary) | press | | search only
S-D01-048 | Steam Page Analyzer, Steam description writing guide (405 Steam pages sampled Feb to Jul 2026) | https://www.steampageanalyzer.com/blog/steam-description-writing-guide | 2026-01-18 (updated 2026-09-15) | blog | | fetched (summary)
