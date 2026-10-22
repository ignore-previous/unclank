# D02 social-ads-marketing

Social posts on X, Bluesky, LinkedIn and Reddit, TikTok scripts, devlog posts, ad copy, ad creatives, AI-avatar and UGC-style video ads, and marketing approaches such as hook formulas, engagement bait, thread templates and invented founder stories. Rounds 1 and 2 are merged (both gathered by claude-haiku-5-5). Much of the quantified evidence comes from detector vendors, post-scheduling tools and ad-tool vendors with a stake in the result; those sources are marked "(vendor)" in the source list. Only D02-004 reaches strong, and it rests on platform rules and statements more than on reader data. The rest is thin: round 2 mostly confirmed platform policies on primary pages, and TikTok wording, the Harris Poll figures and the Sprout Social figures are still search only. The tells are grouped under "Posts and threads" first and "Ads and creatives" second, so the file can be split later.

## Checklist
- [Avoid · strong] Do not automate replies or comments to people who have not engaged with you; reply by hand with one specific detail from the post, or say nothing. (D02-004)
- [Avoid · moderate] Do not publish founder stories, customer wins, testimonials or "witnesses" you cannot back with real names and checkable numbers; never use synthetic people as customers. (D02-005)
- [Avoid · moderate] Cut stock AI vocabulary and cliché phrases ("delve", "testament", "game-changer", "let that sink in"); use the plain verb and say what the thing did. (D02-003)
- [Choose deliberately · moderate] Say the claim directly instead of "not X, it's Y" or reflexive lists of three; keep a contrast only where the contrast is the point. (D02-002)
- [Choose deliberately · moderate] Open with the specific event, number or claim, not a stock hook ("Nobody talks about...", "Stop X, start Y", "Here's what..."); if you keep a hook shape, earn it in the next line. (D02-001)
- [Choose deliberately · moderate] Keep an AI presenter in an ad only with a reason: check lip sync, motion and lighting at phone size, never pass it off as a customer, and prefer real creators or real hands and voices in a creator-style feed. (D02-010)

## Tells

### Posts and threads

#### D02-001 Stock hook formulas
- Label: Choose deliberately
- Confidence: moderate (1 with good data: MagicPost study (vendor), 143,515 posts from 3,000 authors; a Medium blog, hook guides and a second MagicPost article from the same vendor add no weight)
- Dated: noted from LinkedIn hook guides and 2025 AI-post commentary (exact start not found), still cited in 2026
- Why it reads as AI: Fixed openers such as "Nobody talks about...", "Stop X, start Y", "Here's what/how" and "The result?" are what a template-driven generator produces first, and they now appear on lists of copy-paste openers. The formula is not the problem; it standing in for a point is.
- Fix: Open with the specific thing that happened, the number, or the claim itself.
- Sources: S-D02-001, S-D02-002, S-D02-003, S-D02-047
- Flag: The only fetched evidence is one vendor study. It measured reach against each author's own average (about -6.7% for "Stop X, start Y", -4.8% for "The result?", -4.3% for "Here's what/how"), calls this correlation, and found the cost not measurable after 27 July 2026 once substance was held equal. A second MagicPost article (Oct 2026, search only, same vendor, not independent) gives -4.1% for "Here's what/how" against -4.3% in the first, so the exact figure is unsettled. The Medium list and the guides that still teach "Nobody talks about" as a live hook are search only. Round 2 found no independent measurement of opener wording. Lean second-order: substance matters more than the phrase.

#### D02-002 Negative-parallel contrast and rule-of-three lists
- Label: Choose deliberately
- Confidence: moderate (2 independent: Wikipedia WikiProject AI Cleanup guide; MagicPost study (vendor) measuring "It's not X, it's Y" at about -4.9% reach)
- Dated: noted from 2024-2025 AI-writing commentary, still listed in the Wikipedia guide as of Oct 2026
- Why it reads as AI: "Not X, but Y" and neat triplets replace a plain statement with a contrast or a rhythm, and the Wikipedia guide names both as common AI signs.
- Fix: State the claim directly; use two items when two is the real number.
- Sources: S-D02-004, S-D02-001
- Flag: Label is my change from the gatherer's "Avoid". The construction is old rhetoric humans use, and the Wikipedia page says its signs are observations, not rules, with unreliable detectors and judges. The reach figure covers only "It's not X, it's Y", is vendor-run and correlational. The Wikipedia guide is about encyclopedia text, not social posts. No new evidence in round 2.

#### D02-003 Stock AI vocabulary and cliché phrases
- Label: Avoid
- Confidence: moderate (2: Wikipedia guide with era-by-era word lists; one author's hand-labelled count of 500 LinkedIn posts, weak method)
- Dated: noted from 2023-2024 (GPT-4 era); word lists drift per model generation; still cited Oct 2026
- Why it reads as AI: Words like "delve", "testament", "fostering", "showcasing" and "leverage" cluster in model output by generation, and phrases like "let that sink in" and "game-changer" turn up far more often in AI-generated LinkedIn posts than in ordinary writing.
- Fix: Use the plain verb and say what the thing did; cut "pivotal" and "landscape" unless you can say what changed.
- Sources: S-D02-004, S-D02-005
- Flag: The two sources cover different words and neither is rigorous. The DEV author calls the count "directional data, not gospel", labelled posts by hand, and gives no baseline for normal usage (28x for "let that sink in", 19x for "game-changer" is relative to that author's own sense of normal). The Wikipedia lists are from Wikipedia text and go stale. No new evidence in round 2.

#### D02-004 Generic automated replies and comments
- Label: Avoid
- Confidence: strong (3 independent origins: LinkedIn, reported by Fortune and by Social Media Today as two separate statements and counted once; X's own developer rules; Pangram per-platform scan (vendor). Further platform-enforcement items are search only and not counted)
- Dated: noted from 2024-2025; LinkedIn help change reported 20 Aug 2025; X developer rules page undated, current when fetched in round 2; enforcement reported May 2026 (LinkedIn) and July 2026 (X); still cited 2026
- Why it reads as AI: Automated replies follow one template, arrive fast, restate the post in smoother words and end on a generic question or emoji, so the same reply appears under every post. Platforms now treat this as automation.
- Fix: Reply by hand with one specific detail from the post or your own experience, or do not reply; never automate replies to people who did not reply to you.
- Sources: S-D02-006, S-D02-010, S-D02-034, S-D02-035, S-D02-007, S-D02-008, S-D02-009
- Flag: The strength rests on how platforms treat automation, not on data that readers notice the pattern; round 2 found no reader-side measurement. X's developer guidelines say deploying AI-generated replies without approval is a violation, and ban keyword-triggered auto-replies, but allow one auto-reply to a user who already replied to you, so the rule targets unsolicited automation. LinkedIn's help text, as reported by Social Media Today, says it may limit visibility of comments made with automation tools; LinkedIn's own Professional Community Policies page does not name bots or automation tools (fetched), so the LinkedIn rule rests on the press report of the help text, which was not fetched. LinkedIn's comment crackdown figures (including a 94% accuracy claim by an executive), X's removal of about 42,000 accounts and X's engagement-bait payout change are search only, come from platforms or secondary outlets, and carry no independent false-positive data. Pangram's own false-positive claim is the vendor's. The tell is platform-specific: the fetched Pangram scan found Reddit replies 98.1% human, while LinkedIn comments were slightly more likely AI than top-level posts once length was controlled.

#### D02-005 Fabricated founders, personas and testimonials
- Label: Avoid
- Confidence: moderate (3 distinct sources: the FTC rule, now seen on the FTC's own page, with the earlier law-firm blogs counted as coverage of it, not extra sources; ABC News investigation via PYMNTS, search only; Futurism, search only)
- Dated: first cases 2024-2025; FTC final rule announced 14 Aug 2024, in force since 21 Oct 2024; 2026 coverage of AI-made founders and fake PR personas
- Why it reads as AI: The story is generic and cannot be checked, and the people behind it have no traceable record. Generators make these cheaply, which is why regulators and journalists name them.
- Fix: Publish only stories and testimonials you can stand behind: real names, real numbers, a way to check them; do not use synthetic people as witnesses or customers.
- Sources: S-D02-036, S-D02-037, S-D02-011, S-D02-012, S-D02-013
- Flag: The FTC release (fetched) names fake reviews by "someone who does not exist, such as AI-generated fake reviews" and civil penalties against knowing violators. That covers reviews and testimonials; it does not name founder stories or personas in general. A founder story falls under the rule only if presented as a customer review or testimonial, so the founder and persona part rests on the two search-only press items. The rule text on the Federal Register (16 CFR Part 465) was seen in search only. The $53,088 per-violation figure for 2026 comes from secondary compliance sites and is not confirmed by the FTC; the earlier "near $53,000" is the same figure, unresolved. Law-firm blogs disagreed on whether the rule names AI; the FTC page does. The sources show that fabrication happens and is penalised, not that readers can spot it. No counter-evidence found: real build-in-public posts with real numbers are fine.

#### D02-006 Engagement pods and mass-liked "proof" posts
- Label: Avoid
- Confidence: anecdotal (1 for the claim that pods are automation-run and generic: Spinutech and vendor blogs, May 2026; LinkedIn's own policy confirms the ban but not that readers see pods as AI)
- Dated: noticed 2024-2025; LinkedIn policy page undated, fetched in round 2; press report 20 Aug 2025; Terms of Service stance reported 2026
- Why it reads as AI: Groups that like and comment on each other within minutes are often run by automation, and the comments are generic.
- Fix: Do not join pods; earn comments with a point someone can answer.
- Sources: S-D02-007, S-D02-038, S-D02-035
- Flag: Evidence upgraded, confidence not. LinkedIn's Professional Community Policies (fetched) tell members not to agree with others ahead of time to like or re-share, so the policy ban is confirmed on the primary page. The Spinutech report of LinkedIn's stance repeats that same origin, and Social Media Today's piece relays LinkedIn lowering reach for pods and automation, so these do not count as separate sources. The claim that pods are automated and read as AI still rests on search-only agency and vendor blogs. The same press piece says much pod coordination happens off-platform, which makes enforcement harder. The "97% accuracy" detection figure comes from a vendor of AI comment tools and is not usable. No independent measurement of how pod posts look to readers.

#### D02-007 Chatbot formatting leftovers in posts and devlogs
- Label: Avoid
- Confidence: anecdotal (1: Wikipedia guide)
- Dated: noted from 2023 onward, still listed Oct 2026
- Why it reads as AI: Stray asterisks and hash headers, heavy bold, bold inline labels, emoji standing in for headings, title case in running text and curly quotes are default chat-tool formatting pasted in without cleanup.
- Fix: Paste plain text into the platform's editor and check for leftover symbols; use plain sentences for headers.
- Sources: S-D02-004
- Flag: Single source, and it describes Wikipedia articles, not social posts. Markdown and emoji are fine on platforms that render them, and bold labels can be good structure in a devlog; the tell is unrendered or unedited leftovers. No new evidence in round 2.

#### D02-008 Thread template skeletons
- Label: Choose deliberately
- Confidence: anecdotal (1 cluster: template and tweet-tool vendors selling the formats)
- Dated: template sets circulate 2024-2026, still cited
- Why it reads as AI: The same three-beat progress thread ("shipped / didn't / next", "Here's what I learned", "Everyone says X. Nobody explains how", a thread-emoji opener) used unchanged across projects looks template-made.
- Fix: Pick the one thing that happened this week and write about it; cut any beat with no real content.
- Sources: S-D02-014, S-D02-010
- Flag: Search only; the only evidence is that template sellers offer these formats, not that readers or detectors flag them. An unnamed "average AI thread length of about 1.02 tweets" figure cited by one template vendor has no source or method and is not used. Pangram's X numbers (10.0% of top-level posts, 23.9% of X articles flagged AI) are vendor figures about AI content in general, not thread format. Templates are used by humans and work; the tell is the unedited default. No new evidence in round 2.

#### D02-009 Confession hooks and engagement-ask closers
- Label: Avoid
- Confidence: anecdotal (X's penalty on explicit engagement asks is now verified on the fetched article, but it is one platform statement and not data on AI or readers; the template-page and hand-count sources describe adjacent patterns)
- Dated: 2025-2026 template sets; X rule change 16 Jul 2026
- Why it reads as AI: Openers such as "Honest moment:" or "Not sure what to do. Any founders dealt with this?" and bare closers like "Agree?" or "Thoughts?" ask for replies by rote, with no specific situation behind them. X now also penalises explicit asks such as "I'll follow everyone who replies".
- Fix: Name the specific problem and the options you are weighing; ask one question you need answered, about a specific choice; drop the "Agree?" closer and any "reply and I'll follow back" ask.
- Sources: S-D02-014, S-D02-005, S-D02-009, S-D02-039
- Flag: Round 2 opened S-D02-009 (Social Media Today, quoting an X product head): accounts that solicit engagement three or more times lose revenue-share access. This is the same source as round 1, now verified, not a second one. The rule covers explicit asks; "Thoughts?" and "Agree?" are not named, so the rote-closer half of the tell has no direct evidence. The template text is vendor-supplied and search only. The DEV count (a "Humble Brag Confession" opener leading in 27% of 500 AI-generated posts) is a hand-labelled sample and a different phrasing. Sprout Social's Q1 2026 pulse survey (vendor) reportedly lists engagement-bait tactics (about 23%) among behaviours brands should stop; the PDF was unreadable, so this is search only and not counted. One closing question is not a tell: see D02-N03.

### Ads and creatives

#### D02-010 Stiff or glossy AI-avatar presenters in feed ads
- Label: Choose deliberately
- Confidence: moderate (2: NN/g critique of uncanny AI ad visuals; affiliate and vendor review blogs, counted as one cluster. Kantar's data covers AI ads in general, not avatars, so it is context and not a third source)
- Dated: noticed 2024-2025 in HeyGen-style tools, still cited in 2026 reviews; Kantar figures 26 Mar 2026; counter-evidence study Apr 2025
- Why it reads as AI: Stiff head movement, drifting lip sync, rubbery skin or studio-clean lighting in a feed of real creator content reads as an ad, and the near-human look breaks the emotional beat. The tell is the delivery, not photorealism as such.
- Fix: Use real creators, or shoot close-ups with real hands and voices; if you use an avatar, check lip sync and motion at phone size before launch, keep it where a glossy presenter fits, and do not present it as a customer.
- Fixable: partly (lip sync and lighting can be edited; stiff faces and skin are harder)
- Sources: S-D02-016, S-D02-015, S-D02-023, S-D02-017, S-D02-018, S-D02-030, S-D02-031, S-D02-032
- Flag: Label changed from Avoid to Choose deliberately on the round 2 gatherer's suggestion; this is the lead's call. No source tests stiffness or lip sync in ads. NN/g's article critiques AI holiday ads, not avatar UGC, and cites no user research. The review blogs are affiliate or vendor pages and search only. Counter-evidence: a peer-reviewed study (Baake, Schmitt and Metag, Journal of Science Communication, Apr 2025) found realistic avatars rated more positively than cartoon-style ones, so realism alone gives no penalty; it tested German science-communication video with a panel of about 491, not ads, and its authors limit the result to their conditions (see D02-N06; the paper page is search only, the release fetched). General AI-ad penalty, from Kantar's ad-testing database (26 Mar 2026): GenAI-made ads average the 54th percentile on overall impact against the 65th for non-AI ads, with wide spread, and 57% of consumers worry about fake or misleading AI ads. Kantar gives no detection-rate figure and no avatar breakdown. The best consumer data on detection cuts the other way: in the Ipsos with Syracuse Newhouse study (3,000 US respondents, 20 ads, May 2026), only 13% of viewers who saw an AI ad were at least somewhat confident it was AI, and 13% suspected human ads. A second article gives 25% for the same measure (search only, conflicts; the Syracuse release is primary). So the cost is in feel and effect, not detection. A glossy avatar can suit a B2B explainer; the format itself is a deliberate choice.

#### D02-011 Rapid-montage, stitched-together AI ads
- Label: Avoid
- Confidence: anecdotal (1 opinion for the visual pattern: NN/g; surveys, Kantar and press below support only the general AI-ad penalty)
- Dated: 2025 holiday ads (Coca-Cola, McDonald's Netherlands) and Super Bowl 2026; Kantar 26 Mar 2026; still cited Oct 2026
- Why it reads as AI: Many one-second clips, distant shots that hide distortion and few human close-ups let a tool hide flaws, and the story follows what the tool can do rather than what the story needs.
- Fix: Use fewer, longer shots; shoot human close-ups or use real footage; write the story first, then pick tools.
- Fixable: partly (editing and reshooting fix the montage; uncanny faces are harder)
- Sources: S-D02-016, S-D02-019, S-D02-020, S-D02-021, S-D02-022, S-D02-017, S-D02-030, S-D02-044
- Flag: NN/g cites production figures (e.g. about 70,000 clips for Coca-Cola's 2025 ad) but no audience research; round 2 confirmed this on the page, and that Coca-Cola's 2025 ad swapped people for animals to avoid close-ups, so the clip count is production effort, not a visible flaw. IAB (505 US consumers; 71% think they have seen an AI ad, up from 54%) and Digiday (McDonald's Netherlands pulled an AI Christmas ad in Dec 2025) show general backlash, not montage specifically. The Harris Poll figures (78% say AI makes ads feel less authentic; 73% less likely to trust a suspected AI ad; six countries, n=6172, per a search snippet) are search only, because the Harris pages returned 403 in both rounds and the saved deck was unreadable. The Super Bowl 2026 item is a single vendor blog, search only. Performance evidence on the general AI-ad penalty: Ipsos/Syracuse had AI ads 5 points below the sales benchmark against 11 above for human ads; Kantar's database puts GenAI ads at the 54th percentile on overall impact against the 65th for non-AI ads, with wide spread and no detection figure. Taboola's click-through figure (0.76% AI against 0.65% human, raw) is a vendor's own platform data and does not hold up: Taboola's own release says AI ads performed comparably under its strictest controls (sibling ads from one advertiser, campaign and day), so it is not evidence that AI ads under- or over-perform and is not used.

#### D02-012 Ad edits applied by platform AI tools unless you opt out
- Label: Choose deliberately
- Confidence: anecdotal (1: Marketing Brew trade piece with several marketers quoted, 21 Apr 2026; Meta's help page confirms the features and labels for material edits but not the complaint)
- Dated: marketer complaints reported late 2025 into 2026, Marketing Brew 21 Apr 2026
- Why it reads as AI: The marketers quoted say Meta's AI creative tools changed their ads without their knowledge: resized and restyled images, invented products, and a "strange AI sheen" that looks like generation, not a creative choice. They also report that the features can re-enable when an ad is duplicated.
- Fix: Check the Advantage+ creative settings on every ad, including duplicates, switch off the generative enhancements you did not choose, and compare the rendered ad on a phone with your original asset before launch.
- Fixable: yes by editing (turn off the features and check the render)
- Sources: S-D02-040, S-D02-033
- Flag: One trade piece. The claims come from marketers and a brand's customer post as quoted by Marketing Brew, second-hand in places, and the brand's statement that it had opted out of every feature was not checked. Meta's spokesperson says advertisers can opt out in Ad Account Settings, and, per the gatherer's notes, that tests run on a small share of impressions. The article never says the tools are on by default, so the tell is worded as "applied unless you opt out", attributed to the marketers. Meta's help page (undated) says it labels ads "created or materially edited" with its generative features and does not label minor or immaterial changes such as resizing or colour correction.

#### D02-013 Benefit-first AI UGC scripts
- Label: Avoid
- Confidence: anecdotal (1 cluster: three AI-UGC tool vendors, all search only)
- Dated: 2025-2026 vendor guides; still cited Oct 2026
- Why it reads as AI: In UGC-format ads, an AI-written spoken script defaults to benefit language and polished grammar, with no friction, no specific problem and no creator's own words, so it sounds like brand copy; a real creator sounds less even.
- Fix: Start from one specific problem and the creator's own words, include one detail only someone who used the product would know, and read the script aloud and cut any line that sounds like an advert.
- Fixable: yes by editing the script
- Sources: S-D02-041, S-D02-042, S-D02-043
- Flag: Search only, and each source sells AI UGC tools, so the advice serves their product. Tagshop's summary of a Reddit thread (not opened) says generic "buy now" scripts perform poorly while problem-led AI scripts convert about as well as real creator content, so the fix may be a better script, not a human. No measured data on script wording. Plain grammar and no contractions also occur in human scripts, so grammar alone is not the tell.

## Not a tell

### D02-N01 Clear disclosure of AI use in ads
- Why it is fine: Disclosing AI is good practice and does not hurt purchase intent on average: 73% of Gen Z and millennials said knowing an ad used AI would raise or not change their likelihood to buy, and 89% of advertisers using gen AI for ads disclose at least sometimes (fewer than half always). Harris respondents ranked being told every time AI is used as their top comfort measure (45%, search only), and Sprout's Q1 2026 pulse survey (vendor, search only) reportedly has unlabelled AI content as the top behaviour brands should stop (28%). Kantar finds 57% of consumers worry about fake or misleading AI ads, which is why disclosure matters. Meta's own help page says ad images with an AI-generated photorealistic human get a label next to "Sponsored", and does not label minor or immaterial edits. Meta's political, social issue and election ad standards (change log 2 Jul 2026) say photorealistic AI media must be disclosed or the ad is rejected; that scope is political ads only. TikTok's rules for realistic AI avatars are still search only.
- Sources: S-D02-020, S-D02-021, S-D02-029, S-D02-028, S-D02-033, S-D02-045, S-D02-030, S-D02-039
- Flag: Some research and one Aug 2026 poll report (search only, unchecked) suggest labels can lower trust, so treat it as good practice, not proof of no cost. Meta's own pages conflict on third-party tools: the help page says no AI info is added when ads are made or changed with third-party tools, while the newsroom page (updated 1 Jun 2026, S-D02-046) says Meta will automatically detect third-party AI tools; unresolved. The TikTok claims (a "Misleading and false content" ad-policy section updated April 2026; a 21 Jul 2026 "mandatory labels for all AI ads" claim from one blog) are search only and unconfirmed; the TikTok pages returned only titles or errors. The Sprout PDF was unreadable, so its figures are not verified.

### D02-N02 Concrete detail and lived experience in posts
- Why it is fine: The specific posts people blame on AI are the ones that help reach: since 27 July 2026, lived experience added about 25% reach and concrete detail about 14% against the author's average, while posts with neither were about 23% below it (40,937 posts from 660 creators).
- Sources: S-D02-001
- Flag: One vendor dataset, correlational.

### D02-N03 Sincerity, one closing question and P.S. sign-offs
- Why it is fine: Ordinary human habits some call AI tells: genuine sincerity added about 4.6% reach, a closing question about 2.9% (2025 data), and a P.S. sign-off about 5.9% in 2025 with no measurable effect since late July 2026, so no single device is a safe signal either way.
- Sources: S-D02-001
- Flag: One vendor dataset, correlational.

### D02-N04 Using AI as a drafting tool with human review
- Why it is fine: AI use is not the tell; unedited output is. 43% of consumers want human review of AI content (Harris, search only), brands claiming to be anti-AI are called hypocritical because AI is usually used somewhere in production, and AI did best with straightforward, product-driven briefs in the Ipsos/Syracuse study.
- Sources: S-D02-019, S-D02-017, S-D02-021
- Flag: The Harris and Digiday points are self-reported attitudes, and Digiday quotes people who sell AI-using production.

### D02-N05 Human-made work accused of being AI
- Why it is fine: Clean human art, voices and writing gets flagged as AI: developers reported wrongful accusations around Steam Next Fest in Feb 2026, and a Steam review called a human-written story ChatGPT-made. A look that "feels AI" is not proof of AI use.
- Sources: S-D02-024, S-D02-025, S-D02-026, S-D02-027
- Flag: All search only, anecdotes from one period. The cited Microsoft figure (people identify AI content about 62% of the time) was not checked.

### D02-N06 A realistic human presenter as such
- Why it is fine: Realism alone is not a trust cost on the evidence found: a peer-reviewed study rated realistic avatars more positively than cartoon-style ones, so what reads as AI in D02-010 is stiff or glossy delivery, not a human-looking face. Taboola's data (vendor) also lists a large, clear human face among the strongest trust cues.
- Sources: S-D02-031, S-D02-032, S-D02-044, S-D02-030
- Flag: Counter-evidence to D02-010, not about ads. The study is German science communication with a panel of about 491, rated realism only moderate, and holds "at least in our conditions" per its authors; the paper page is search only and the EurekAlert release was fetched. The Taboola data is a vendor's own and is not otherwise used here. Kantar finds only 48% like seeing AI-generated images in ads, so liking is a separate question from realism.

## Sources
S-D02-001 | AI Posts Get Less Engagement on LinkedIn (MagicPost; 143,515 English posts from 3,000 authors, Dec 2024 to May 2026; July 2026 run on 40,937 posts from 660 creators) | https://magicpost.in/blog/ai-posts-less-engagement-linkedin | 2026 (page date not visible) | study (vendor) | | fetched
S-D02-002 | LinkedIn vs AI Slop (Medium) | https://medium.com/@sushilaDevi/linkedin-vs-ai-slop-9eb34619847e | about 60 days old when gathered | blog | | search only
S-D02-003 | LinkedIn hook examples and formulas (LinkedGrow; PostPlank and ViralBrain also teach "Nobody talks about", no URLs in raw) | https://linkedgrow.ai/blog/linkedin-hook-examples-formulas | 2026 | guide | | search only
S-D02-004 | Wikipedia:Signs of AI writing (WikiProject AI Cleanup advice page, not policy; first 100,000 characters read) | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | Oct 2026 | guide | | fetched
S-D02-005 | I Analyzed 500 AI-Generated LinkedIn Posts (DEV Community, hand-labelled sample) | https://dev.to/adrianvegaresearch/i-analyzed-500-ai-generated-linkedin-posts-heres-what-they-all-have-in-common-2h36 | about 8 months old when gathered | blog | | fetched
S-D02-006 | LinkedIn "Seems like AI slop" button and automated comments (Fortune) | https://www.fortune.com/2026/07/31/linkedin-seems-like-ai-slop-button-billions-automated-comments-attempts/ | 31 Jul 2026 | press | | fetched
S-D02-007 | LinkedIn May 2026 comment crackdown and engagement pods (Spinutech, TheNextWeb and vendor blogs; no URLs in raw) | no URL in raw | May 2026 | press | | search only
S-D02-008 | X removes about 42,000 AI-reply accounts, July 2026 (Startup Fortune; TrustAudience guide; no URLs in raw) | no URL in raw | Jul 2026 | press | via an X product lead's post as reported by secondary outlets | search only
S-D02-009 | X updates its engagement bait detection (Social Media Today; quotes an X product head: soliciting engagement 3 or more times costs revenue-share access) | https://www.socialmediatoday.com/news/x-updates-its-engagement-bait-detection/825495/ | Jul 2026 (change dated 16 Jul 2026) | press | via the X product head's post | fetched (opened in round 2)
S-D02-010 | AI in Your Feed (Pangram) | https://www.pangram.com/blog/ai-in-your-feed | 9 Jul 2026 | study (vendor) | | fetched
S-D02-011 | FTC final rule on fake reviews and influencer marketing (Isabokelaw; other law-firm blogs not named) | https://www.isabokelaw.com/blog/ftc-final-rule-on-fake-reviews-and-influencer-marketing-what-brands-and-creators-need-to-know | 2026 | guide | | search only
S-D02-012 | AI fakes the founder and keeps the money (PYMNTS) | https://www.pymnts.com/commerce/social-commerce/2026/ai-fakes-the-founder-and-keeps-the-money | 8 May 2026 | press | via ABC News investigation | search only
S-D02-013 | PR firm with fake publicist personas and AI headshots (Futurism; no URL in raw) | no URL in raw | 2026 | press | | search only
S-D02-014 | Template and tweet-tool vendor pages: AutoTweet, Xholic, Teract, OpenTweet (no URLs in raw) | no URL in raw | 2026 | guide (vendor) | | search only
S-D02-015 | AdLibrary and other AI-avatar review blogs (no URLs in raw) | no URL in raw | 2026 | blog (vendor) | | search only
S-D02-016 | Why AI-Generated Holiday Ads Fail (Nielsen Norman Group; critique, no user research) | https://www.nngroup.com/articles/ai-ad/ | undated in fetch, 2025-2026 | guide | | fetched
S-D02-017 | Newhouse research finds AI ads fall short on sales impact (Syracuse; Ipsos with Syracuse Newhouse, 3,000 US respondents, 20 ads, 10 brands) | https://news.syr.edu/2026/05/18/newhouse-research-finds-ai-ads-fall-short-on-sales-impact/ | 18 May 2026 | study | | fetched
S-D02-018 | App Developer Magazine on the same Ipsos/Syracuse study, giving 25% (no URL in raw; conflicts with S-D02-017) | no URL in raw | 2026 | press | | search only
S-D02-019 | With AI backlash building, marketers reconsider their approach (Digiday; also cites the Taboola click-through figure second-hand) | https://www.digiday.com/marketing/with-ai-backlash-building-marketers-reconsider-their-approach/ | 12 Feb 2026 | press | | fetched
S-D02-020 | The AI Ad Gap Widens (IAB; 505 US consumers, fielded Oct 2025 to Jan 2026) | https://www.iab.com/insights/the-ai-gap-widens/ | 2026 | study | | fetched
S-D02-021 | I Never Asked for This (Harris Poll with the 4As and Infillion; six countries, n=6172 per a search snippet; the report page returned 403 in both rounds, and the fetched PDF deck was binary and unreadable) | theharrispoll.com/reports/i-never-asked-for-this/ (as given in raw, search snippet only) | Jun 2026 | study | | search only
S-D02-022 | Super Bowl 2026 AI ads (hellowarrant blog; no URL in raw) | no URL in raw | 2026 | blog (vendor) | | search only
S-D02-023 | Webseotrends and Playcut AI-avatar comparison blogs (affiliate/vendor; no URLs in raw) | no URL in raw | 2026 | blog (vendor) | | search only
S-D02-024 | Developers wrongly accused of AI use before Steam Next Fest (Metricus; no URL in raw; includes an unchecked Microsoft 62% figure) | no URL in raw | 22 days old when gathered | blog | | search only
S-D02-025 | Crime Scene Cleaner denies AI assets (Plagiarism Today; no URL in raw) | no URL in raw | Apr 2026 | blog | | search only
S-D02-026 | Shrine's Legacy Steam review called story ChatGPT-written (no outlet or URL in raw) | no URL in raw | Dec 2025 | press | | search only
S-D02-027 | Indie dev's wife as voice actor after AI voice accusation (Dexerto; no URL in raw) | no URL in raw | 2026 | press | | search only
S-D02-028 | AI labels can undercut trust in advertising (Fingerlakes1; no URL in raw) | no URL in raw | Aug 2026 | press | | search only
S-D02-029 | TikTok and Meta AI-ad and AI-avatar labelling rules (vendor blogs, unnamed, disagreeing on dates; no URLs in raw) | no URL in raw | 2026 | blog (vendor) | | search only
S-D02-030 | The state of GenAI in media and advertising: Momentum meets reality (Kantar; LINK ad-testing database, no sample size given; GenAI ads average the 54th percentile on overall impact vs the 65th for non-AI ads; 57% worry about fake or misleading AI ads; no detection-rate figure) | https://www.kantar.com/inspiration/advertising-media/the-state-of-genai-in-media-and-advertising | 26 Mar 2026 | study | fetched by the lead | fetched
S-D02-031 | Balancing realism and trust: AI avatars in science communication (Baake, Schmitt and Metag, Journal of Science Communication 24(2) A03; about 491 respondents; science communication, not ads) | https://jcom.sissa.it/article/pubid/JCOM_2402_2025_A03/ | Apr 2025 | study | | search only
S-D02-032 | EurekAlert release on the JCOM avatar study | https://www.eurekalert.org/news-releases/1079762 | 15 Apr 2025 | press | | fetched
S-D02-033 | How AI-generated images in ads are identified and labeled on Meta (Meta help page; undated; conflicts with S-D02-046 on third-party tools) | https://www.meta.com/help/artificial-intelligence/355108217670024/ | undated | policy | | fetched
S-D02-034 | Developer Guidelines, gray areas on AI-generated content and replies (X) | https://docs.x.com/developer-guidelines | undated | policy | | fetched
S-D02-035 | LinkedIn May Limit the Visibility of Comments Made via Automation Tools (Andrew Hutchinson, Social Media Today; quotes LinkedIn's help text) | https://www.socialmediatoday.com/news/linkedin-limit-visibility-of-comments-made-via-automation-tools/758207/ | 20 Aug 2025 | press | quotes LinkedIn help-page text (help page not fetched) | fetched
S-D02-036 | Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials (FTC) | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials | 14 Aug 2024 | policy | | fetched
S-D02-037 | Trade Regulation Rule on the Use of Consumer Reviews and Testimonials, 16 CFR Part 465 (Federal Register) | https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials | 22 Aug 2024 | policy | | search only
S-D02-038 | Professional Community Policies, "Do not spam members or the platform" (LinkedIn; does not name bots or automation tools) | https://www.linkedin.com/legal/professional-community-policies | undated | policy | | fetched
S-D02-039 | Sprout Social Q1 2026 Pulse Survey Analysis (PDF unreadable; figures such as 28% unlabelled AI and about 23% engagement bait come from search snippets) | https://media.sproutsocial.com/uploads/2026/03/Sprout-Social-Q1-2026-Pulse-Survey-Analysis.pdf | Mar 2026 | study (vendor) | | search only
S-D02-040 | Meta's AI push has made its way into ad creative. Not all marketers are happy about it (Jasmine Sheena, Marketing Brew) | https://www.marketingbrew.com/stories/2026/04/21/meta-ai-creative-tools-marketer-response | 21 Apr 2026 | press | partly via a brand's Facebook post | fetched
S-D02-041 | What Is an AI UGC Ad? The 2026 Guide (AdMakeAI) | https://admakeai.com/blog/what-is-ai-ugc-ad | 2026 | guide (vendor) | | search only
S-D02-042 | AI UGC Ads 2026: Create Videos Without Hiring Creators (FutureFactors) | https://futurefactors.ai/ai-ugc-ads-2026-guide/ | 2026 | guide (vendor) | | search only
S-D02-043 | AI UGC Ads: The Complete Guide for Marketers in 2026 (Tagshop) | https://tagshop.ai/blog/what-are-ai-ugc-ads/ | 2026 | guide (vendor) | via a Reddit thread (not opened) | search only
S-D02-044 | GenAI ads study 2026 (Taboola press release; sibling ads, over 500 million impressions, own Realize platform; named researcher Oded Netzer, Columbia; raw CTR 0.76% AI vs 0.65% human, "comparable" under strictest controls) | https://www.taboola.com/press-releases/genai-ads-study-2026/ | Jan 2026 | study (vendor) | | fetched
S-D02-045 | Meta Transparency Center, social issue, election and political ads standards | https://transparency.meta.com/policies/ad-standards/SIEP-advertising/SIEP/ | change log 2 Jul 2026 | policy | | fetched
S-D02-046 | Gen AI transparency in Meta's ads products (Meta newsroom; updated 1 Jun 2026) | https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/ | 1 Jun 2026 update | policy | | fetched
S-D02-047 | Does LinkedIn penalize AI content (MagicPost, second article; about -4.1% for "Here's what/how") | https://magicpost.in/blog/does-linkedin-penalize-ai-content | Oct 2026 | study (vendor) | same vendor as S-D02-001 | search only
