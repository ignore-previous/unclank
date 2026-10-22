---
name: unclank-launch
description: Pre-launch check for the visible defaults and leftovers that make a site, app or repo look unfinished or machine-made, such as the starter favicon and page title, a missing link preview, a stock 404 page, builder badges, placeholder text and an unchecked templated README. Use it when someone is about to ship, deploy, share or open-source something, asks for a launch or polish check, or asks why their project looks vibe-coded. It also covers making these choices during a build.
---

# unclank-launch

Checks what a visitor sees before they read a word: the browser tab, the link preview, the error page, the badges, leftover placeholder text and the README. None of these proves AI was used. Each one shows that a starter or builder default shipped and nobody checked it. They are common starter leftovers that readers associate with AI-built projects. The research also suggests readers react to **clusters**, not single hits.

Every check here comes from evidence-backed research. Each one has a tell ID (e.g. [D08-001]). The reasoning, dates and sources are in `references/evidence.md`. Read an entry there before telling someone that a hit matters, when they push back, or when you need the fix details.

## Modes

- **Audit mode** (the default when asked to "check", "review" or "audit"). Report the hits first and change nothing until the user asks for fixes. Follow "How to audit" below.
- **Build mode** (when creating or finishing a project). Apply the checklist as you go, so nothing in it is left at its default. Mention briefly what you set. Don't produce an audit report or the UNCLANK-AUDIT block. List anything you couldn't finish (a file you can't create or delete, a fact to verify) as next steps for the user.

## Not a tell: don't flag or "fix" these

- Using a framework (Vite, Next.js, React) or a host (Vercel, Netlify). The tell is the untouched default inside it, not the tool [D08-N01].
- A README with working install steps and the usual sections [D08-N02].
- A few badges that report something true, such as CI status, version or licence [D08-N03].
- Standard legal wording and sections. Only a mismatch with what the site does, or a leftover template bracket, is a problem [D08-N04].
- Emoji in a README by themselves. It's an old human habit too [D08-N05].
- Vite serving the app for unknown paths (single-page-app fallback). That's framework behaviour; what matters is what the visitor then sees [D08-N06].
- A `favicon.ico` file in the app root. That's a normal convention; only the untouched default icon is a tell [D08-N07].

## Checklist

Labels: **Avoid** means fix it before launch. **Choose deliberately** means it's fine if it was chosen, and a signal when it's an unchosen default. Confidence: **strong** means 3+ independent sources, **moderate** means 2, **anecdotal** means one opinion, so treat it as a hint.

### Browser tab and search result
- [Avoid · strong] **Starter page title or description** [D08-002]. Look at `<title>` and `<meta name="description">` in the entry HTML, or the framework's metadata export (e.g. `app/layout.tsx` in Next.js). Starter titles look like "Vite + React", "Vite App", "Create Next App", "React App", "My App", or a generic folder name such as "client" or "my-app". A folder name that is the product's real name is fine. A description that is the starter's own text counts too. A missing description goes under "Check this".
- [Avoid · strong] **Starter favicon** [D08-001]. Look for `<link rel="icon">` and the icon files. Flag the Vite bolt (`vite.svg`) and the React atom (`logo192.png`, `logo.svg`). Flag a Next.js `favicon.ico` only if you can show it's the starter's file (for example, the same byte size as the default). Otherwise, and when there's no icon at all, list it under "Check this". The fix is a real mark, deleting the starter icon files, and serving `/favicon.ico` as well as an SVG.

### Link preview (when someone shares the URL)
- [Avoid · moderate] **Missing or default social preview** [D08-004]. Every page people will share needs `og:title`, `og:description`, `og:image` and `twitter:card`, in the HTML the server sends, not added later by JavaScript. A missing tag is the hit. For the image, an absolute URL at 1200x630 is Facebook's recommended size (600x315 is its minimum). If you can't measure the image, put its size under "Check this".

### Error page
- [Avoid · strong] **Stock or blank 404** [D08-003]. Check for a custom not-found page: `404.html`, `app/not-found.tsx`, `pages/404`, a catch-all route, or the host's error-page setting. Without one, visitors see the host's stock error or a bare message with no way back. Where you can, request a made-up path and look at the result. Otherwise say it's inferred from the code. The fix is a branded 404 with navigation and a link home.

### Builder leftovers
- [Avoid · strong] **Builder badge the owner didn't choose** [D08-005]. Look for "Edit with Lovable", "Made in Bolt" and similar floating badges. Removing one usually needs a paid plan, or exporting and self-hosting. Hiding it with CSS isn't a fix.
- [Avoid · anecdotal] **Generator credit left in the page** [D03-013]. Look for footer or meta text crediting a site builder or AI tool that the owner didn't choose to show.
- [Choose deliberately · anecdotal] **Builder fingerprints in the page source** [D08-012]. Look for generator meta tags and attributes from AI builders (Lovable, Bolt, v0, Google AI Studio) and comments that read like prompts. A static-site generator's own generator tag (Hugo, Astro, WordPress) is a framework default, not a hit [D08-N01]. Strip them at the source in the build. Don't fake them away.

### Placeholder content
- [Avoid · anecdotal] **Placeholder content on a live page** [D08-007]. Search the user-facing text for `lorem`, `ipsum`, `John Doe`, `Jane Doe`, `Your Name`, `Your Company`, `[Insert`, `TODO`, `TBD`, and `Ask if you'd like` or similar chatbot offers. Check that the footer year is current and that stock testimonials or logos aren't stand-ins. Flag `example.com` addresses only in visible contact details or links. Skip input `placeholder=` hints, docs, code comments and test files: only what users can see counts.

### README and repo (if the repo is or will be public)
- [Choose deliberately · strong] **Templated README that wasn't checked** [D08-010]. The strong evidence is for an emoji on every heading, which developers call AI-made. Generic sections that say nothing specific are a weaker sign. Install steps you can't run and a missing limits section go under "Check this", not the audit block. Fix with plain headings, sections chosen for this project, install steps actually run, and one real limitation stated.
- [Avoid · anecdotal] **Leftover template or chatbot text in a README** [D08-013]. Search for square-bracket placeholders, `[Insert` or `<insert`, "choose a licence" or "choose a license", "your-username", and chatbot closings ("Let me know if you'd like…"). Also flag a licence section with no LICENSE file.
- [Choose deliberately · anecdotal] **Badge wall** [D08-011]. Keep only the badges that report something true and point at the real repository.

### Content details
- [Choose deliberately · moderate] **Emoji instead of icons, or sparkles in copy** [D08-006]. Emoji in interface chrome, such as buttons, nav and feature bullets, and ✨ in welcome or marketing copy. The fix is one real icon set for the interface, keeping emoji for content.
- [Avoid · anecdotal] **Missing or meaningless alt text** [D08-008]. Informative images need real alt text. Alt text like "image" or the filename doesn't count. Decorative images should have `alt=""`, and that empty alt is correct.
- [Avoid · anecdotal] **Template legal pages or cookie banner that don't match the site** [D08-009]. The policy should list the cookies and third parties that actually load, with every template bracket filled in. Report it, but don't rewrite legal text yourself: that's for the owner.

## How to audit

1. **Find the surfaces:**
   - the entry HTML files and the framework metadata;
   - `public/` or `static/`;
   - the router's not-found handling;
   - the README and LICENSE;
   - any `og:` image files.

   For a built site, check the built output too: it can differ from the source, and a stale build can hold old text.
2. **Run every check** in the checklist. Read the files; don't guess. A hit needs evidence you can point to. Report a Choose deliberately item only when the files show the default; you can't see intent, so say it may be deliberate. Mark a hit "inferred" when the files show the fault but you couldn't confirm it live, such as no not-found route in the code. When you can't see enough to judge (a file the project mentions isn't there, or you can't view an image or request a URL), it isn't a hit: list it under "Check this" and keep it out of the audit block.
3. **Group hits that share a fix.** For example, one missing `<head>` block causes the title, description and social preview hits.
4. **Write the report:**
   - Avoid hits first, worst first, then Choose deliberately. Give each hit its tell ID, file and line, what you saw, and the fix in one line.
   - Say how many hits there are, and whether they form a cluster. 3 or more Avoid hits is the pattern readers notice.
   - List the checks that passed in one line, so the user knows what was covered, then the "Check this" items.
5. **End with the audit block,** exactly in this form. Use one line per hit, and leave out the "Check this" items. The label is exactly `Avoid` or `Choose deliberately`; for an inferred hit, start the note with `inferred:`. When something is missing, give the file where it belongs and `-` for the line. If there are no hits, write the two marker lines with nothing between them.

```
UNCLANK-AUDIT
D08-002 | Avoid | index.html:7 | title is "Vite + React"
D08-004 | Avoid | index.html:- | no og: or twitter: tags
END-UNCLANK-AUDIT
```

## Ground rules

- Check your own or the user's work. Don't use these signals to accuse anyone of using AI: human projects ship starter defaults too.
- Don't flag anything on the Not a tell list. When unsure, say "check this" rather than calling it a hit.
- In audit mode, change nothing until the user asks.
- For games, store pages and platform AI-disclosure rules, use `unclank-store`. For page design (layout, colour, type, cards), use `unclank-ui` once it's released (planned).

Last reviewed: 21 Oct 2026. Evidence: `references/evidence.md`. Full research: `research/domains/D08-tech-defaults-visible.md`.
