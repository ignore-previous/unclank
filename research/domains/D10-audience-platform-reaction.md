# D10 audience-platform-reaction

Platform rules on AI-made content (Steam, itch.io, Kickstarter, Apple, Google Play, art communities) and how audiences react to it (backlash cases, surveys, disclosure effects). This domain covers rules and reactions, not visual tells, so entries use Rule / Applies to / Means for a small creator in place of "Why it reads as AI". For a platform rule, confidence comes from the platform's own page: a fetched primary policy page alone counts as moderate, however many of that platform's pages are cited; a rule known only from press or blogs is anecdotal and flagged; press items repeating one announcement count once. Rounds merged so far: round 1 (breadth, primary pages fetched around 20 Oct 2026), round 2 (depth check, 20 Oct 2026) and round 3 (second depth check, 20 Oct 2026). Round-2 and round-3 fetches went through a summarising fetch tool, so their quotes are marked "fetched (summarised)" in the source list; the lead opened the Apple guidelines and the ArtStation help page directly on 20 Oct 2026, and spot-checked TheGamer's 1666: Amsterdam report and the Waxy.org piece the same day.

## Checklist
- [Avoid · strong] Keep a register of AI-touched assets and audit the build against it before launch, so no placeholder AI art ships (D10-012)
- [Avoid · moderate] Answer Steam's AI content survey for every AI-made asset players see or hear, and keep the answers matching what ships (D10-001)
- [Avoid · moderate] Treat store capsules, key art, cover art and trailers as in scope for AI disclosure; use real-build or human-made art there, or disclose (D10-002)
- [Avoid · moderate] Tag every itch.io asset page that contains generative AI in the AI Disclosure section, or risk delisting (D10-003)
- [Avoid · moderate] On Kickstarter, name the AI tools used, how their output enters the project and which elements they make, and keep the creative work human-led (D10-005)
- [Avoid · moderate] Do not submit any AI-touched art to Lospec's gallery (D10-009)
- [Avoid · moderate] If your app generates content with AI, build filtering, reporting and blocking (guideline 1.2 names AI content creation apps and nonconsensual intimate imagery) and name third-party AI providers before submitting to Apple, and recheck guidelines 1.2 and 2.5.19 on the day you submit (D10-006)
- [Avoid · moderate] If generative AI is central to your Android app, add output safeguards for offensive or deceptive content (D10-008)
- [Avoid · moderate] Tag generative AI in itch.io games in the AI Disclosure section; the rule covers games too, only enforcement is softer (D10-004)
- [Choose deliberately · moderate] Record AI use on covers and cover copy, and disclose it where an award or contract rule applies (D10-015)
- [Choose deliberately · moderate] Before releasing an AI-made ad, check it for uncanny faces, motion and props, and disclose the AI use where audiences may react (D10-014)
- [Choose deliberately · moderate] Label AI work on DeviantArt as "Created using AI tools"; the label is required for anything offered for sale (D10-011)
- [Choose deliberately · moderate] On ArtStation, tag Marketplace content CreatedWithAI, and expect viewers to be able to filter AI work out (D10-018)

## Tells

### Platform rules

### D10-001 Steam: undisclosed AI content that ships with the game
- Label: Avoid
- Confidence: moderate (1 with good data: Valve's own content survey page, fetched twice; press repeats the January 2026 change and counts as the same origin)
- Dated: restructured January 2026 per press (PC Gamer, 16 Jan 2026); Valve's page is undated, fetched 20 Oct 2026
- Rule: Steam's content survey has a "Generative Artificial Intelligence Content" section for content that ships with the game and is consumed by players. It has two categories: Pre-Generated (made with AI tools during development and shipped) and Live-Generated (made with AI while the game runs). Live-generated content needs a description of the guardrails that stop illegal output. The wording that reviewers compare survey answers with the build and store page, and that a game must match its marketing, is not on the fetched page; it comes from Valve's January 2024 wording quoted second-hand by an itch.io post (search only) and from press.
- Applies to: Games released on Steam. Scope is AI output that ships and that players see or hear.
- Means for a small creator: Fill in the AI section honestly, describe the use in the free-text box, and keep the answer in line with the build and the store page. See D10-N01 for the soft exclusion of efficiency tools.
- Fix: Answer truthfully, describe each AI-made asset type, and re-check the survey whenever the build changes.
- Sources: S-D10-001, S-D10-002, S-D10-003, S-D10-004, S-D10-061
- Flag: Round-2 fetch of Valve's page gave no question wording, answer options or free-text prompt, and not the "consistent with marketing" sentence round 1 credited to it. KitGuru (the source of the round-1 question text) did not surface again, so that text stays unverified. The round-1 list of asset types (artwork, sound, narrative, localization) was not re-confirmed in round 2. The January 2026 dating rests on press, not on Valve's page.

### D10-002 Steam: AI-made store-page or marketing art
- Label: Avoid
- Confidence: moderate (2 independent origins, upgraded from anecdotal in round 3: TheGamer's report on 1666: Amsterdam, fetched, where AI marketing assets and cover art drew a fierce reaction; and press on Valve's January 2026 change plus a second-hand 2024 quote, search only, counted as one origin. The reaction is well supported; the claim that Valve's rule covers marketing art is still press only, because Valve's page does not state it.) Lead check 20 Oct (r3): moderate accepted. TheGamer reports AI cover art and the studio names 'external marketing assets', which are marketing art even though the Steam store page isn't named.
- Dated: January 2026 press coverage; 1666: Amsterdam statement reported 10 Jun 2026
- Rule: Press (Game Developer, PC Gamer) reports that Valve's AI section also covers store-page and marketing content, and Valve's January 2024 wording is quoted second-hand as saying a game should match its marketing. Valve's current survey page, as fetched, does not say either.
- Applies to: Steam store pages, capsules, key art, trailers, community assets.
- Means for a small creator: Treat capsules, key art and trailers as in scope. Disclose AI in them, or use human-made or licensed art there, since shoppers see them first. Fetched case: after players found AI in the 1666: Amsterdam prologue demo, Panache Digital Games said early asset versions "made their way into the prologue", covering in-game portraits and marketing assets, and apologised. TheGamer reports the cover art was AI-generated too and the reaction was fierce.
- Fix: Use real-build or human-made art for store assets, or disclose AI-made ones.
- Sources: S-D10-001, S-D10-002, S-D10-003, S-D10-004, S-D10-024, S-D10-060, S-D10-061, S-D10-065, S-D10-075
- Flag: Not stated on Valve's fetched page; coverage of store-page and marketing content is attributed to press and the 2024 post, both secondary and search only. TheGamer (fetched) confirms AI in marketing assets and cover art but does not say the AI art was on the Steam store page or capsule. Players' claim that the Steam page had no AI disclosure at demo time is search only (GamerMarkt, 1vX.gg, second-hand) and the live store page was not checked. TechPowerUp returned 403. The moderate rating is a judgement call for the lead.

### D10-003 itch.io: untagged generative AI on an asset page
- Label: Avoid
- Confidence: moderate (1 with good data: itch.io's quality guidelines, fetched; two secondary items search only)
- Dated: disclosure field added November 2024 per press (search only); guidelines page undated, fetched
- Rule: Every project with generative AI material should be tagged in the AI Disclosure section. Asset pages are strictly enforced, and an untagged asset page may be delisted. Mass-produced AI pages count as spam.
- Applies to: itch.io asset packs and asset pages. Spam rule applies to any page.
- Means for a small creator: If you sell or give away assets that contain any AI output, tag the page, even after hand edits. Asset buyers filter on this tag.
- Fix: Tag the page in the AI Disclosure section of the edit page; do not mass-produce AI listings.
- Sources: S-D10-005, S-D10-006, S-D10-007
- Flag: The November 2024 date and the forum and PC Gamer items are search only.

### D10-004 itch.io: generative AI in a game
- Label: Avoid (lead review 20 Oct: itch.io's own guidelines ask every project with generative AI material to be tagged; the grace period for games only delays enforcement, it does not waive the rule)
- Confidence: moderate (1 with good data: itch.io's quality guidelines, fetched)
- Dated: guidelines page undated, fetched
- Rule: Games with generative AI material should also be tagged, but games have a grace period and the page states no penalty. Tagged projects appear on the AI Assisted browse page.
- Applies to: itch.io games (not asset pages; see D10-003).
- Means for a small creator: Tagging is expected and carries no stated penalty. It also places the game where AI-filtering players can find or skip it. Procedural generation, pathfinding and dynamic music are exempt (D10-N02).
- Fix: Tag it accurately and accept being listed as AI-assisted.
- Sources: S-D10-005, S-D10-008
- Flag: A forum complaint that the tag cannot separate light from heavy AI use is search only.

### D10-005 Kickstarter: undisclosed or mostly-AI projects
- Label: Avoid
- Confidence: moderate (1 with good data: Kickstarter's own pages, the help article fetched and the updates post fetched (summarised); both are one origin; later rule changes are search only)
- Dated: policy effective 29 Aug 2023 per the updates post, which the fetch summary dates 12 Jun 2024; a rules update on 12 May 2026 comes from secondary coverage (search only); help article undated, fetched
- Rule: Kickstarter conditionally allows AI. Creators using AI tools state what AI technology they plan to use, how the output enters the project and which elements AI will make, and the creative work must come from humans. Projects that build AI tools must say whether the database's host or provider obtained consent; without consent safeguards Kickstarter is "unlikely to allow" the project. All other platform rules still apply. Round 1 also records that Trust & Safety reviews the answers and approved answers are published on the project page.
- Applies to: Kickstarter campaigns that use or build AI.
- Means for a small creator: Add a clear AI section naming the tool, what it made and which parts a human made. An undisclosed AI-made sample or reward reads as deception to backers.
- Fix: Put the AI section on the page before launch.
- Sources: S-D10-009, S-D10-010, S-D10-011, S-D10-012
- Flag: The "Trust & Safety reviews" and "published on the project page" points come from the round-1 help-article read and were not found in the round-2 fetch of the updates post. The "may be suspended" wording and the 2026 "little or no human creation" rule come from a search summary and Graphic Policy (search only). kickstarter.com/rules and the creator FAQ returned 403, so were not opened. Approval is judgement-based.

### D10-006 Apple: AI content creation apps without safeguards
- Label: Avoid
- Confidence: moderate (1 with good data: Apple's App Review Guidelines, fetched by the lead and by the gatherer)
- Dated: guideline text fetched 20 Oct 2026; the footer shows "Last Updated: October 16, 2026"
- Rule: Guideline 1.2 (User-Generated Content) lists intellectual property infringement, nonconsensual intimate imagery and anonymous bullying among the challenges of apps where users create or share content, and says this includes AI content creation apps beside social media and user-generated content platforms. Such apps need filtering of objectionable material, reporting with timely response, blocking of abusive users and published contact information. Guideline 5.1.2(i) covers sharing personal data, "including with third-party AI", and requires explicit permission before doing so. Guideline 2.5.19 on the live page is the rule against hidden, dormant or undocumented features.
- Applies to: iOS apps that generate content with AI or send user data to an AI provider.
- Means for a small creator: Only matters if you ship an app with generative features. Build moderation and reporting first, and name the AI provider in the privacy disclosure.
- Fix: Add the 1.2 safeguards and the 5.1.2(i) permission prompt before submission, and reread 1.2 and 2.5.19 on the day you submit.
- Sources: S-D10-013, S-D10-014, S-D10-055, S-D10-076, S-D10-077
- Flag: PARTLY RESOLVED (lead check 20 Oct 2026). Guideline 1.2 on the live page now names nonconsensual intimate imagery in the same paragraph as AI content creation apps, so the press claim about a 1.2 line is partly on the page, though not as an AI-specific sentence. The press claim about a new 2.5.19 "bait-and-switch" rule is still NOT on the page: 2.5.19 as fetched is the hidden, dormant or undocumented features rule, which this entry already said. The gatherer's round-3 "correction" only restated that text, so it changes nothing. Whether that rule moved to 2.5.19 in the 16 Oct update (press says from 2.3.1) is unverified; Apple's changelog (appstorereviewguidelineshistory.com) and the developer news post of 16 Oct were not opened. The press (9to5Mac, AppleInsider, TUAW, ppc.land, an AGTP post on X; one announcement counted once, all search only) dates from 16 to 19 Oct 2026. The gatherer's round-3 fetch read the whole page in two parts and found no further AI-specific guideline.

### D10-007 Apple: AI-made screenshots that misrepresent the app
- Label: Avoid
- Confidence: anecdotal (one developer blog, second-hand, search only; Apple's own rule is real but not AI-specific)
- Dated: noted from July 2026
- Rule: Apple's fetched guideline text has no AI-specific rule for screenshots. Its guideline 2.3.3 page (fetched, summarised) says screenshots should show the app in use and not merely title art, and that Apple approves a submission only where more than half of the screenshots show the app in use; the rest may use marketing material. Its general metadata-accuracy and misleading-marketing rules also apply, so a screenshot showing something the app cannot do risks rejection.
- Applies to: App Store screenshots and previews.
- Means for a small creator: Show the real build. AI in framing or background around real UI is a lesser concern (D10-N04). The only AI-specific reading is from a blog.
- Fix: Check every screenshot against the binary.
- Sources: S-D10-013, S-D10-015, S-D10-066, S-D10-078
- Flag: Only the blog (Storeboard, search only) ties this to AI; Apple's pages do not. Clause 2.3.3 is now confirmed on Apple's help page, so the earlier clause-number mismatch is settled. No first-hand report of an AI-screenshot rejection was found (Apple forums and Reddit were not reachable). The appsubmitter.io guide is a vendor page, search only, and not AI-specific.

### D10-008 Google Play: generative AI apps that produce offensive or deceptive output
- Label: Avoid
- Confidence: moderate (1 with good data: Google Play Console Help policy page, fetched)
- Dated: fetched 20 Oct 2026; page shows no effective date
- Rule: Developers are responsible for ensuring that their generative AI apps do not generate offensive content, including deceptive output and sexual deepfakes. The policy covers apps where AI is a central feature, such as chatbots.
- Applies to: Android apps whose main feature is generative AI.
- Means for a small creator: Matters only if you ship such an app. Add output filters, abuse reporting and clear enforcement before launch.
- Fix: Add safeguards on generated output before submission.
- Sources: S-D10-016
- Flag: Third-party blogs claim a visible AI-generated label, a Play Console declaration and a 15 April 2026 enforcement date. Google's fetched page mentions none of these, so treat them as unverified and do not rely on them.

### D10-009 Lospec gallery: any AI in the process
- Label: Avoid
- Confidence: moderate (1 with good data: Lospec's own announcement article, fetched by the lead)
- Dated: article dated 12 Jun 2023
- Rule: Lospec's gallery no longer accepts art with AI anywhere in its process. A search snippet of the submit page lists "No AI Generated Art" as rule 4 of six and says art made with AI in its process is not allowed.
- Applies to: Lospec gallery submissions (pixel art).
- Means for a small creator: Do not post AI-touched work there; post it elsewhere, labelled.
- Fix: Keep AI-assisted pieces off the gallery.
- Sources: S-D10-017, S-D10-018
- Flag: The submit page itself was not opened in either round (search snippet only). The lead fetched the article.

### D10-010 Art communities that ban AI output (Newgrounds, Fur Affinity and others)
- Label: Avoid
- Confidence: anecdotal (2022 reporting, fetched, plus search-only lists; the platforms' current rule pages were not opened, and under this domain's rule a policy known only from press stays anecdotal)
- Dated: rules announced Aug to Sep 2022 (Waxy.org 9 Sep 2022; Fur Affinity ban reported 14 Sep 2022); current text unverified
- Rule: Waxy.org (Andy Baio, 9 Sep 2022, fetched) reports Newgrounds' rule as "AI-generated art is not allowed in the Art Portal". The exception: character art with an AI-generated background is acceptable if the AI elements are noted, and tracing over AI art belongs on your blog. Waxy quotes Fur Affinity as "Content created by artificial intelligence is not allowed on Fur Affinity", with no exception mentioned. Dogpatch (14 Sep 2022, fetched, opinion) reports the Fur Affinity ban but has no policy text. Search only: a later Fur Affinity section 2.13 that names paint-overs and backgrounds (AlternativeTo list), and archived copies of both rule pages dated 4 Jun 2025 that were seen in search but not opened.
- Applies to: Newgrounds, Fur Affinity and similar handmade-art communities.
- Means for a small creator: Read each site's current rules before posting AI-assisted work. Newgrounds allows a noted AI background on character art, per the 2022 report. Community lists are advocacy-minded.
- Fix: Post AI-assisted work only where the current rules allow it, and note any AI elements.
- Sources: S-D10-019, S-D10-020, S-D10-021, S-D10-047, S-D10-059, S-D10-064, S-D10-070, S-D10-071, S-D10-072, S-D10-073, S-D10-074
- Flag: This is 2022 reporting; the current rule texts are unverified. Newgrounds' Art Guidelines page returned 403, the Fur Affinity policy page returned 403 and the Fur Affinity upload policy was not attempted. Waxy likely repeats the official Newgrounds page, so the Newgrounds rule has one origin. The Fur Affinity section 2.13 wording is search only and may not match the live page. A Flayrah commenter said the 2022 wording left AI backgrounds unclear (search only). The secondary lists may repeat one another.

### D10-011 DeviantArt: AI work without the "Created using AI tools" label
- Label: Choose deliberately
- Confidence: moderate (1 with good data: DeviantArt's own Terms of Service section 31 and its Team journal post, both fetched (summarised) and counted as one origin; upgraded from anecdotal in round 2)
- Dated: label announced 12 Jun 2023 and updated 19 Jul 2023; Terms of Service section 31 undated in the fetched text
- Rule: DeviantArt's Terms of Service (section 31) say content offered for sale (Premium Downloads, Premium Galleries, Subscriptions, Exclusives, Arts & Crafts, Merch, Originals) that was made with generative AI must be clearly tagged "Created using AI tools". For content not for sale the terms only recommend the label. The creator is solely responsible for complying. The 2023 journal post said all AI-made submissions would need the label and that, from 19 Jul 2023, the label is applied automatically only where an image's metadata shows AI.
- Applies to: DeviantArt uploads, strictest for anything offered for sale.
- Means for a small creator: Label honestly; the label is mandatory for sale items and sensible elsewhere. Untagged AI work that is found later reads as a trust breach.
- Fix: Use the label on every AI-touched piece, and always on items for sale.
- Sources: S-D10-048, S-D10-049, S-D10-050, S-D10-019
- Flag: The Help Center page (S-D10-050) was truncated before any rule text. The Terms' effective date was not in the fetched text, and the 2023 journal (all AI submissions) is broader than the current Terms (required for sale only), so the journal may be superseded. Round 1's "automatic from 19 Jul 2023" overstated it, as the automatic label depends on metadata.

### D10-018 ArtStation: AI work and the CreatedWithAI tag
- Label: Choose deliberately
- Confidence: moderate (1 with good data: ArtStation's help article "Use of AI software on ArtStation", fetched by the lead and by the gatherer; the Terms of Service are search only)
- Dated: help article dated 2 Sep 2026, fetched 20 Oct 2026
- Rule: ArtStation permits AI-assisted work, and viewers can use filters to hide AI work. The CreatedWithAI tag is required only for content distributed through the ArtStation Marketplace, and products that break the terms may be delisted. NoAI is NOT applied by default (lead check of the help page). Users should post only work they own or have permission to share.
- Applies to: ArtStation portfolio posts and Marketplace products.
- Means for a small creator: Tag Marketplace products CreatedWithAI. For portfolio posts, tag voluntarily where the Terms may expect it, and expect some viewers to filter the work out.
- Fix: Add the CreatedWithAI tag to Marketplace content and any AI-touched portfolio piece.
- Sources: S-D10-051, S-D10-052, S-D10-022
- Flag: A search summary claims ArtStation made NoAI the default for new projects and existing uploads on 2 Sep 2026; the help page contradicts it, so that claim is wrong. The Terms of Service (search summary, section 46; page 403) say any content made with generative AI must be tagged CreatedWithAI, which is broader than the help page's Marketplace-only rule; the scope for portfolio posts is unresolved. The crawler-blocking claim and the homepage filtering claim (80.lv, search only, date not recovered) were not confirmed.

### Audience reactions

### D10-012 Shipped AI placeholders found by players
- Label: Avoid
- Confidence: strong (3 independent cases from 3 non-vendor outlets, all now fetched: Engadget on Crimson Desert, Game Developer on Jurassic World Evolution 3, TheGamer on 1666: Amsterdam). Lead review 20 Oct (r2): strong accepted, on condition that the 1666 case could be fetched. Round 3 met that condition, so the earlier downgrade risk is cleared.
- Dated: Jurassic World Evolution 3, June 2025; Crimson Desert, March 2026; 1666: Amsterdam, prologue demo 5 Jun 2026, studio statement reported 10 Jun 2026, Early Access listed for 25 Aug 2026
- Why it matters: Blatant AI art next to human art stands out, and "we forgot to replace it" reads as indifference. Reported cases: Pearl Abyss apologised for AI-made 2D props in Crimson Desert, saying experimental AI tools were "unintentionally included in the final release" and promising an audit; Frontier removed AI scientist portraits from Jurassic World Evolution 3 after fan complaints (Game Developer, 25 Jun 2025); players found AI assets in the 1666: Amsterdam demo, and Panache Digital Games apologised, said early asset versions "made their way into the prologue" (in-game portraits and marketing assets), PROMISED removal in a demo update, and said Early Access and the full game "will not include any assets generated by AI" (TheGamer, 10 Jun 2026, fetched). TheGamer reports no removal. Engadget also cites Sandfall (Clair Obscur) losing Indie Game Awards honours over AI placeholder textures, an unchecked mention.
- Fix: Keep a register of every AI-touched asset with a replacement plan, and audit the build against it before launch.
- Sources: S-D10-023, S-D10-056, S-D10-060, S-D10-024, S-D10-075
- Flag: For 1666: Amsterdam the fetched source supports a promise of removal, not a removal; earlier rounds wrote "removed", which was wrong. That the AI was removed from Early Access is search only: a Panache co-founder quoted in an interview as saying it was "totally removed" (via PC Gamer and TechPowerUp summaries), a studio post on X promising human-made versions in an update (search summaries), and the TechPowerUp and 1vX.gg headlines. The co-founder's remark may mean pre-production only. No patch notes were found. Counter-evidence: Crimson Desert sold strongly after the controversy (Circana's Piscatella, via GameSpot), so backlash did not always cost sales. The Goodreads source used in round 1 is superseded by Game Developer.

### D10-013 AI images in a trailer or showcase
- Label: Avoid
- Confidence: anecdotal (one case, one fetched secondary write-up plus a search-only post)
- Dated: September 2026
- Why it matters: Trailers are the most visible footage and fans check them frame by frame. In the reported Level-5 case (Professor Layton remake, Yo-Kai Watch 2 and DecaPolice named), CEO Akihiro Hino called it "experimentation with the latest technology", said the company made "extensive use of AI this time", and said released games contain nothing simply generated by AI. His comment about cutting development from five years to two is a separate statement, not the reason he gave for the experiment.
- Fix: Use footage from the real build, and label any AI-made still.
- Sources: S-D10-027, S-D10-028
- Flag: One case. Dynasage (fetched, 14 Sep 2026) is itself a republication of an IGN India piece that was not opened, and the CEO's X post was not seen. The Threads post is search only. Round 1 merged two statements into one; corrected here. Whether the AI assets appeared in a trailer or showcase was not re-confirmed in round 2.

### D10-014 AI-made ads and campaigns
- Label: Choose deliberately
- Confidence: moderate (upgraded from anecdotal in round 3, a judgement call: 2 independent cases. McDonald's Netherlands is documented by NBC News and TODAY, fetched, counted as one origin because TODAY is NBC-owned, plus a TechRadar report, search only. Coca-Cola's 2025 ad rests on search-only items and a weak figure, so the rating leans on the McDonald's case.) Lead check 20 Oct (r3): moderate accepted at the minimum. One fetched origin (McDonald's, NBC/TODAY), with TechRadar and Coca-Cola search only. It drops to anecdotal if no second origin is fetched.
- Dated: McDonald's Netherlands, posted 6 Dec 2025 and pulled by about 10 Dec; Coca-Cola, 2024 and 2025 (sentiment figure Nov 2025)
- Why it matters: Named viewers called the McDonald's Netherlands AI Christmas ad "unsettling", "creepy" and "inauthentic" (NBC News, 11 Dec 2025), and the brand pulled the 45-second spot within days. The word "soulless" comes from TechRadar's headline, not from NBC. For Coca-Cola's 2025 AI ad, one social-listening figure (Sprout Social data via Campaign) puts sentiment at 37% positive, against 83% for John Lewis in the same period; there is no baseline, so a fall in sentiment is not shown. Coca-Cola says its 2024 campaign did well in private testing (search summary only). Survey data is mixed: one figure puts the share who dislike an ad more when told AI made it at 24.7%, and in another study only 13% of viewers of an AI ad were confident it was AI.
- Fix: Disclose AI use where it matters, and check how the ad reads on a phone with the sound off.
- Sources: S-D10-029, S-D10-030, S-D10-031, S-D10-032, S-D10-067, S-D10-068, S-D10-069, S-D10-079
- Flag: The McDonald's claims are now fetched (NBC News and TODAY, both summarised). Coca-Cola, TechRadar and the survey items are search only. The round-2 TechRadar fetch was cut off before the article body, so its claim rests on the headline. Ruminatex is a vendor guide citing an unopened tracker. The EMARKETER figure and the 24.7% and 13% survey figures were not confirmed. The Ipsos/Newhouse and Gartner figures come second-hand via one roundup. The earlier line that Coca-Cola sentiment "fell" is withdrawn.

### D10-015 AI covers and cover copy in publishing
- Label: Choose deliberately
- Confidence: moderate (two independent cases: The Spinoff on the New Zealand awards, fetched; Gizmodo reporting Wired, search only and anonymous-sourced)
- Dated: New Zealand awards November 2025; Wired report October 2026; Shy Girl March 2026
- Why it matters: A covers-first medium makes an uncredited AI cover read as a shortcut. The Ockham New Zealand Book Awards Trust disqualified two titles from 2026 contention over AI covers; the AI clause was in the entry pack that opened 7 Aug, and enforcement relies on submitters confirming with authors and designers. Large publishers were reported to use AI for covers and jacket copy, mostly without telling authors. Related but about text: Hachette dropped the planned 2026 US release of Shy Girl and pulled the UK edition in March 2026 after accusations of AI-written text, which the author denies, saying a freelance editor added AI material.
- Fix: Record AI use per asset, and disclose it to an awards body or author where a rule applies. Label unsure: Avoid where a contract or awards rule applies, Choose deliberately otherwise.
- Sources: S-D10-033, S-D10-034, S-D10-035
- Flag: The Gizmodo item is search only and second-hand to Wired through anonymous sources. Shy Girl concerns AI-written text, not covers; its detector evidence is contested (a 3 Apr 2026 WSJ op-ed questions the Pangram report, which used a pirated copy), and the facts come from Wikipedia (fetched, reference). The trust's own explanation was not quoted. No reader survey on AI covers was found, and some critics call the outrage out of proportion.

### D10-016 Disclosing AI use lowers trust
- Label: Choose deliberately
- Confidence: anecdotal (lead review 20 Oct: downgraded from moderate; the two items are search only, and one is a working paper that has not been peer-reviewed.)
- Dated: 2025 studies
- Why it matters: A study across 13 experiments (Schilke and Reimann, 2025) found disclosed AI use lowers trust, including on creative tasks. Music studies found listeners engage less with music labelled AI even when a human made it. A separate arXiv study found labels lower perceived accuracy but have limited wider effects, and one study found AI-assisted labels rated better than fully AI-generated ones.
- Fix: Disclose where a platform requires it, and say what a human did. Weigh the trust cost when deciding whether to use AI at all.
- Sources: S-D10-043, S-D10-044, S-D10-045, S-D10-039
- Flag: All search only. The music result includes a non-peer-reviewed working paper. The MDPI study date was not recovered. Round 2 did not recheck these.

### D10-017 Human-made work flagged as AI
- Label: Choose deliberately
- Confidence: anecdotal (one case, two outlets)
- Dated: event December 2022, reported January 2023
- Why it matters: A human artist was banned from an art subreddit after moderators judged the piece AI-made and rejected the artist's account, even though the artist offered the layered file. Painterly or glossy styles can be misread.
- Fix: Keep layered project files and work-in-progress shots. Do not alter good work only to avoid a false flag.
- Sources: S-D10-036, S-D10-037
- Flag: One 2022 case, not a platform-wide rule. Both items search only (PC Gamer and Artnet returned 403 in round 2). The subreddit's name (round 1 said r/Art) is not confirmed; search headlines say only "art subreddit".

### D10-019 AI disclosure added only after players find the AI
- Label: Avoid
- Confidence: anecdotal (one clear case in a fetched outlet; a second case in the same study set contradicts the pattern; a third case, 1666: Amsterdam, fits only partly)
- Dated: Crimson Desert, March 2026; 1666: Amsterdam, June 2026; Frontier, June 2025 (counter-case)
- Why it matters: When a studio adds an AI note to its store page or announces removal only after players spot the AI, it looks like a shortcut taken and then covered, not a planned choice. Engadget reports Crimson Desert's Steam page now carries a disclosure saying generative AI was "used in a supplementary capacity" for some 2D props, after players raised the art.
- Fix: Write the disclosure before launch, state what is AI-made and what will be replaced, and make the store page match the build.
- Sources: S-D10-023, S-D10-056, S-D10-060, S-D10-065, S-D10-075
- Flag: Engadget does not date the Steam disclosure, so "added only after" is an inference. Round 3 adds a second case: in 1666: Amsterdam the studio admitted the AI and apologised only after players found it, and TheGamer (fetched) says the reply did little to reassure the community; the claim that its Steam page had no AI disclosure at demo time is search only. Kept anecdotal because both cases rest partly on inference or search-only reports. Counter-evidence: Frontier's disclaimer was on the Steam page before the Jurassic World Evolution 3 backlash, so a disclosure alone did not stop complaints; removal followed. Overlaps D10-012, and may be better read as part of it.

## Belief test: are game audiences the most hostile?
- No study compares audiences on one question, so "most hostile" cannot be confirmed or refuted from these sources. Round 2 checked Quantic Foundry (gamers only), Circana PlayerPulse (US players only), GameDiscoverCo (Steam fans only) and GDC (industry professionals only); none asks two audiences the same question.
- For: Quantic Foundry's survey (N=1,799, run Oct to Dec 2025, core-skewed sample) found 85% negative and 63% in the most negative option on gen AI in games. Round 2 confirmed N, 85% and 63% in a fetched secondary write-up (S-D10-046, Gamesmarket, 22 Dec 2025); the original post returned 403 in both rounds, and the question wording is still unknown. The write-up says the survey asked about AI-generated quests and dialogue, which Yee says came from a 2024 survey. GDC's 2026 State of the Industry (more than 2,300 professionals) reports 52% think gen AI is having a negative impact, and 36% use gen AI tools (S-D10-053 on GDC's own site, fetched; S-D10-054 Game Developer, fetched), but that measures developers, not players. Search-only per-discipline figures from a secondary summary (visual and technical art 64% negative, design and narrative 63%, programming 59%, executives 19% positive) are the closest same-question comparison found, and sit inside the industry. Backlash cases in games are frequent (D10-012, D10-013).
- Against: Circana's December 2025 US tracker found most players neutral or unsure, with just over 25% less likely to buy (S-D10-057, fetched syndication; S-D10-026, S-D10-038, search only). GameDiscoverCo's Steam-fan survey (about 3,800 respondents, 25 Jun to 2 Jul 2026) found about 43% fine with AI, 26% neutral and about 31% negative, with 8% saying they would not buy (S-D10-058, fetched, secondary). The same Quantic survey found 79% negative on blockchain games in 2024 (search only), so high hostility is not unique to AI.
- Spread inside games: samples and measures differ widely (85% negative among Quantic's core-skewed sample against about 31% among Steam fans), so "game audiences" is not one group.
- Other fields show comparable reaction: ads (S-D10-029, S-D10-031, S-D10-032, S-D10-067), music (S-D10-043), disclosure trust studies across tasks (S-D10-044), and publishing cases (S-D10-033). Their measures differ, so no ranking follows.
- Verdict: not supported as stated; games show visible backlash and a hostile core, while the broader player base looks mostly neutral to mixed.

## Not a tell

### D10-N01 AI development and efficiency tools on Steam
- Why it is fine: Valve's survey is about AI content that ships with the game and that players experience. Efficiency tools are "not the focus of this section", which is a soft exclusion and not a formal exemption. Anything players see or hear still needs disclosure.
- Sources: S-D10-001, S-D10-002

### D10-N02 Procedural generation, pathfinding and dynamic music on itch.io
- Why it is fine: itch.io exempts self-contained algorithms without large external datasets, with NPC pathfinding, procedural levels and dynamic music as its examples. These are standard game techniques, not generative AI.
- Sources: S-D10-005

### D10-N03 Disclosed AI assistance
- Why it is fine: Platforms accept AI when it is disclosed. Kickstarter takes disclosure of tool and extent, itch.io lists disclosed projects on an AI Assisted page, ArtStation permits AI work with filters for viewers, and one study rated AI-assisted reviews above fully AI-generated ones. Disclosure may still cost some trust (D10-016) and does not stop backlash against visible AI (D10-012).
- Sources: S-D10-009, S-D10-005, S-D10-039, S-D10-051

### D10-N04 Real app UI in listing marketing
- Why it is fine: Apple's guideline 2.3.3 help page (fetched, summarised) lets screenshots beyond the first half use marketing material, as long as more than half show the app in use. Marketing images built around the real interface therefore stay compliant; only images showing something the app cannot do are the problem. The page does not mention AI, so applying it to AI-made framing is our reading, and the AI-specific concern in D10-007 still rests on a blog.
- Sources: S-D10-015, S-D10-066

### D10-N05 Google Play: summarising and AI-enhanced features
- Why it is fine: Google's policy page says apps whose only feature is summarising content not made by AI are not covered at this time, and that productivity apps using AI to enhance an existing feature are not covered. Other Play policies still apply.
- Sources: S-D10-016

### D10-N06 Most players are neutral about gen AI in games
- Why it is fine: Circana's tracker found most US players neutral or unsure, and a vocal minority against. The refuse-or-less-likely share rose from about 22% in March 2024 to over 25% in December 2025, so sentiment is worsening. GameDiscoverCo's Steam-fan survey found about 43% fine with AI and about 31% negative, which fits "mixed, not uniformly hostile".
- Sources: S-D10-057, S-D10-026, S-D10-038, S-D10-058

### D10-N07 Behind-the-scenes AI (programming help, difficulty tuning)
- Why it is fine: Audience objection follows what players see or hear, not AI use as such. GameDiscoverCo's Steam-fan survey found players most accepting of AI in programming and technical development, and the Quantic write-up says players were more open to AI for dynamic difficulty adjustment. Counter-evidence: about 51% accept AI for some uses but not others, and only 17% believe developers fully disclose AI-made audiovisual content, so trust in disclosure is low. Platform disclosure still applies to anything players see or hear (D10-N01).
- Sources: S-D10-058, S-D10-046

## Sources
S-D10-001 | Steamworks Content Survey | https://partner.steamgames.com/doc/gettingstarted/contentsurvey | undated | policy | - | fetched (also fetched by the lead; round-2 fetch gave no question wording)
S-D10-002 | Steam updates AI disclosure form to specify it's focused on AI content consumed by players (PC Gamer) | https://www.pcgamer.com/software/ai/steam-updates-ai-disclosure-form-to-specify-that-its-focused-on-ai-generated-content-that-is-consumed-by-players-not-efficiency-tools-used-behind-the-scenes/ | 16 Jan 2026 | press | - | search only
S-D10-003 | Valve tweaks and clarifies AI disclosure rules for Steam (Game Developer) | https://www.gamedeveloper.com/business/valve-tweaks-and-clarifies-ai-disclosure-rules-for-steam | Jan 2026 | press | - | search only
S-D10-004 | Steam updates its gen AI disclosure policies (KitGuru) | https://www.kitguru.net/desktop-pc/mustafa-mahmoud/steam-updates-its-gen-ai-disclosure-policies/ | Jan 2026 | press | - | search only (did not resurface in round 2)
S-D10-005 | itch.io quality guidelines | https://itch.io/docs/creators/quality-guidelines | undated | policy | - | fetched (also fetched by the lead)
S-D10-006 | Generative AI disclosure tagging (itch.io forum) | https://itch.io/t/4309690/generative-ai-disclosure-tagging | 2024 | forum | - | search only
S-D10-007 | Itch.io now requires asset creators to disclose use of generative AI (PC Gamer) | https://www.pcgamer.com/software/platforms/indie-distribution-platform-itch-io-now-requires-asset-creators-to-disclose-the-use-of-generative-ai-in-their-work/ | 2024 | press | - | search only
S-D10-008 | AI generated vs AI assisted, where's the line (itch.io forum) | https://itch.io/t/4741212/ai-generated-vs-ai-assisted-wheres-the-lines | date not recovered | forum | - | search only
S-D10-009 | Can I use AI-generated content or create AI technology in my project? (Kickstarter help) | https://help.kickstarter.com/hc/en-us/articles/16848396410267-Can-I-use-AI-generated-content-or-create-AI-technology-in-my-project | undated | guide | - | fetched
S-D10-010 | Kickstarter project guidelines for AI-generated content and AI technology | https://updates.kickstarter.com/kickstarter-project-guidelines-for-ai-generated-content-and-ai-technology/ | 12 Jun 2024 per fetch summary (policy effective 29 Aug 2023) | guide | - | fetched (summarised, round 2)
S-D10-011 | Kickstarter unveils generative AI policy (Steampunk Explorer) | https://steampunk-explorer.com/news/kickstarter-unveils-generative-ai-policy-full-disclosure-key | 29 Aug 2023 | press | - | search only
S-D10-012 | Kickstarter attacks adult comics while updating its rules (Graphic Policy) | https://graphicpolicy.com/2026/05/14/kickstarter-attacks-adult-comics-while-updating-its-rules/ | 14 May 2026 | press | secondary summary of the rules page | search only
S-D10-013 | App Review Guidelines (Apple) | https://developer.apple.com/app-store/review/guidelines/ | footer "Last Updated: October 16, 2026" per gatherer's fetch | policy | - | fetched (by the lead 20 Oct 2026 and by the gatherer; round 3 read it in two parts)
S-D10-014 | Generative AI porn apps targeted in App Review Guidelines update (AppleInsider) | https://appleinsider.com/articles/26/10/17/generative-ai-porn-apps-targeted-in-app-review-guidelines-update | 17 Oct 2026 | press | - | search only (describes wording only partly on the fetched page; see D10-006)
S-D10-015 | Apple guideline 2.3.3 screenshots (Storeboard) | https://storeboard.dev/blog/apple-guideline-2-3-3-screenshots | 7 Jul 2026 | blog | second-hand reading of Apple's rule | search only
S-D10-016 | Understanding Google Play's AI-Generated Content policy (Google Play Console Help) | https://support.google.com/googleplay/android-developer/answer/14094294 | undated | policy | - | fetched
S-D10-017 | Lospec Will No Longer Be Accepting AI Related Art Submissions (Lospec) | https://lospec.com/articles/lospec-will-no-longer-be-accepting-ai-related-art-submissions | 12 Jun 2023 | policy | - | fetched (by the lead)
S-D10-018 | Lospec gallery submit page | https://lospec.com/gallery/submit | undated | policy | - | search only (snippet; not opened)
S-D10-019 | Sites That Restrict/Ban AI Art (DeviantArt journal) | https://www.deviantart.com/evil0verlady/journal/Sites-That-Restrict-Ban-AI-Art-937239233 | date not recovered | forum | second-hand list | search only
S-D10-020 | List of sites banning AI art (TechCrunch) | https://techcrunch.com/?p=2439231 | 2022 | press | second-hand | search only
S-D10-021 | Art websites that ban AI (Brush Warriors) | https://brushwarriors.com/art-websites-that-ban-ai/ | date not recovered | guide | - | search only
S-D10-022 | ArtStation will block AI crawlers from scraping artists' work (80.lv) | https://80.lv/articles/artstation-will-block-ai-crawlers-from-scraping-artists-work | date not recovered | press | - | search only
S-D10-023 | Crimson Desert developer apologizes and promises to replace AI-generated art (Engadget) | https://www.engadget.com/gaming/crimson-desert-developer-apologizes-and-promises-to-replace-ai-generated-art-183716439.html | 22 Mar 2026 | press | - | fetched (summarised, round 2)
S-D10-024 | 1666 Amsterdam developer drops gen AI art after community backlash (TechPowerUp) | https://www.techpowerup.com/352122/1666-amsterdam-developer-drops-gen-ai-art-after-community-backlash | 2026 | press | - | search only (403 in round 2)
S-D10-025 | Jurassic World Evolution 3 removes generative AI from game after fan backlash (Goodreads author blog) | https://www.goodreads.com/author_blog_posts/25869553-jurassic-world-evolution-3-removes-generative-ai-from-game-after-fan-bac | 2025 | blog | - | search only (superseded by S-D10-056; no longer cited)
S-D10-026 | GenAI in games: most players just don't care, study finds (GameSpot) | https://www.gamespot.com/articles/genai-in-games-most-players-just-dont-care-study-finds/1100-6538972/ | 24 Mar 2026 | press | reports Circana PlayerPulse | search only (403 in round 2; text read via S-D10-057)
S-D10-027 | Level-5 boss addresses AI backlash (Dynasage blog) | https://blog.dynasage.com/2026/09/level-5-boss-addresses-ai-backlash.html | 14 Sep 2026 | blog | secondary write-up; republishes an IGN India piece not opened | fetched (summarised, round 2)
S-D10-028 | Level-5 backlash over generative AI assets (Threads post) | https://www.threads.com/@thedynasage/post/DdTWLrQm7jK/level-faced-major-backlash-after-fans-spotted-generative-ai-assets-in-new-game | date not recovered | forum | - | search only
S-D10-029 | McDonald's pulls AI-generated Christmas ad after backlash (TechRadar) | https://www.techradar.com/ai-platforms-assistants/mcdonalds-pulls-ai-generated-christmas-ad-after-backlash-over-soulless-visuals-and-holiday-chaos | Dec 2025 | press | - | search only (round-2 fetch cut off before the article body; the "soulless" wording is from its headline)
S-D10-030 | Brands using AI commercials (Ruminatex) | https://www.ruminatex.com/guides/brands-using-ai-commercials | 2025 | guide | cites an unopened sentiment tracker | search only
S-D10-031 | 5 of the most controversial campaigns of 2025 (EMARKETER) | https://www.emarketer.com/content/5-of-most-controversial-campaigns-of-2025- | Mar 2025 | press | - | search only
S-D10-032 | AI slop backlash 2026 (Grey Journal) | https://greyjournal.net/hustle/grow/ai-slop-backlash-2026/ | May 2026 | press | roundup quoting Ipsos/Newhouse and Gartner | search only
S-D10-033 | How two AI book covers forced the publishing industry to reckon with its future (The Spinoff) | https://thespinoff.co.nz/culture/20-11-2025/how-two-ai-book-covers-forced-the-publishing-industry-to-reckon-with-its-future | 20 Nov 2025 | press | - | fetched (summarised, round 2)
S-D10-034 | Major publishers reportedly cover their books in AI (Gizmodo) | https://gizmodo.com/as-they-supposedly-battle-ai-slop-major-publishers-reportedly-cover-their-books-in-it-2000824603 | 10 Oct 2026 | press | second-hand to Wired, anonymous sources | search only
S-D10-035 | Shy Girl (Wikipedia) | https://en.wikipedia.org/wiki/Shy_Girl | Mar 2026 | reference | - | fetched (summarised, round 2)
S-D10-036 | Artist banned from art subreddit because their work looked AI-generated (PC Gamer) | https://www.pcgamer.com/artist-banned-from-art-subreddit-because-their-work-looked-ai-generated/ | 8 Jan 2023 | press | - | search only (403 in round 2)
S-D10-037 | Artist Ben Moran banned from subreddit over AI suspicion (Artnet) | https://news.artnet.com/art-world/artist-ben-moran-banned-from-subreddit-ai-art-2240795 | Dec 2022 | press | - | search only (403 in round 2)
S-D10-038 | Mat Piscatella post on gen AI sentiment (Bluesky) | https://bsky.app/profile/matpiscatella.bsky.social/post/3mgfz5whvhs26 | date not recovered | forum | quote from a search summary | search only
S-D10-039 | AI-assisted vs AI-generated reviews (MDPI) | https://www.mdpi.com/0718-1876/21/5/154 | date not recovered | study | - | search only
S-D10-040 | Gen AI attitudes among gamers (Quantic Foundry, Nick Yee) | https://quanticfoundry.com/2025/12/18/gen-ai/ | 18 Dec 2025 | study | primary returned 403 in both rounds; figures confirmed via S-D10-046 | search only
S-D10-041 | GDC 2026 by the numbers (Cinevva) | https://app.cinevva.com/news/2026-03-13-gdc-2026-by-the-numbers | Mar 2026 | press | secondary to the GDC report; superseded for the 52% figure by S-D10-053 | search only
S-D10-042 | GDC 2026 report on generative AI (Gianty) | https://www.gianty.com/gdc-2026-report-about-generative-ai/ | 2026 | press | secondary to the GDC report; superseded for the 52% figure by S-D10-053 | search only
S-D10-043 | Listeners engage less deeply with music labeled as AI, even when human-made (Music Business Worldwide) | https://www.musicbusinessworldwide.com/listeners-engage-less-deeply-with-music-labeled-as-ai-even-when-its-actually-human-made-academic-study-finds/ | date not recovered | press | reports studies by Wu and Holmes and Friedrichsen et al. | search only
S-D10-044 | The Transparency Dilemma: How AI Disclosure Erodes Trust (Schilke and Reimann) | https://www.researchgate.net/publication/389852982_The_Transparency_Dilemma_How_AI_Disclosure_Erodes_Trust | 2025 | study | - | search only
S-D10-045 | AI label study (arXiv 2506.16202) | https://arxiv.org/pdf/2506.16202 | 2025 | study | - | search only
S-D10-046 | Quantic Foundry: most gamers are negative about the use of gen AI in video games (Gamesmarket) | https://www.gamesmarket.global/quantic-foundry-most-gamers-are-negative-about-the-use-of-gen-ai-in-video-games/ | 22 Dec 2025 | press | secondary write-up of Quantic Foundry's survey | fetched (summarised, round 2)
S-D10-047 | Newgrounds Art Guidelines | https://www.newgrounds.com/wiki/help-information/terms-of-use/art-guidelines | undated | policy | - | search only (403; quote seen in search)
S-D10-048 | DeviantArt Terms of Service, section 31 | https://www.deviantart.com/about/policy/service | effective date not in fetched text | policy | - | fetched (summarised, round 2)
S-D10-049 | New Label Requirement for AI Artwork (DeviantArt Team journal) | https://www.deviantart.com/team/journal/New-Label-Requirement-for-AI-Artwork-966421077 | 12 Jun 2023, updated 19 Jul 2023 | policy | - | fetched (summarised, round 2)
S-D10-050 | What does "Created using AI tools" mean? (DeviantArt Help Center) | https://www.deviantartsupport.com/kb/en/article/what-does-created-using-ai-tools-mean | undated | policy | - | search only (fetch truncated before rule text)
S-D10-051 | Use of AI Software on ArtStation (ArtStation help) | https://help.artstation.com/en/articles/16155157-use-of-ai-software-on-artstation | 2 Sep 2026 | policy | - | fetched (by the lead and by the gatherer)
S-D10-052 | ArtStation Terms of Service | https://www.artstation.com/tos | undated | policy | summary of section 46 seen in search | search only (403)
S-D10-053 | GDC 2026 State of the Game Industry (GDC) | https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/ | date not recovered | study | - | fetched (summarised, round 2)
S-D10-054 | One third of game workers use generative AI but half think it's bad for the industry (Game Developer) | https://www.gamedeveloper.com/business/one-third-of-game-workers-use-generative-ai-but-half-think-it-s-bad-for-the-industry | 3 Feb 2026 | press | reports the GDC survey | fetched (summarised, round 2)
S-D10-055 | Apple's new App Store rules crack down on AI nudification and bait-and-switch apps (9to5Mac) | https://9to5mac.com/2026/10/16/apples-new-app-store-rules-crack-down-on-ai-nudification-and-bait-and-switch-apps/ | 16 Oct 2026 | press | an AGTP post on X reports the same; the 2.5.19 "bait-and-switch" claim is not on the fetched Apple page, the 1.2 point is partly on it | search only
S-D10-056 | Frontier yanks generative AI portraits from Jurassic World Evolution 3 after fans revolt (Game Developer) | https://www.gamedeveloper.com/production/frontier-yanks-generative-ai-portraits-from-jurassic-world-evolution-3-after-fans-revolt | 25 Jun 2025 | press | - | fetched (summarised, round 2)
S-D10-057 | GenAI in games: most players just don't care (Yahoo Tech syndication of GameSpot) | https://tech.yahoo.com/gaming/articles/genai-games-most-players-just-124400774.html | 24 Mar 2026 | press | syndicated GameSpot piece reporting Circana PlayerPulse via Mat Piscatella | fetched (summarised, round 2)
S-D10-058 | What do Steam fans really think about AI (GameDiscoverCo newsletter) | https://newsletter.gamediscover.co/p/what-do-steam-fans-really-think-about | 7 Jul 2026 | blog | secondary newsletter write-up of a survey fielded 25 Jun to 2 Jul 2026 | fetched (summarised, round 2)
S-D10-059 | Online Art Communities Begin Banning AI-Generated Images (Waxy.org, Andy Baio) | https://waxy.org/2022/09/online-art-communities-begin-banning-ai-generated-images/ | 9 Sep 2022 | blog | second-hand report of the Newgrounds and Fur Affinity rules | fetched (by the lead and by the gatherer, summarised)
S-D10-060 | 1666: Amsterdam Dev Responds To AI Controversy (TheGamer) | https://www.thegamer.com/1666-amsterdam-ai-art-response/ | 10 Jun 2026 | press | - | fetched (by the lead and by the gatherer)
S-D10-061 | Valve, AI Content on Steam (Steamworks Development announcement, Jan 2024) | https://steamcommunity.com/gid/103582791433666425/announcements/detail/3862463747997849619 | 2024 | policy | primary: Valve's own Steamworks announcement (the itch.io post it replaces returned 404) | search only
S-D10-062 | duplicate of S-D10-060 (TheGamer, 1666: Amsterdam) | https://www.thegamer.com/1666-amsterdam-ai-art-response/ | 10 Jun 2026 | press | cite S-D10-060 | fetched
S-D10-063 | duplicate of S-D10-059 (Waxy.org) | https://waxy.org/2022/09/online-art-communities-begin-banning-ai-generated-images/ | 9 Sep 2022 | blog | cite S-D10-059 | fetched (summarised)
S-D10-064 | Fur Affinity bans AI art (Dogpatch, opinion) | https://dogpatch.press/2022/09/14/fur-affinity-bans-ai-art/ | 14 Sep 2022 | press | opinion piece, no policy text | fetched
S-D10-065 | 1666: Amsterdam (GamerMarkt) | https://www.gamermarkt.com/blog/1666-amsterdam-ai-art-controversy-full-game/ | undated | blog | - | search only
S-D10-066 | Guideline 2.3.3: Screenshots Showing the App in Use (Apple Developer) | https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots | undated | policy | - | fetched (summarised)
S-D10-067 | McDonald's pulls AI-generated Christmas ad (NBC News) | https://www.nbcnews.com/world/europe/mcdonalds-ai-generated-christmas-advert-social-media-backlash-rcna248590 | 11 Dec 2025 | press | - | fetched (summarised)
S-D10-068 | McDonald's halts AI-generated Christmas ad (TODAY) | https://www.today.com/food/news/mcdonalds-removes-ai-generated-christmas-ad-social-media-backlash-rcna248668 | 11 Dec 2025 | press | NBC-owned, counted with S-D10-067 as one origin | fetched (summarised)
S-D10-069 | Coca-Cola's AI Christmas ad 'most talked about' on social (Campaign) | https://www.campaignlive.com/article/coca-colas-ai-christmas-ad-most-talked-about-social/1940473 | Nov 2025 | press | Sprout Social data | search only
S-D10-070 | Anti-AI Art Communities (AlternativeTo list, quotes Fur Affinity 2.13) | https://alternativeto.net/lists/41259/anti-ai-art-communities/ | undated | guide | second-hand list | search only
S-D10-071 | Fur Affinity bans artworks generated by AI (Flayrah) | https://www.flayrah.com/8747/fur-affinity-bans-artworks-generated-artificial-intelligence-programs | 2022 | press | - | search only (403 on fetch)
S-D10-072 | Newgrounds art guidelines, Wayback copy | https://web.archive.org/web/20250604032814/https://www.newgrounds.com/wiki/help-information/terms-of-use/art-guidelines | 4 Jun 2025 | policy | archived copy cited in a search summary | search only (not opened)
S-D10-073 | Fur Affinity AUP, Wayback copy | https://web.archive.org/web/20250604031948/https://www.furaffinity.net/aup | 4 Jun 2025 | policy | archived copy cited in a search summary | search only (not opened)
S-D10-074 | Does Newgrounds allow NSFW content? (Veilwright Studio, 2026 explainer) | https://veilwrightstudio.com/journal/does-newgrounds-allow-nsfw/ | 2026 | blog | - | search only (not opened)
S-D10-075 | 1666: Amsterdam drops generative AI, Panache says (1vX.gg) | https://1vx.gg/news/panache-says-1666-amsterdam-has-removed-generative-ai-entirely | undated | press | second-hand | search only
S-D10-076 | Apple tightens App Store rules against harmful AI image apps (TUAW) | https://www.tuaw.com/2026/10/19/apple-tightens-app-store-rules-against-harmful-ai-image-apps | 19 Oct 2026 | press | same announcement as S-D10-055 | search only
S-D10-077 | Apple's App Store rules now require apps to remove AI intimate imagery (ppc.land) | https://ppc.land/apples-app-store-rules-now-require-apps-to-remove-ai-intimate-imagery/ | Oct 2026 | press | same announcement as S-D10-055 | search only
S-D10-078 | App Store Guideline 2.3.3 Screenshots Rejection (appsubmitter.io) | https://www.appsubmitter.io/app-rejection-guides/app-store-guideline-2-3-3-screenshots/ | undated | guide | vendor | search only
S-D10-079 | Coca-Cola faces intense backlash for AI 2025 Christmas ad (Euronews) | https://www.euronews.com/2025/11/05/real-magic-coca-colas-ai-generated-christmas-ad-sparks-widespread-backlash-again | 5 Nov 2025 | press | - | search only
S-D10-080 | duplicate of S-D10-055 (9to5Mac) | see S-D10-055 | 16 Oct 2026 | press | cite S-D10-055 | search only
