# D08 tech-defaults-visible

Technical defaults a visitor can see (tab icon, tab title, 404 page, link preview, platform badges, leftover placeholder text) and the same kind of leftovers in a repo's README, plus builder markers that only show in page source. These signal a scaffold or builder that nobody finished. No source ties any of them to AI alone: they show a starter was used and not checked. The best-sourced guide (Checkvibe, a vendor) says no single signal proves anything and only the combination matters. Evidence is mostly hand-filed GitHub bugs (they show a default shipped, not that visitors notice), vendor guides, detector-tool criteria (opinion, not measurement) and forum comments. No measured sample of live AI-built sites was found. Colour and UI-library sameness is left to D03. The arXiv paper 2609.15369 (SlopShape) analyses the text of company blog posts, not HTML or layout, so it is not D08 evidence. Rounds 1 to 3 merged.

## Checklist
- [Avoid · strong] Replace the starter's page title ("Vite + React", "Create Next App", "My App", the project folder name) and its placeholder meta description before launch (D08-002)
- [Avoid · strong] Replace the framework favicon (Vite bolt, Next.js triangle, React atom) with your own mark, delete the starter's icon files and serve /favicon.ico too (D08-001)
- [Avoid · strong] Add a branded 404 with navigation and a link home; do not ship the host's stock or blank 404 (D08-003)
- [Avoid · strong] Remove builder badges ("Edit with Lovable", "Made in Bolt") by upgrading from the free plan or exporting and self-hosting (D08-005)
- [Choose deliberately · strong] Edit a templated README: plain headings, install steps you have run, no emoji on every heading, and read it once for leftover template or chatbot text (D08-010)
- [Avoid · moderate] Give every shared page an absolute og:image of at least 1200x630, plus og:title and og:description, in server-rendered HTML (D08-004)
- [Choose deliberately · moderate] Use one real icon set for UI; keep emoji for content, and drop sparkle emoji in welcome messages (D08-006)

## Tells

### D08-001 Untouched framework favicon
- Label: Avoid
- Confidence: strong (3 unrelated GitHub PRs, all fetched, plus 2 fetched HN comments from two threads and 2 vendor/author guides counted as one; the PRs prove the default shipped, the HN comments show readers noticing) Lead review 20 Oct (r2): strong accepted for "the default favicon ships": three unrelated fetched PRs. Nobody in them says visitors noticed, and one PR body was written by Claude Code.
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: A scaffold's own icon in the tab, in search results and in share sheets shows that the starter was never finished. Three PRs from unrelated repos (Sep and Oct 2026) show the default reaching production and being fixed by hand; they say nothing about whether visitors notice. The reader-side evidence is thinner: two HN commenters (Apr and Feb 2026) spotting a Vite favicon or the default Next.js one on a Show HN, one line each. AI builders and quick starters ship these defaults, so they turn up on AI-built sites, but nothing ties them to AI alone.
- Fix: Replace favicon.ico, the SVG/PNG icons and apple-touch-icon with a brand mark. Delete the starter's icon files so no default stays behind, and serve /favicon.ico as well as the SVG, since one PR author reads from server logs that some clients ask for it directly.
- Fixable: yes by editing
- Sources: S-D08-001, S-D08-002, S-D08-003, S-D08-004, S-D08-005, S-D08-050, S-D08-060, S-D08-052, S-D08-077
- Flag: The sbdnext-event PR (S-D08-005) body was written by Claude Code, an AI agent. It is evidence that the default favicon shipped, but its explanation that app/favicon.ico overrides app/icon.png is the agent's own claim; the Next.js docs (S-D08-052) say where favicon.ico goes but not which file wins. Do not treat precedence as fact. "Delete the starter's icon files" holds without it. None of the three PRs says the site was AI-built. Checkvibe (S-D08-001) and the DEV post (S-D08-002) are vendor content from one tool author's world and count as one; the DEV post gives no counts and its sample was picked for showing the tells. Checkvibe does not name a Vercel favicon; the two Next.js PRs do. The round 3 HN comment (S-D08-060) is one line with no count and does not say the site was AI-built. A Next.js community discussion (S-D08-077, search snippet only, replies not docs) reports that a favicon.ico in src/app overwrites a custom icon; it does not settle the precedence question.

### D08-002 Default page title and metadata strings
- Label: Avoid
- Confidence: strong (3 unrelated GitHub issues and 3 HN comments from three threads, all fetched, plus Checkvibe; the issues prove the default shipped, the HN comments show readers noticing)
- Dated: noted from 2024, still cited in 2026
- Why it reads as AI: The tab, Google result and link preview show the starter's name ("Vite + React", "Create Next App", "My App"), the project folder's name ("client", "Vite App") or the starter's placeholder description, so the site looks unfinished at first glance. Starters ship these strings and they reach production unchanged. Three issues in unrelated repos (one from Oct 2024, two from Oct 2026) show the defaults shipping; three HN commenters (Mar 2024, Dec 2025, Apr 2026) noticed a "Vite App", "client" or "Create Next App" title on a Show HN, one calling it confusing on desktop. Neither group ties the default to AI.
- Fix: Set a real title and meta description. In Next.js edit the metadata export in app/layout.tsx; in Vite edit index.html and set per-route titles in code or with a head library. Rename a title that is only the folder name.
- Fixable: yes by editing
- Sources: S-D08-001, S-D08-006, S-D08-007, S-D08-008, S-D08-050, S-D08-051, S-D08-061, S-D08-057, S-D08-042
- Flag: The fetched issues are plain bugs with one-line fixes and none ties the default to AI; a hand-written site can ship the same title. The three HN comments are one-liners on single posts with no counts. The folder-name variant ("client", "my-app") rests on the two older comments only. Placeholder meta descriptions rest on the Checkvibe summary, one issue body that quotes the create-next-app description, and the Vibe extension's criteria list (S-D08-042, tool criteria, opinion).

### D08-003 Default or blank 404 page
- Label: Avoid
- Confidence: strong (3 unrelated GitHub issues, all fetched, plus Checkvibe; the issues prove the default shipped, not that visitors notice) Lead review 20 Oct (r2): strong accepted for "the default 404 ships" (three unrelated fetched issues). Visitor reaction is unmeasured. Round 3 searched HN and the web for a visitor or press reaction to a default 404 and found none, so there is no upgrade.
- Dated: noted from 2026, still cited in 2026
- Why it reads as AI: Scaffolded apps often ship with no custom not-found page, so a visitor who mistypes a URL sees the host's stock error (Checkvibe cites Vercel's "404: NOT_FOUND"), a bare framework message such as a black page with "404 | This page could not be found." and no navigation, or nothing at all. Three issues in unrelated repos (23 Sep to 8 Oct 2026) report this; they were filed by the projects' own developers, so they show the default shipped and say nothing about visitors noticing. One calls it only "cosmetic".
- Fix: Add a branded not-found page with navigation and a link home (app/not-found.tsx or pages/404.js in Next.js; route unknown paths to a branded component in Vite). Match the app's language and design; one issue was an RTL Hebrew app falling back to an English default page.
- Fixable: yes by editing
- Example done well: rescue-dog-aggregator issue #456 closed in a day, with a comment confirming the live fix kept the header, footer and links back into the catalogue (S-D08-009).
- Sources: S-D08-001, S-D08-009, S-D08-010, S-D08-011
- Flag: None of the issues ties the default to AI; a default 404 is common on hand-written sites too. One blog (S-D08-076, search only) says about 40% of users close the tab on a default 404, but it gives no source for the figure; it is not used here. How a Vite single-page app answers an unknown path is still unverified: the Vite docs (S-D08-053) say appType defaults to 'spa' but not what an unknown path returns.

### D08-004 Missing or default social preview
- Label: Avoid
- Confidence: moderate (1 fetched GitHub PR, 3 fetched official docs or specs that say what to set but not that omission reads as AI, plus Checkvibe and the DEV post counted as one vendor source; 1 search-only blog) Lead check 20 Oct (r3): moderate is right. The documentation says what to set; it does not show that a missing image reads as AI.
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: A shared link that shows a blank card or the site's stock image tells everyone who shares it that no one set up the metadata. Checkvibe groups a missing og:image with template defaults. One PR (MyWebsite #39, merged 14 Oct 2026) says link previews had no Open Graph image at all before the fix. The DEV post says most of its sample had incomplete or missing OpenGraph metadata, but it gives no count and its sites were picked for showing the tells, so it cannot show how common this is.
- Fix: Add an absolute https og:image of at least 1200x630 (about 1.91:1), plus og:title, og:description and twitter:card, in server-rendered HTML. The size comes from Facebook's docs (600x315 is the minimum for large link posts, 200x200 the smallest allowed, 8 MB the cap); the Open Graph spec gives no size. In Next.js set metadataBase so the image resolves to the production URL, not localhost. Next.js docs say bots and crawlers that expect metadata in the head get it without streaming. The image itself is a design choice.
- Fixable: yes by editing
- Sources: S-D08-001, S-D08-002, S-D08-004, S-D08-012, S-D08-057, S-D08-070, S-D08-071, S-D08-042
- Flag: Vendor sources carry the AI link (the DEV post's author built the tool it reports on). The crawler point is now backed by Next.js docs, but only for Next.js; the general claim that crawlers skip client-side JavaScript rests on a search-only blog (S-D08-012). The Vibe extension lists "Missing SEO meta tags" as a criterion (tool criteria, opinion). A missing og:image is common on hand-written sites and is invisible until someone shares the link. Round 3 found no reader reaction to a blank link preview. The ogp.me spec (S-D08-071) lists og:image as a required property, but neither it nor Facebook's docs (S-D08-070, lead-checked 20 Oct 2026) require an absolute URL; that rule rests on the Next.js docs and general practice. The docs show the property is expected, not that readers read its absence as AI, so the tell stays moderate; the lead may judge otherwise.

### D08-005 Builder badges the visitor did not choose
- Label: Avoid
- Confidence: strong (4 fetched origins: Lovable docs, Bolt docs, Parkstatic and Checkvibe; all vendors, and the docs prove the badge exists, not that readers read it as low effort) Lead review 20 Oct (r2): strong accepted. Lovable's and Bolt's own docs are primary facts from two different companies, not vendors copying each other, and the badge names the builder on the page, so the claim that it is visible needs no reader study.
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: On the free plan, Lovable and Bolt put a badge on published sites ("Edit with Lovable", "Made in Bolt"). It names the platform to every visitor and puts the builder's brand on your site. Lovable's plan table shows badge removal as a dash for Free and Yes for Pro, Business and Enterprise (lead-checked 20 Oct 2026); Bolt's FAQ says a paid plan removes its badge. Checkvibe lists the badge as a platform fingerprint. The only reader-side evidence is one HN comment (Jul 2025) saying a site looked like a perfect example of AI until the commenter found the Lovable badge.
- Fix: Upgrade from the free plan: in Lovable it is a per-project setting under Project settings, Publishing, and a downgrade brings the badge back at the next publish; in Bolt any paid plan removes it. Or export the code and self-host on your own host and domain. Do not rely on hiding it with CSS: Parkstatic says that does not hold and a dismiss button only lasts until the next page load. Shipper.now (fetched) quotes a free CSS method but says the badge stays in the DOM and the code; the Medium guide it draws on is still search only.
- Fixable: yes by editing (platform setting or export)
- Sources: S-D08-001, S-D08-034, S-D08-035, S-D08-036, S-D08-022, S-D08-072, S-D08-062, S-D08-023, S-D08-024
- Flag: The docs establish the free-plan badge and its paid removal, not that visitors read it as AI or low effort; a badge on a free plan is a cost choice, not proof of low effort. Parkstatic sells self-hosting, and its claim that Lovable's servers inject the badge at serve time (so a self-hosted build has none) is not in Lovable's docs; treat it as Parkstatic's claim. Parkstatic's CSS verdict and the Medium guide (S-D08-024, HTTP 403, search only; S-D08-074 is the same URL) disagree on whether hiding the badge is acceptable. Parkstatic and Shipper.now agree it stays in the DOM, and Shipper.now quotes a Lovable FAQ line saying free users always see the badge, which its own CSS method does not reconcile. The HN comment (S-D08-062) does not name the site, and the thread title in the API listing is about a car, so its link to the comment is unclear; one replier defends Lovable. Treat it as one anecdote. S-D08-023 is search only. Round 1 also named a Replit badge but no source in this file covers it, so it is dropped. Strong rests on four fetched origins that are all vendors; the lead may prefer moderate.

### D08-006 Emoji standing in for icons or sparkle in copy
- Label: Choose deliberately
- Confidence: moderate (2 fetched opinion sources on UI emoji, the godobject post with its HN thread counted as one, and Krebs's blog and tool; 2 further sources search only)
- Dated: noted from 2026, still cited in 2026
- Why it reads as AI: Emoji are already in the text a generator writes, so they get dropped in for icons or as decoration (the godobject post cites a sparkle in hype welcome messages) at no cost. They also look different on each OS and read as a stand-in for a real icon. Krebs's slop checker lists "nav or sidebar items prefixed with emoji" as one of its patterns, and the Vibe extension lists "excessive emoji usage"; both are detector criteria, which are opinion, not measurement. The godobject post names "emoji slop" in general rather than emoji as UI icons; the icon-specific claim comes from Krebs and the two search-only sources.
- Fix: Use one icon set (SVG, one stroke weight, one family) with labels. Keep emoji for content, not UI chrome, and cut sparkle emoji from welcome and marketing copy.
- Fixable: yes by prompting or editing
- Sources: S-D08-014, S-D08-015, S-D08-016, S-D08-017, S-D08-040, S-D08-039, S-D08-042, S-D08-045
- Flag: The HN thread (S-D08-015) mostly accepts emoji as a tell but replies say several patterns are old human habits and one line of prompt removes emoji. The UX blog (S-D08-016) and the GitHub PR (S-D08-017) are search snippets only. Krebs's pattern list belongs to the author's own tool; his blog says 16 patterns but lists 18, while the repo README and check.js give 14 (use 14). HN thread 46651671 (S-D08-045) is a comment about adding emoji to docs and commit messages, not UI icons, and a reply says older models used many emoji and the habit has faded. The Netcraft post (S-D08-044) is about emoji in phishing-kit code comments and does not support this tell. See also D03-009, where emoji icons are Choose deliberately in D03.

### D08-007 Placeholder content left on a live page
- Label: Avoid
- Confidence: anecdotal (one vendor source and one tool-author post counted as one; two detector criteria lists are opinion)
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: Lorem ipsum, "Your Company", "John Doe" testimonials, dead sample links and an old copyright year show that no person read the page before it went live. Checkvibe lists these as clues but calls this group the weakest signal; the DEV post says stale 2024 copyright dates were particularly common on uncustomised Lovable sites, with no counts. The Vibe extension and Paladini's detector both check for generic placeholder text, but a criteria list is opinion, not measured prevalence.
- Fix: Search the rendered page for lorem, "Your", "John Doe", "example" and "placeholder", and check the footer year. Replace or remove each hit.
- Fixable: yes by editing
- Sources: S-D08-001, S-D08-002, S-D08-042, S-D08-043
- Flag: Checkvibe and the DEV post are vendor content with no rates of placeholder text on AI sites. The two detector tools give no accuracy figures (the Vibe listing showed 2 ratings). Three-tier pricing is not claimed as a tell: no source supports it, and a stock hero-plus-feature-cards layout (S-D08-013, a vendor review seen in search only) is a layout question, not a leftover.

### D08-008 Missing or meaningless alt text
- Label: Avoid
- Confidence: anecdotal (the WebAIM figure is good data but covers all sites, not AI-built ones)
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: Generators often skip alt text or write generic values such as "image". The failure is real and common, but sighted visitors rarely see it, so it signals quality problems more than an AI origin.
- Fix: Write alt text for informative images, use an empty alt for decorative ones, and check by hand, since automated checks pass useless alt text. An empty alt on a decorative image is correct.
- Fixable: yes by editing
- Sources: S-D08-030, S-D08-002, S-D08-031
- Flag: The 53.1% missing-alt figure (WebAIM data via a news analysis) is for top-million homepages, not AI sites, and the article's AI link is the author's argument. The DEV post (vendor) has no counts. The GitHub blog item is a search snippet only. Not a visible tell, so it may belong in an accessibility domain. Not re-checked in round 2.

### D08-009 Template or generated legal pages and cookie banner
- Label: Avoid
- Confidence: anecdotal (one vendor guide on AI builders; three general guides that do not mention AI)
- Dated: noted from 2026
- Why it reads as AI: A builder-generated banner with one accept button, a generic privacy policy that says things the site does not do (analytics that fire before consent), or template brackets and credit lines left in the text show the legal pages were never checked.
- Fix: List the real cookies and third parties, make the policy match what loads, block scripts until consent where required, and fill in every template bracket.
- Fixable: no (legal content, not visual)
- Sources: S-D08-025, S-D08-026, S-D08-027, S-D08-028
- Flag: Only the Kukie vendor guide (S-D08-025) speaks about AI builders; the others are general compliance guides. All are search snippets. The claim that a live site left the SEQ Legal credit line in place is the gatherer's inference, not the source's. Generic wording alone is fine (see D08-N04). Not re-checked in round 2.

### Repos and READMEs

#### D08-010 Templated README that looks finished but was not checked
- Label: Choose deliberately
- Confidence: strong (4 fetched HN comments from four separate threads that call an emoji-heavy README AI-made, plus 5 further threads where a commenter calls a README AI-written without naming emoji; the fixed section order rests on search-only vendor posts and is contradicted by a non-vendor guide) Lead review 20 Oct (r2): strong accepted only for "readers call emoji-heavy READMEs AI-made" (four HN threads, fetched). The fixed section order is still vendor-only, so treat that part as moderate at most. Emoji READMEs predate LLMs (D08-N05), so this is a signal, not proof. Round 3: the five extra threads are API excerpts and only the Meshtastic thread was opened (by the lead, 20 Oct); they add reader reaction to the prose feel, not to emoji. Lead check 20 Oct (r3): strong kept. Separate HN threads with different commenters count as separate origins, but they all come from one developer community, so the README should say the reaction is measured among developers, not general visitors.
- Dated: noted from 2025, still cited in 2026
- Why it reads as AI: Four HN commenters on four unrelated projects (Jun 2025 to May 2026) call an emoji-on-every-heading README AI-made. Vendor posts (search only) say AI README generators follow a stock section order (Features, Installation, Usage, Contributing, License) with an emoji on every heading, but a non-vendor guide, makeareadme, uses a different order and says the sections are not fixed, so order alone does not separate AI from human READMEs. The result can look finished before anyone has run the steps, and one commenter notes a polished README that arrived in a single commit. Five more commenters (Dec 2025 to Jul 2026) say a README reads as AI-written and put them off, without pointing to emoji; one also calls it incomplete.
- Fix: Use plain headings with at most one or two emoji, pick the sections your project needs (no order is standard), make sure the install steps run, and add the trade-offs a real builder would mention. If headings change, update in-page links, since emoji alter the anchors.
- Fixable: no (documentation)
- Sources: S-D08-047, S-D08-059, S-D08-049, S-D08-058, S-D08-048, S-D08-046, S-D08-063, S-D08-064, S-D08-065, S-D08-066, S-D08-067, S-D08-068, S-D08-069, S-D08-018, S-D08-019, S-D08-020, S-D08-021
- Flag: The four fetched comments are opinions with no counts, all from HN, so they may share one community's habits; each is one commenter's guess, not proof. A commenter (S-D08-046) recalls major React packages with emoji READMEs about ten years ago, which says the habit predates AI. The fixed section order and the "thin commit history" claim rest on S-D08-018 to S-D08-021, which are search snippets that were never opened; Unilink (S-D08-018) and SlateGit (S-D08-020) are vendors and count as one. The single-commit signal (S-D08-048) is one comment. The termdeck PR (S-D08-021) shows only that emoji headings break anchors, not that they signal AI. The Netcraft post (S-D08-044) is not about READMEs and does not support this tell. Strong rests on comment-level sources from one community (HN), counted as nine threads; the lead may prefer moderate. The five round 3 threads (S-D08-063 to S-D08-067) are excerpts cut at about 125 characters; do not credit them with any feature the excerpt does not show. Prana et al. (S-D08-069, 2018 abstract) shows "what" and "how" sections were already common in READMEs before LLMs. See D08-013 for the leftover-text finding in the Meshtastic thread.

#### D08-011 Badge wall in a README
- Label: Choose deliberately
- Confidence: anecdotal (one vendor guide, seen in search only)
- Dated: noted from 2026 (date not shown)
- Why it reads as AI: A row of decorative badges (language logos, shields) with no build or test badge carries no information, and reads as decoration copied from a template.
- Fix: Keep only badges that report something true about the project (CI status, version, licence) and check that they point at the real repository.
- Sources: S-D08-033
- Flag: Single vendor source, search only, opinion; the "ten shields in a row" criticism is not measured. See D08-N03. Not re-checked in round 2.

#### D08-013 Leftover template or chatbot text in a README
- Label: Avoid
- Confidence: anecdotal (one HN thread, opened by the lead on 20 Oct 2026; one commenter)
- Dated: noted Dec 2025
- Why it reads as AI: A README that still holds a placeholder such as "[Insert your download link here]", or a licence section that reads like a pasted chatbot reply (a line telling you to choose a licence, then an offer to generate more files), shows that nobody read it before publishing. The HN commenter called the README obviously AI-written, said it smelled of AI and a lack of attention to detail, and wondered how much of the code was vibe-coded.
- Fix: Search the README for square brackets, "insert", "choose" and chatbot-style closing offers; fill in or delete each one, pick a licence and add the LICENSE file.
- Fixable: no (documentation)
- Sources: S-D08-063
- Flag: One commenter on one thread. He does not mention emoji, badges or section order, so this does not support D08-010's order claim. His doubt about the code is his own inference. Related to D08-007 (placeholder text on a live page) and D08-009 (template brackets in legal pages).

### Page source

#### D08-012 Builder fingerprints in the page source
- Label: Choose deliberately
- Confidence: anecdotal (two detector tools, each naming a different signal; criteria lists are opinion, not measurement)
- Dated: no first-noticed date found; the Vibe listing was last updated 5 Jan 2026
- Why it reads as AI: Generator meta tags, platform-specific scripts or class prefixes, and prompt-style code comments left in the shipped HTML name the builder, but only to people who view the source or inspect the DOM; a visitor looking at the rendered page sees none of it. Paladini's Vibe Code Detector scores generator meta tags and deployment signatures for Lovable, Bolt, v0 and Google AI Studio; the Vibe Chrome extension lists "AI-style code comments" as a criterion.
- Fix: Strip generator meta tags and prompt-style comments in the build before publishing. Remove them at the source; do not fake them away.
- Fixable: yes by editing (build config or source cleanup)
- Sources: S-D08-043, S-D08-042, S-D08-073, S-D08-075
- Flag: Detector criteria only, with no measured prevalence and no accuracy figures (the Vibe extension had 559 users and 2 ratings at fetch). Not visible on the rendered page, so it may fit better in a source-code domain; the lead decides about moving it. MDN (S-D08-073) documents the generator meta name as identifying the software that made the page; that a meta element is not rendered is general HTML knowledge, not stated on that page. Round 3 searches found no generator tag in published Lovable HTML, and one search-only PR (S-D08-075) says Lovable's data-lov attributes are added only in development mode, so how often Lovable output carries a fingerprint is unverified. No visitor-facing harm either way.

## Not a tell

### D08-N01 Using a framework or a deploy host
- Why it is fine: Building on Vite, Next.js or React, or deploying to Vercel or Netlify, is normal. The tell is the untouched default inside it. Checkvibe says no single signal proves anything and the combination matters more, and that the real concern is unreviewed code, not AI code. Caveat: Checkvibe sells a scanner, so it has a commercial reason to say so.
- Sources: S-D08-001

### D08-N02 A README with working install steps and the usual sections
- Why it is fine: Clear, runnable install and usage steps are the goal whatever the style; check that commands run, links resolve and badges point to the real repository. Install and usage sections are an old convention: a 2018 study of README content found "what" and "how" material very common, and makeareadme's sample template has Installation, Usage, Contributing and License. Their presence alone is not a tell.
- Sources: S-D08-032, S-D08-068, S-D08-069

### D08-N03 A few informative badges
- Why it is fine: Build, test and version badges tell a reader something true about the project. It is the decoration-only wall that reads as filler.
- Sources: S-D08-033

### D08-N04 Standard legal wording and sections
- Why it is fine: Generic privacy and cookie wording is normal boilerplate by design. Only a mismatch with what the site does, or leftover template brackets, is a problem (D08-009).
- Sources: S-D08-029

### D08-N05 Emoji in READMEs as an old human habit
- Why it is fine: One HN commenter recalls major React-ecosystem packages with emoji READMEs about ten years ago. That is one person's recollection, not a measurement, but it shows emoji headings alone do not prove AI (see D08-010).
- Sources: S-D08-046

### D08-N06 Vite's default single-page-app fallback for unknown paths
- Why it is fine: Vite's appType defaults to 'spa'. This is framework behaviour, not a sign of AI. What a visitor sees at an unknown URL is the 404 tell (D08-003), and the fix is the app's own not-found page.
- Sources: S-D08-053

### D08-N07 A favicon.ico file in the app root
- Why it is fine: Next.js documents favicon.ico at the top of app/ as a normal convention. Only the untouched default content is a tell (D08-001).
- Sources: S-D08-052

## Sources
S-D08-001 | How to Tell If a Website Is Vibe Coded: 7 Signals to Check | https://checkvibe.dev/blog/how-to-tell-if-a-website-is-vibe-coded | 7 Aug 2026 | guide (vendor) | | fetched (by the lead)
S-D08-002 | I analyzed 100 vibe-coded websites and found these common mistakes | https://dev.to/kaplich/i-analyzed-100-vibe-coded-websites-and-found-these-common-mistakes-5275 | 6 Aug 2025 | blog (author built the tool it reports on; no counts; the 100 sites came from builders' showcase pages and Twitter examples that "had the telltale signs", so the sample was selected by the tells) | | fetched
S-D08-003 | Replace the Vite default favicon and serve /favicon.ico (PeterHartwieg/Rentenrechner PR #421) | https://github.com/PeterHartwieg/Rentenrechner/pull/421 | merged 27 Sep 2026 | forum (GitHub PR) | | fetched
S-D08-004 | Replace default Vercel favicon/OG image (AshuReiziger/MyWebsite PR #39) | https://github.com/AshuReiziger/MyWebsite/pull/39 | merged 14 Oct 2026 | forum (GitHub PR) | | fetched
S-D08-005 | Fix favicon still showing the default Vercel triangle (powerfloweu/sbdnext-event PR #8) | https://github.com/powerfloweu/sbdnext-event/pull/8 | merged 5 Oct 2026 | forum (GitHub PR; body written by Claude Code, an AI agent; lead-checked 20 Oct 2026) | | fetched
S-D08-006 | fix: replace default 'Create Next App' metadata in root layout (coderooz/Dynamic-Next.js-CMS issue #2) | https://github.com/coderooz/Dynamic-Next.js-CMS/issues/2 | 7 Oct 2026 | forum (GitHub issue) | | fetched
S-D08-007 | Page title is still the default 'Create Next App' placeholder (biu6iu/pantry-pulse issue #67) | https://github.com/biu6iu/pantry-pulse/issues/67 | 8 Oct 2026 | forum (GitHub issue) | | fetched
S-D08-008 | Change Default Tab Title from 'Vite + React' to Custom Site Title (pawarspeaks/TechNexus issue #60) | https://github.com/pawarspeaks/TechNexus/issues/60 | 12 Oct 2024 | forum (GitHub issue) | | fetched
S-D08-009 | Add a branded 404 page (currently Next.js default with no navigation) (ssatama/rescue-dog-aggregator issue #456) | https://github.com/ssatama/rescue-dog-aggregator/issues/456 | 23 Sep 2026 | forum (GitHub issue) | | fetched
S-D08-010 | The 404 page is Next.js's bare default, not in Hebrew or the app's own design (ron14y-sys/squad_lock issue #190) | https://github.com/ron14y-sys/squad_lock/issues/190 | 1 Oct 2026 | forum (GitHub issue) | | fetched
S-D08-011 | 404 page is the default Next.js page with no link home (mnaimfaizy/code-theory issue #167) | https://github.com/mnaimfaizy/code-theory/issues/167 | 8 Oct 2026 | forum (GitHub issue) | | fetched
S-D08-012 | Your link previews are blank because og:image is missing | https://dev.to/renev3408/your-link-previews-are-blank-because-ogimage-is-missing-here-is-a-stdlib-only-python-fix-o1e | date not shown | blog | | search only
S-D08-013 | 7 best AI landing page generators in 2026 | https://manus.im/blog/best-landing-page-generator | 2026 | guide (vendor review) | | search only
S-D08-014 | 10 tells of a slop UI | https://godobject.dev/blog/10-tells-of-slop | 27 Sep 2026 | blog (opinion, anecdote; earlier URL https://hereticpleb.vercel.app/blog/10-tells-of-slop redirects here) | | fetched (by the lead)
S-D08-015 | Tells of a Slop UI (Hacker News thread, 386 points, 244 comments) | https://news.ycombinator.com/item?id=49867038 | 27 Sep 2026 | forum | via Algolia API | fetched
S-D08-016 | AI icon design generic (UX Skill blog) | https://uxskill.laithjunaidy.com/blog/ai-icon-design-generic.html | date not shown | blog | | search only
S-D08-017 | feat(ui): replace emoji icons with a real SVG icon set (HDLC01/Treadwell-Proposal-Tool PR #503) | https://github.com/HDLC01/Treadwell-Proposal-Tool/pull/503 | date not shown | forum (GitHub PR) | | search only
S-D08-018 | GitHub README Templates in 2026 (Unilink) | https://app.unilink.us/blog/github-readme-templates-2026 | date not shown | blog (vendor) | redirect to https://unilink.us/blog/github-readme-templates-2026 not followed | search only
S-D08-019 | Treat AI-Generated READMEs Like First Drafts | https://hackernoon.com/treat-ai-generated-readmes-like-first-drafts | 9 Sep 2026 | blog | | search only
S-D08-020 | Vibe-Coded Projects on Your Resume: Authenticity Red Flags (SlateGit) | https://slategit.com/blog/vibe-coded-projects-on-resume-authenticity-signals | date not shown (about two months old per snippet) | blog (vendor) | | search only
S-D08-021 | docs: emoji section headings in README (kiril6/termdeck PR #97) | https://github.com/kiril6/termdeck/pull/97 | Oct 2026 (per snippet) | forum (GitHub PR) | | search only
S-D08-022 | How to remove the Lovable badge (parkstatic) | https://parkstatic.site/blog/remove-lovable-badge | 6 Aug 2026 | blog (third party; sells self-hosting) | | fetched
S-D08-023 | Remove the Lovable badge (opsily) | https://opsily.com/hosting/ship/remove-lovable-badge | 2026 | guide | | search only
S-D08-024 | How to hide the "Edit with Lovable" badge for free (Medium) | https://medium.com/@elifront/how-to-hide-the-edit-with-lovable-badge-for-free-a685266c08d8 | 2025 | blog | | search only (fetch returned HTTP 403)
S-D08-025 | AI Website Builders and Cookie Consent: 2026 Guide (Kukie) | https://kukie.io/blog/ai-website-builder-cookie-consent | 2026 | guide (vendor) | | search only
S-D08-026 | Privacy Policy Examples: Annotated Sample Sections | https://legalpolicygenerator.com/blog/privacy-policy-examples | date not shown | guide | | search only
S-D08-027 | Cookie Consent, GDPR, and Website Privacy Compliance | https://internet-solutions.net/cookie-consent-gdpr-and-website-privacy-compliance-what-you-actually-need-to-have/ | date not shown | guide | | search only
S-D08-028 | Free Cookie Policy Template (2026) (SEQ Legal) | https://seqlegal.com/free-legal-documents/cookies-policy/ | 2026 | guide (template page) | | search only
S-D08-029 | WP Legal Pages (WordPress plugin page) | https://wordpress.org/plugins/wplegalpages/ | date not shown | guide (plugin page) | | search only
S-D08-030 | Accessibility problems hide inside AI-generated websites | https://the-word.news/2026/0402/accessibility-problems-hide-inside-ai-generated-websites/ | 2 Apr 2026 | press (analysis; uses WebAIM data) | | fetched
S-D08-031 | Your alt text passes automated checks. That doesn't mean it's any good. | https://github.blog/engineering/user-experience/your-alt-text-passes-automated-checks-that-doesnt-mean-its-any-good/ | 24 Aug 2026 (per snippet) | blog (GitHub) | | search only
S-D08-032 | README Markdown: Structure, Syntax & Templates (2026) | https://macmdviewer.com/blog/readme-markdown-guide | 2026 | guide | | search only
S-D08-033 | CI/CD Badges: A Practical Setup Guide (SlateGit) | https://slategit.com/blog/ci-cd-badges-on-github-readme-guide | date not shown | guide (vendor) | | search only
S-D08-034 | Lovable FAQ (hide badge setting) | https://docs.lovable.dev/introduction/faq | not shown | policy (official docs) | | fetched
S-D08-035 | Lovable subscription plans (badge row) | https://docs.lovable.dev/introduction/subscription-plans | not shown | policy (official docs; row "Remove 'Edit with Lovable' badge" shows a dash for Free, Yes for Pro, Business and Enterprise; lead-checked 20 Oct 2026) | | fetched
S-D08-036 | Bolt FAQ (Made in Bolt badge) | https://support.bolt.new/concepts/faq | not shown | policy (official docs) | | fetched
S-D08-037 | Bolt release notes (not cited in a tell; the Bolt FAQ carries the same statement) | https://support.bolt.new/release-notes | not shown | policy (official docs) | | search only
S-D08-038 | SlopShape: Identifying AI-Generated Commercial Web Content (arXiv 2609.15369) (not D08 evidence: it analyses the text of company blog posts, not HTML or layout) | https://arxiv.org/abs/2609.15369 | submitted 17 Sep 2026; v3 28 Sep 2026 | study | | fetched (abstract)
S-D08-039 | design-slop-cop repo (README, check.js, file list) | https://github.com/AdrianKrebs/design-slop-cop | created 28 Apr 2026; pushed 7 Jul 2026 | tool (MIT; author's own; 14 patterns; criteria are opinion, not measurement) | | fetched via GitHub API
S-D08-040 | Scoring Show HN submissions for AI design patterns (Krebs) | https://www.adriankrebs.ch/blog/design-slop/ | 20 Apr 2026 | blog (author's tool; says 16 patterns but lists 18) | | fetched
S-D08-041 | Design Slop Cop live app (not cited in a tell) | https://slopcop.adriankrebs.ch/ | not shown | tool | | search only (fetch failed)
S-D08-042 | Vibe - Detect AI-Generated Websites (Chrome Web Store listing) | https://chromewebstore.google.com/detail/vibe-detect-ai-generated/eicihnfpompmmipabjeejcdgdjomclad | last updated 5 Jan 2026 (per listing) | tool listing (criteria are opinion; no accuracy figures; 559 users and 2 ratings at fetch) | | fetched
S-D08-043 | Vibe Code Detector (Paladini; page and repo) | http://paladini.io/vibe-code-detector/ ; https://github.com/paladini/vibe-code-detector | not shown | tool (MIT, open source; heuristics, not measured) | | fetched
S-D08-044 | Excessive Emojis as an AI Indicator (Netcraft) (not cited in a tell: it covers emoji in phishing-kit code comments, not READMEs or UI) | https://www.netcraft.com/blog/excessive-emojis-as-an-ai-indicator | 24 Mar 2026 | blog (vendor; threat intelligence) | | fetched
S-D08-045 | HN thread 46651671 (Claude and emoji in documentation) | https://news.ycombinator.com/item?id=46651671 | 16 Jan 2026 | forum | via Algolia API | fetched
S-D08-046 | HN thread 45718947 (Recall for Linux; emoji readmes a decade ago) | https://news.ycombinator.com/item?id=45718947 | 27 Oct 2025 | forum | via Algolia API | fetched
S-D08-047 | HN thread 47289023 (Argus; "emoji soup readme") | https://news.ycombinator.com/item?id=47289023 | 7 Mar 2026 | forum | via Algolia API | fetched
S-D08-048 | HN thread 46522706 (SMTP Tunnel; emoji readme, single commit) | https://news.ycombinator.com/item?id=46522706 | 7 Jan 2026 | forum | via Algolia API | fetched
S-D08-049 | HN thread 44310533 (Workout.cool; "readme and emojis seem heavily AI") | https://news.ycombinator.com/item?id=44310533 | 18 Jun 2025 | forum | via Algolia API | fetched
S-D08-050 | HN thread 47694130 (navigation app; "page title says client", Vite favicon) | https://news.ycombinator.com/item?id=47694130 | 8 Apr 2026 | forum | via Algolia API | fetched
S-D08-051 | HN thread 39719832 (developer portfolio; "Vite App" title) | https://news.ycombinator.com/item?id=39719832 | 15 Mar 2024 | forum | via Algolia API | fetched
S-D08-052 | Next.js docs: favicon, icon, apple-icon | https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons | 3 Mar 2026 (lastUpdated on page) | policy (official docs; does not state which icon file wins) | | fetched
S-D08-053 | Vite docs: shared options (appType) | https://vite.dev/config/shared-options | not shown | policy (official docs; does not say what an unknown path returns) | | fetched
S-D08-054 | I Scanned 100 Vibe-Coded Apps for Security (VibeWrench) (not cited in a tell: its 63% figure is "fail basic SEO" with no breakdown and is not about "Vite App" titles; the 100 apps are public GitHub repos, not live sites) | https://dev.to/vibewrench/i-scanned-100-vibe-coded-apps-for-security-i-found-318-vulnerabilities-4dp7 | early Mar 2026 (post dated 9 Mar) | blog (author sells the scanner) | | fetched
S-D08-055 | Junie: why vibe-coded websites don't rank on Google (not cited in a tell: its "17 of 20" audit names no sites, platforms or method) | https://www.tryjunie.io/blog/why-vibe-coded-websites-dont-rank-on-google | May 2026 | blog (vendor; competes with Lovable and Bolt) | | fetched
S-D08-056 | Where to host a website built by AI (not cited in a tell) | https://bootstrap.build/articles/host-ai-generated-website/ | about 42 days before the search (not dated on page) | guide | | search only
S-D08-057 | Next.js docs: metadata and OG images | https://nextjs.org/docs/app/getting-started/metadata-and-og-images | 25 Aug 2026 (lastUpdated on page) | policy (official docs) | | fetched
S-D08-058 | HN thread 48071085 (GitHub Store; "scream AI, including the Readme, emojis") | https://news.ycombinator.com/item?id=48071085 | 9 May 2026 | forum | via Algolia API | fetched
S-D08-059 | HN thread 45219444 (Fartscroll-Lid; "soulless AI emoji slopfest") | https://news.ycombinator.com/item?id=45219444 | 12 Sep 2025 | forum | via Algolia API | fetched
S-D08-060 | HN 47123830 ("Hacker News.love"; "favicon is still the default nextjs one") | https://news.ycombinator.com/item?id=47123830 | 23 Feb 2026 | forum | via Algolia API | fetched
S-D08-061 | HN 46301008 (Show HN: HN++; page title "Create Next App") | https://news.ycombinator.com/item?id=46301008 | 17 Dec 2025 | forum | via Algolia API | fetched
S-D08-062 | HN 44653462 ("perfect example for AI ... lovable badge") | https://news.ycombinator.com/item?id=44653462 | 22 Jul 2025 | forum | via Algolia API | fetched (site unnamed; context unclear)
S-D08-063 | HN 46269292 (Standalone Meshtastic Command Center - One HTML File Offline; commenter calls the README AI-written and points to placeholder and chatbot text) | https://news.ycombinator.com/item?id=46269292 | 15 Dec 2025 | forum | via Algolia API | fetched (thread opened by the lead 20 Oct 2026)
S-D08-064 | HN 46298731 (Show HN: Titan; "readme looks too ai-written") | https://news.ycombinator.com/item?id=46298731 | 17 Dec 2025 | forum | via Algolia API | fetched (excerpt only)
S-D08-065 | HN 46851847 (Show HN: NanoClaw; AI README "a real ick") | https://news.ycombinator.com/item?id=46851847 | 2 Feb 2026 | forum | via Algolia API | fetched (excerpt only)
S-D08-066 | HN 48876728 (Show HN: Reame; "hard getting past the AI-written README") | https://news.ycombinator.com/item?id=48876728 | 11 Jul 2026 | forum | via Algolia API | fetched (excerpt only)
S-D08-067 | HN 48878006 (Show HN: Sqlsure; struggles with AI-written READMEs) | https://news.ycombinator.com/item?id=48878006 | 12 Jul 2026 | forum | via Algolia API | fetched (excerpt only)
S-D08-068 | makeareadme.com (README section guidance and sample template; order differs from the vendor stock order and is called not fixed) | https://makeareadme.com/ | date not shown | guide (non-vendor, personal) | | fetched
S-D08-069 | Prana et al., Categorizing the Content of GitHub README Files (4,226 sections from 393 repositories) | https://arxiv.org/abs/1802.06997 | submitted 20 Feb 2018 | study | | fetched (abstract)
S-D08-070 | Facebook for Developers: sharing images (at least 1200x630; 600x315 minimum for large link posts; 200x200 least allowed; about 1.91:1; 8 MB max; lead-checked 20 Oct 2026) | https://developers.facebook.com/docs/sharing/webmasters/images/ | date not shown | policy (official docs) | | fetched
S-D08-071 | Open Graph protocol (og:image required; no size or aspect guidance) | https://ogp.me/ | date not shown | policy (official spec) | | fetched
S-D08-072 | shipper.now, Lovable badge CSS (quoting page; says the badge stays in the DOM) | https://shipper.now/hide-lovable-badge/ | last updated 28 Aug 2026 | blog (third party) | | fetched
S-D08-073 | MDN, meta name (generator entry) | https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name | date not shown | policy (reference) | | fetched
S-D08-074 | Medium guide, Eli Front (Lovable badge CSS); same URL as S-D08-024, no new evidence | https://medium.com/@elifront/how-to-hide-the-edit-with-lovable-badge-for-free-a685266c08d8 | 2025 (search summary) | blog | | search only (Medium 403; elifront.com mirror 404; freedium SSL error; no Wayback snapshot)
S-D08-075 | GitHub PR ips-ag/FotoGen #161 (lovable-tagger, dev-only data-lov attributes) | https://github.com/ips-ag/FotoGen/pull/161 | date not shown | forum (GitHub PR) | | search only
S-D08-076 | eastondev, Next.js custom error pages (unsourced 40% figure; not used) | https://eastondev.com/blog/en/posts/dev/20260105-nextjs-error-pages/ | 5 Jan 2026 | blog | | search only
S-D08-077 | Next.js discussion #46415 (default favicon overwrites custom icon; replies, not docs) | https://github.com/vercel/next.js/discussions/46415 | opened 2023, replies to Apr 2026 (per snippet) | forum | | search only
S-D08-078 | Next.js discussion #81330 (find or customise default 404; not cited in a tell) | https://github.com/vercel/next.js/discussions/81330 | not shown | forum | | search only
S-D08-079 | Bolt hosting troubleshooting FAQ (no badge information; not cited in a tell) | https://support.bolt.new/cloud/hosting/troubleshoot-host | not shown | policy (official docs) | | fetched
