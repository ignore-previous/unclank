# D05 pixel-game-art

Tells that make pixel art and 2D game sprites, tiles and animation sheets read as AI-generated. Rounds merged so far: R1 breadth (D05-r1-breadth), R2 depth (D05-r2-depth, merged directly by the lead because the PC was over its memory budget for helpers) and R3 depth (D05-r3-depth). Much of the evidence still comes from vendors: most 2026 "fix AI pixel art" guides come from companies that sell a fixer or a generator. Vendor sources are marked "(vendor)", and vendors who repeat each other count once. The fetched non-vendor evidence is a GIGAZINE hands-on review, an independent tool-maker (MonoPix), two itch.io threads and three Hacker News threads; the Hacker News thread of 7 Jun 2025 counts as one origin however many commenters it has. Round 3 added first-hand commenter evidence on lighting, outlines and semi-transparent pixels from that thread, and fetched GamineAI (a vendor that promotes its own AI game-building product). A general study (Ha et al., CCS 2024, S-D05-041) found that commercial detectors and even expert artists flag human art as AI at high rates. So treat each tell here as a quality check on your own work, not as a way to accuse someone else. The human craft rules (small palette, clusters, hue-shifted ramps, bounded dithering, readable silhouettes) are the basis for most Fix lines here. Audience rules are out of scope; in brief, Lospec's gallery (12 Jun 2023) refuses any art that uses AI anywhere in its process, so cleaned-up AI output is also refused, and itch.io and Steam ask for AI disclosure (see D10).

## Checklist
- [Avoid · strong] Reject any "pixel art" that is a high-resolution image under a pixel filter: blocks of different sizes, gradients inside blocks, a grid that drifts (D05-001)
- [Avoid · strong] Put every pixel on one grid, with one pixel size across the whole image (D05-003)
- [Avoid · strong] Use one fixed, small palette shared across the set, not hundreds or thousands of near-identical shades (D05-004)
- [Avoid · strong] Use hard edges, palette indices and binary alpha, not blurred or semi-transparent in-between pixels (D05-005)
- [Avoid · strong] Keep animation frames identical in character, proportions, palette, pivot and cell size, and check the loop at 1x (D05-002)
- [Avoid · moderate] Pick one outline rule for the whole set and remove doubled or soft outlines (D05-006)
- [Avoid · moderate] Fix one lighting setup (direction and style) for the whole set and compare sprites side by side (D05-007)
- [Avoid · moderate] Make tile edges match, and test a 3x3 block for seams before shipping (D05-008)
- [Avoid · moderate] Export true alpha and check every sprite on light and dark backgrounds; no painted checkerboard, halo or leftover background (D05-012)
- [Avoid · moderate] Ship sprite sheets as real atlases: equal cells, frame rectangles, pivots and durations as data (D05-013)
- [Avoid · moderate] Judge every sprite at 1x and zoomed against the craft rules; reject art that only passes at a distance (D05-011)

## Tells

### D05-001 Pixel filter over a high-resolution image (fake pixel art)
- Label: Avoid
- Confidence: strong (4 independent, fetched origins: a GIGAZINE hands-on review, Dec 2025; the Hacker News thread of 16-17 Jan 2025; the Hacker News thread of 7 Jun 2025; the MonoPix tool-maker post, Mar 2026. Pixel Engine (vendor) is a fifth. Lead review 20 Oct (r2): restored to strong. The lead spot-checked GIGAZINE (2 Dec 2025: imperfect grids, colour bleeding, 38,680 colours) and HN 42733893 (17 Jan 2025). The HN voices are commenters, not named pixel artists. R3 adds two comments in the 7 Jun 2025 thread (S-D05-050), counted once with S-D05-011.)
- Dated: noted from Jan 2025 (Hacker News), still cited in 2026 (press, tool-makers)
- Why it reads as AI: the picture is generated at high resolution, then shrunk or snapped to a grid afterwards, so the pixels look like blocks but do not behave like hand-placed ones. The zoom test shows it: block sizes vary or a block holds a gradient. Close up, such an image is an illustration with a filter.
- Fix: draw or generate at native size on a grid, or detect the grid, downscale to the true size with a dominant-colour vote, reduce the palette, and upscale with nearest-neighbour. Reject outputs whose block sizes vary.
- Fixable: partly. A plain "pixel art" prompt gives the filter look; grid-native tools and a snap pass fix it. One HN commenter judged a sample unfixable without redrawing.
- Sources: S-D05-001, S-D05-002, S-D05-005, S-D05-011, S-D05-019, S-D05-020, S-D05-021, S-D05-035, S-D05-036, S-D05-049, S-D05-050, S-D05-051
- Flag: The 7 Jun 2025 thread is split: two commenters argue grid precision matters less once sprites scale at runtime, while another says off-grid art is simply not pixel art. The HN downscaling point is the commenter's guess about how such tools work. Vendors of generators (Retro Diffusion, PixelLab) claim true-grid output; unverified (S-D05-024, S-D05-025). D05-003 is the visible grid symptom of this tell and shares most of its sources. S-D05-049 (Lux, 2022) is a general quality statement about Stable Diffusion output, not about the filter effect, so it is not counted as an origin. S-D05-050 is a title snippet only and S-D05-051 is a search summary only.

### D05-002 Animation frames that change shape, size or pivot
- Label: Avoid
- Confidence: strong (3 independent, fetched origins: the Sprite Sheet Diffusion study, and two vendor guides from different companies with different text, GameLabs and QuestStudio. A third vendor, SpriteFlow's maker on DEV, concedes drift in its own advice.) Lead review 20 Oct (r2): restored to strong. The study is independent, and the vendors' own advice to hand-polish hero characters admits the problem.
- Dated: noted from Mar 2025 (study v2), still cited Aug to Oct 2026 (vendor guides)
- Why it reads as AI: each frame comes from a separate generation or a loosely cut sheet, so cape colour, head size or foot position change between frames, backgrounds jitter and cycles do not loop.
- Fix: generate from one reference pose in a fixed cell size, keyframe first and fill in-betweens, or render frames from a rig. Fix the foot anchor at a recorded coordinate and the bounding box, move only the upper body for idles, and play the loop at 1x as a GIF.
- Fixable: partly. Same-seed and reference-image methods help; full consistency needs a rig or per-frame editing. Plain sprite sheets from a general model: no.
- Sources: S-D05-012, S-D05-013, S-D05-014, S-D05-015, S-D05-016, S-D05-032, S-D05-033
- Flag: The study's own fine-tuned method reaches consistency only in part. Vendors say their tools fix drift; untested here. S-D05-012 and S-D05-013 are still search only.

### D05-003 Off-grid pixels and mixed pixel sizes ("mixels")
- Label: Avoid
- Confidence: strong (fetched: GIGAZINE Dec 2025, MonoPix Mar 2026, HN thread 7 Jun 2025; plus Sprite Fusion with its May 2026 GIGAZINE review counted once, and Anijam). Lead review 20 Oct (r2): upgraded from moderate. It shares its fetched evidence with D05-001, so treat the two as one check in practice. R3: S-D05-050 is the same HN thread as S-D05-011 and counts with it, once.
- Dated: the human complaint about "mixels" is older than generators (an Urban Dictionary entry from 2009 and a Flowlab rant from about 2022, both search only); noted for AI from 2025, still cited in 2026
- Why it reads as AI: one image holds pixels of different sizes, some blocks one pixel wide beside neighbours two wide, because the model paints with no real grid and a grid is applied later. AI made an old beginner's fault common.
- Fix: snap to a detected grid and resample to the true sprite size with nearest-neighbour, or use a grid-native tool. Check at 1x and zoomed.
- Fixable: partly. Prompting alone rarely removes it.
- Sources: S-D05-001, S-D05-002, S-D05-007, S-D05-008, S-D05-011, S-D05-035, S-D05-036, S-D05-046, S-D05-047, S-D05-050
- Flag: Some human artists break the grid on purpose (see D05-N03), so judge intent across the image, not one stray block.

### D05-004 Hundreds or thousands of near-identical colours, no fixed palette
- Label: Avoid
- Confidence: strong (4 origins: GIGAZINE's measured test image, 38,680 colours, lead-verified; Pixel Engine's measured comparison, vendor, lead-checked; Sprite Fusion, vendor; an itch.io commenter who used colour count as their AI test). Lead review 20 Oct (r2): upgraded from moderate. The count is a signal, not proof: the itch.io case was hand-made soft-brush art that was suspected anyway (see D05-N05).
- Dated: noted from 2025, still cited in 2026; players already used it as a test in about 2024
- Why it reads as AI: colour is continuous for the model, so each gradient step becomes a new shade. Pixel Engine (vendor) reports an AI image with over 10,000 unique colours where real pixel art of the same character used about 24.
- Fix: quantise to one named or k-means palette and share it across the set. Scale the count to sprite size (about 4 to 8 for 16 px, about 16 for 64 px). Build ramps that shift hue, with cool shadows and warm highlights, from about 32 px up.
- Fixable: partly. Some generators take a colour limit; post-hoc quantisation is reliable.
- Sources: S-D05-001, S-D05-003, S-D05-005, S-D05-027, S-D05-028, S-D05-035, S-D05-040
- Flag: Each measured count is from one image. Retro Diffusion and PixelLab advertise palette limits (S-D05-024, S-D05-025, search only), so the tell is default output, not every output.

### D05-005 Soft in-between colours and blurred or semi-transparent edges
- Label: Avoid
- Confidence: strong (3 independent, fetched non-vendor origins: MonoPix; GIGAZINE Dec 2025 on colour bleeding and blurred, distorted lines, lead-verified; the Hacker News thread of 7 Jun 2025, where lesostep reports "floating almost-transparent pixels in the mix", lead-verified 20 Oct. Two vendors add support: Sprite Fusion with its May review counted once, and GamineAI, now fetched, which advises binary alpha and warns of semi-transparent fringe pixels.) Lead review 20 Oct (r2): upgraded from moderate. R3: held at strong, with a non-vendor first-hand source added.
- Dated: noted from 2025 (Hacker News, Jun 2025), still cited in 2026
- Why it reads as AI: diffusion favours smooth gradients, and shrinking averages neighbouring pixels, so edges become intermediate shades or partly transparent fringes and the sprite looks smudged. It reads right from a distance and breaks up close.
- Fix: hard palette indices, nearest-neighbour downscale, binary alpha unless the engine needs translucency. Keep only anti-aliasing that is hand-placed at chosen edges, which is accepted craft (D05-N01).
- Fixable: partly. A "no anti-aliasing" prompt helps only some of the time.
- Sources: S-D05-001, S-D05-002, S-D05-003, S-D05-009, S-D05-011, S-D05-035, S-D05-036
- Flag: The tell is generator blur, not anti-aliasing as such. The lesostep comment supports the semi-transparent pixels part only. GamineAI is a vendor and counts as one origin at most.

### D05-006 Inconsistent outline treatment across a set
- Label: Avoid
- Confidence: moderate (2 fetched AI-side origins: the Hacker News thread of 7 Jun 2025, where petesergeant says sprites look like they come from different collections because one has a black outline and one does not, non-vendor and first-hand, lead-verified 20 Oct; and GameLabs, vendor, which reports outline thickness changing between frames. GamineAI, vendor, fetched, only advises fixing an outline policy before batch generation; that backs the Fix, not the tell. Seeles, vendor, and an itch.io buyer thread are search only. Monojog backs the Fix as craft advice.) Lead review 20 Oct (r2): held at moderate. R3: now has a non-vendor first-hand source, but it is one commenter in one thread.
- Dated: noted from Jun 2025 (Hacker News); vendor reports 2026
- Why it reads as AI: the model picks an outline per image and nothing holds one rule for the set, so some sprites get a 1px dark outline, others none, with varying colour, doubled edges or mushy anti-aliased lines. GameLabs also reports outline thickness changing between frames of one sprite.
- Fix: choose one rule (1px dark, coloured sel-out, or none), write it into every prompt, compare the batch side by side, and remove doubled or soft edges. The style choice itself is deliberate and fine; only the mixing is the tell (D05-N04).
- Fixable: yes by prompting/editing. A set-level rule can be written in and checked, not guaranteed.
- Sources: S-D05-009, S-D05-010, S-D05-011, S-D05-032, S-D05-037, S-D05-052
- Flag: The vendors may repeat each other. The itch.io buyer thread (S-D05-052) is search only, has no absolute date, and a reply says the pack is marked AI-assisted, so the cause is not isolated. Strong is arguable if the lead counts GamineAI, but its source is policy advice.

### D05-007 Lighting that changes between sprites in a set
- Label: Avoid
- Confidence: moderate (2 fetched origins: the Hacker News thread of 7 Jun 2025, where SXX says getting style, lighting and camera perspective right is "near impossible" and petesergeant says "The kelp pirates are lit differently from each other"; and GamineAI, vendor, which as the gatherer reports says models invent a new lighting setup per image. Search only and uncounted: a DEV post (S-D05-055) and a second Hacker News thread (S-D05-051).) Lead review 20 Oct (r3): upgraded from anecdotal. The r2 claim that the HN thread has nothing on lighting was wrong.
- Dated: noted from Jun 2025 (Hacker News), still cited in 2026 (GamineAI, 12 May 2026)
- Why it reads as AI: each generation chooses its own lighting, with no shared scene, so direction, strength or style differs between sprites or poses and the set looks assembled.
- Fix: set one direction (for example top-left) and one lighting style in every prompt, compare the set side by side, and repaint shading by hand where it flips. Monojog's craft advice (one light direction across a set) supports the Fix.
- Fixable: partly. A prompt helps one image; a batch needs a reference image or editing.
- Sources: S-D05-009, S-D05-011, S-D05-037, S-D05-051, S-D05-055
- Flag: No comment in the HN thread is about light direction as such; they concern lighting style and sprites lit differently. Light direction is a general craft rule and is a tell only when it is inconsistent. S-D05-051 is a search summary with no date; S-D05-055 is search only with no absolute date. The GamineAI quote is as the gatherer reports it.

### D05-008 Tiles with mismatched edges (seams)
- Label: Avoid
- Confidence: moderate (2 vendors, both fetched in round 2: SpriteForge and Stork; Sprite AI, vendor, search only. No independent AI-side source.) Lead review 20 Oct (r2): held at moderate. R3: held; the only non-vendor source (Pinnguaq) is a human craft lesson.
- Dated: noted from 2026; no earlier AI-specific source (the craft lesson is from Jan 2020)
- Why it reads as AI: tiles are generated as one image and cut afterwards, so no edge is tied to its neighbour. Resizing and colour reduction average the edge pixels, and one mismatched pixel shows as a seam when tiles repeat. The common "fade to a neutral border" workaround gives a stamped look instead.
- Fix: generate on an explicit cell grid, or build a Wang or blob autotile set from one source texture; add one to two pixels of export padding; test two copies side by side and a 3x3 block. Rule out engine filtering, atlas padding and non-integer scaling before blaming the art (D05-N06).
- Fixable: partly. A "seamless" prompt helps some models (vendor claim); autotile construction is reliable.
- Sources: S-D05-017, S-D05-018, S-D05-034, S-D05-054
- Flag: S-D05-054 (Pinnguaq, 2020) is human-craft advice that tiles should align on all sides and that a 3x3 layout exposes seams; it supports the craft rule, not the claim that seams are an AI tell. Stork sells a seamless-pattern generator, not a tileset tool, so it bears less on autotile sets. The 3x3 test is a craft check, not AI-specific.

### D05-009 Stray single pixels and speckle noise
- Label: Avoid
- Confidence: anecdotal (one AI-side source: Seeles checklist, vendor, search only; the 2010 Pixel Joint thread is a human craft rule, not AI evidence)
- Dated: craft rule since 2010; AI-specific cleanup advice in 2026
- Why it reads as AI: isolated pixels with no cluster logic appear in shading, outlines or background and look like noise. Pixel Joint's tutorial calls an isolated single pixel noise (2010).
- Fix: remove orphans, redraw in clusters that describe form, run a despeckle pass, and check cluster sizes at 1x. Deliberate single pixels (a highlight, a sparkle) are fine; the tell is random ones.
- Fixable: partly. Hand cleanup works; prompts are weak here.
- Sources: S-D05-003, S-D05-010, S-D05-029
- Flag: the AI-specific claim rests on one search-only vendor checklist; nothing new in rounds 2 and 3.

### D05-010 Dithering used as a default texture
- Label: Choose deliberately
- Confidence: anecdotal (AI-side: the qwe.edu.pl editorial tutorial, fetched in r3, says AI attempts can look messy; GamineAI, vendor, fetched, only gives a dithering policy for the spec sheet, which is advice, not an observation; the over-dithering warnings are human craft rules)
- Dated: craft warning since 2010; AI-specific advice in 2026 (qwe.edu.pl, 13 Feb 2026)
- Why it reads as AI: when asked for pixel art, models may spread speckle over shadows, gradients and backgrounds to imitate smooth shading, and it reads as static, not as a gradient.
- Fix: use one dither pattern, only at a deliberate transition, and prefer clusters elsewhere. Add "no dithering" to prompts for a clean style. Bounded, deliberate dithering is standard craft and not the tell (D05-N02).
- Fixable: yes by prompting/editing. Editing removes what the prompt leaves.
- Sources: S-D05-003, S-D05-009, S-D05-022, S-D05-023, S-D05-026, S-D05-030, S-D05-031
- Flag: no AI-specific complaint from an artist was found. qwe.edu.pl (S-D05-023) is an editorial tutorial, not a sales page, though it links to its own app. It turns up in many search results, but an exact-phrase search found no sign that it is the origin of other D05-010 claims; the shared-origin worry is unconfirmed, not disproved. Borderline between anecdotal and moderate.

### D05-011 Looks like pixel art at a glance, fails at 1x or zoomed
- Label: Avoid
- Confidence: moderate (non-vendor, fetched: an itch.io comment, Jun 2025; the Hacker News thread of 7 Jun 2025, where a commenter says the samples look very nice but are not pixel art in the sense they understand; Lux, a named pixel artist, 8 Nov 2022, who says no Stable Diffusion algorithm then produced fully adequate pixel art. Pixel Engine's zoom test, vendor, is a further source.) Lead review 20 Oct (r3): upgraded from anecdotal. Lead check 20 Oct: moderate accepted but thin. Lux (2022) is a general quality judgement and overlaps D05-001; keep this tell for its distinct check, viewing at 1x and zoomed.
- Dated: noted 2022 (Lux, general quality), Jun 2025 (itch.io, Hacker News); zoom test in 2026 guide
- Why it reads as AI: the output matches the pixel-art style layer but not the craft rules (clusters, palette, grid), so it passes at a distance and fails up close. An itch.io commenter described a "tried-to-be-pixel-art-but-doesn't-know-what-pixel-art-is look".
- Fix: judge at 1x and zoomed, and check the craft rules one by one: palette, clusters, grid, outline, light.
- Fixable: partly.
- Sources: S-D05-004, S-D05-005, S-D05-049, S-D05-050
- Flag: Lux fits only loosely: it says the output was inadequate as pixel art, not that it passes at a glance, and the post is a disclosure and workflow write-up, not a complaint. The specific HN comment (S-D05-050) is a title snippet only, though its thread is fetched. Largely restates D05-001 and the craft-rule tells, so treat it as a test, not a separate visual cause. The same itch.io thread's other commenters praised a cleaner cover.

### D05-012 Fake transparency: painted checkerboard, halo or leftover background
- Label: Avoid
- Confidence: moderate (vendors only: QuestStudio and GameLabs, fetched, different companies; GamineAI, fetched in r3, covers semi-transparent fringe pixels but not a painted checkerboard. Search only: Sorceress, Elseland (vendor status unchecked), Seeles, BG Clear (vendor), Makerfern. No non-vendor AI-side source.) Held at moderate by the r2 precedent for vendor-only tells. Lead check 20 Oct: holding at moderate is right. All the AI-side sources are vendors that sell cleanup or background removal, so they share a commercial interest.
- Dated: noted 2026 (May to Sep); no earlier source
- Why it reads as AI: generators return a flat image, so the "transparent" background is either painted pixels (a checkerboard) or a removal that leaves a white or dark fringe. The sprite shows a box or halo once it sits in the game.
- Fix: export true alpha with binary edges, strip halo pixels, and check every sprite on light and dark backgrounds at native size. If a PNG looks fine in an editor but fringes in the game, check engine filtering and import settings (D05-N06).
- Fixable: partly. Background removal plus a halo pass fixes most cases; prompts alone do not.
- Sources: S-D05-009, S-D05-015, S-D05-032, S-D05-048, S-D05-056, S-D05-057, S-D05-058, S-D05-061
- Flag: All sources sell or run sprite or tile tools. Seeles S-D05-058 is the same vendor as S-D05-010 and counts once. Alpha handling itself is normal engine practice; the tell is faked or fringed transparency. The HN comment on semi-transparent pixels backs D05-005, not the painted-checkerboard part of this tell. By the letter of the 3-origin rule, three fetched vendors could justify strong; a judgement call for the lead.

### D05-013 Decorative sprite sheet with no frame data
- Label: Avoid
- Confidence: moderate (2 vendors, both fetched: QuestStudio and GameLabs)
- Dated: noted 2026 (Aug to Sep)
- Why it reads as AI: a general model draws one image that looks like a grid of frames, with uneven cells and no frame rectangles, pivots or timing, so it cannot be imported as an atlas. Players see the result as jitter or misaligned frames, not the sheet itself.
- Fix: lay out untrimmed equal cells, record frame rectangles, pivot and duration as data, and export the metadata the engine expects.
- Fixable: partly. Metadata can be added by a tool or by hand; prompts cannot create it.
- Sources: S-D05-015, S-D05-032
- Flag: Both sources sell sprite tools and argue that general tools cannot make atlases, which is self-serving. A hand-drawn sheet can also lack metadata. This is mostly a production defect and overlaps D05-002 where players can see it.

## Not a tell

### D05-N01 Hand-placed anti-aliasing at chosen edges
- Why it is fine: Intermediate pixels placed by hand along curves and diagonals, used sparingly, are standard pixel-art craft. The tell is the blur that generation and downscaling spread everywhere (D05-005), not the technique.
- Sources: S-D05-003, S-D05-043

### D05-N02 Bounded checkerboard or ordered dithering
- Why it is fine: A two-colour checker at a deliberate transition is one of the style's identifying features. Overuse as a default texture is the tell (D05-010).
- Sources: S-D05-030, S-D05-043

### D05-N03 Deliberate grid-breaking in human art
- Why it is fine: Some artists break the pixel grid on purpose, for example in background foliage, so one off-grid area is not automatically a tell; accidental, image-wide mixed sizes are (D05-003). Single forum anecdote; the example given was not checked.
- Sources: S-D05-011

### D05-N04 One-pixel outline or selective outline as a set-level choice
- Why it is fine: A 1px outline is the most common convention and thicker lines are allowed; sel-out is also standard. Any of them is fine when held across the whole set; only mixing them is the tell (D05-006).
- Sources: S-D05-003, S-D05-037, S-D05-042

### D05-N05 Large palette in a deliberately painterly style
- Why it is fine: A colour-heavy, soft-brushed style is a legitimate choice. In an itch.io thread, hand-made packs in that style were suspected of AI because of their colour count. Label the style honestly and don't market it as limited-palette pixel art, or readers will apply D05-004 to it.
- Sources: S-D05-040

### D05-N06 Seams, gaps and fringes caused by engine settings
- Why it is fine: Visible lines or gaps between tiles, and fringes around sprites, are often set by the engine through texture filtering, atlas padding or non-integer scaling. Hand-made art shows the same faults, and the fix is in the engine, not the art. Check these before applying D05-008 or D05-012. All three sources are search only.
- Sources: S-D05-057, S-D05-060, S-D05-063

## Open gaps
- No named pixel artist's complaint about AI pixel art has been found after searches of Bluesky, Mastodon, Lospec and Pixel Joint. The nearest items are Lux (S-D05-049, 2022), a first-hand quality statement written alongside a disclosure of AI use, not a complaint; a Bluesky bio stating a no-AI stance (S-D05-062); and a Pixel Joint thread on AI generation (S-D05-053, Jul 2023, search only, content unseen). The human-voice evidence here is anonymous commenters on Hacker News and itch.io.
- No study that detects AI pixel art or game sprites has been found. The only detection study in this file is general (Ha et al., S-D05-041), so the claim that these tells separate AI from human pixel art is untested.

## Sources
S-D05-001 | Sprite Fusion, "How to fix AI pixel art" (Pixel Snapper page) (vendor) | https://www.spritefusion.com/pixel-snapper/how-to-fix-ai-pixel-art | 2026 | guide | - | fetched
S-D05-002 | GIGAZINE, hands-on review of Sprite Fusion Pixel Snapper (mirrors the developer's pitch) | https://www.gigazine.net/gsc_news/en/20260516-spritefusion-pixel-snapper/ | 16 May 2026 | press | - | fetched
S-D05-003 | Pixel Joint, "The Pixel Art Tutorial" (TID=11299) | https://pixeljoint.com/forum/forum_posts.asp?TID=11299 | 27-28 Nov 2010 | forum | - | fetched
S-D05-004 | itch.io forum, "Let's Talk About AI in Game Dev" | https://itch.io/t/4975370/lets-talk-about-ai-in-game-dev | 11 Jun 2025 | forum | - | fetched
S-D05-005 | Pixel Engine, pixelate guide (vendor) | https://pixelengine.ai/guides/pixelate | 2026 | guide | - | fetched (by the lead)
S-D05-006 | Lospec, "Lospec will no longer be accepting AI-related art submissions" | https://lospec.com/articles/lospec-will-no-longer-be-accepting-ai-related-art-submissions | 12 Jun 2023 | policy | - | fetched
S-D05-007 | Anijam, "How to make pixel art with AI" (vendor) | https://www.anijam.ai/blog/how-to-make-pixel-art-with-ai/ | 2025-2026 | guide | - | search only (URL matched from search summary)
S-D05-008 | Dan Kornas, X post on inconsistent pixel sizes and drifting grid resolution | https://x.com/DanKornas/status/2086786116728807571 | undated | forum | - | search only (URL matched from search summary)
S-D05-009 | GamineAI, "How to make pixel art with AI for games" (vendor: promotes its own AI game-building product) | https://gamineai.com/blog/how-to-make-pixel-art-with-ai-for-games | 12 May 2026 | guide | - | fetched (r3; vendor status confirmed by the lead 20 Oct; quotes as reported by the gatherer)
S-D05-010 | Seeles, "AI pixel art generator for games" (vendor) | https://www.seeles.ai/resources/blogs/ai-pixel-art-generator-for-games | 2026 | guide | - | search only (URL matched from search summary)
S-D05-011 | Hacker News, "Good pixel art can be one-shotted by AI now" (commenters on block size, grid, palette, outlines, lighting and semi-transparent pixels; the poster describes a solo project; no comment on light direction as such) | https://news.ycombinator.com/item?id=44207304 | 7 Jun 2025 | forum | - | fetched (r2 via summary; lead spot-checked 20 Oct, r3)
S-D05-012 | Hacker News, "Show HN: AI game animation sprite generator" | https://news.ycombinator.com/item?id=44204181 | 2025 | forum | - | search only (URL matched from search summary)
S-D05-013 | Hacker News, "The curious case of retro demo scene graphics" (comment on sprite animation) | https://news.ycombinator.com/item?id=47574651 | undated | forum | - | search only (URL matched from search summary)
S-D05-014 | Seeles, "How we create AI sprite sheets" (vendor) | https://www.seeles.ai/resources/blogs/how-we-create-ai-sprite-sheets | 2026 | guide | - | search only (URL matched from search summary)
S-D05-015 | QuestStudio, "AI Pixel Art Sprite Sheets: Fix the Grid Before the Animation" (vendor) | https://queststudio.io/blog/ai-pixel-art-sprite-sheet-guide | 13 Sep 2026 | guide | - | fetched (r2)
S-D05-016 | Sprite Sheet Diffusion (arXiv 2412.03685) | https://arxiv.org/html/2412.03685v2 | 16 Mar 2025 (v2) | study | - | fetched (r2)
S-D05-017 | SpriteForge, "Why AI tilesets don't tile" (vendor) | https://www.spriteforge.tech/blog/why-ai-tilesets-dont-tile | 13 Aug 2026 | guide | - | fetched (r2)
S-D05-018 | Sprite AI, "Seamless pixel art tiles" (vendor) | https://www.sprite-ai.art/blog/seamless-pixel-art-tiles | 2026 | guide | - | search only (URL matched from search summary)
S-D05-019 | unfake.js (jenissimo), grid recovery and palette reduction, GitHub README | https://github.com/jenissimo/unfake.js/ | 2025 | guide | - | fetched (r2)
S-D05-020 | Hacker News comment recommending unfake.js | https://news.ycombinator.com/item?id=44874333 | 12 Aug 2025 | forum | - | fetched (r2, Algolia API)
S-D05-021 | Hacker News thread: __loam, AI pixel art "not actual pixel art" (16 Jan 2025); reply by AuryGlenz (id 42733893, 17 Jan 2025) guessing such output is downscaled after the fact | https://news.ycombinator.com/item?id=42731765 | 16-17 Jan 2025 | forum | - | fetched (r2, Algolia API; reply lead-verified)
S-D05-022 | Divoom, "Pixel art dithering: when to use and stop" | https://divoom.com/blogs/setup-ideas/pixel-art-dithering-when-to-use-and-stop | undated | blog | - | search only
S-D05-023 | qwe.edu.pl (QWE AI Academy), "Create pixel art with AI tools" (editorial tutorial, not a sales page; links to its own QWE AI app) | https://www.qwe.edu.pl/tutorial/create-pixel-art-with-ai-tools/ | 13 Feb 2026 | guide | - | fetched (r3)
S-D05-024 | Retro Diffusion (vendor site; palette-limit and true-grid claims) | https://retrodiffusion.ai/ | undated | guide | - | search only
S-D05-025 | PixelLab (vendor site; grid-based output and skeleton animation claims) | https://www.pixellab.ai/ | undated | guide | - | search only
S-D05-026 | Pixel Parmesan, "Dithering for pixel artists" | https://pixelparmesan.com/blog/dithering-for-pixel-artists | undated | blog | - | search only
S-D05-027 | SpriteLab, pixel art palettes guide (palette size by sprite size) | https://spritelab.dev/guides/pixel-art-palettes | undated | guide | - | search only
S-D05-028 | pixel-editor.com, colour theory for pixel art (hue shifting) | https://www.pixel-editor.com/articles/color-theory-for-pixel-art | undated | guide | - | search only
S-D05-029 | SLYNYRD, Pixelblog 5 "Back to basics" (clusters) | https://www.slynyrd.com/blog/2018/5/16/pixelblog-5-back-to-basics | 16 May 2018 | blog | - | search only
S-D05-030 | the-pixel.art, dithering article | https://the-pixel.art/articles/dithering/ | updated 1 Oct 2026 (per search snippet) | guide | - | search only (URL matched from search summary)
S-D05-031 | spritesheetgenerator.online, dithering pixel art guide | https://spritesheetgenerator.online/blog/dithering-pixel-art-guide | undated | guide | - | search only (URL matched from search summary)
S-D05-032 | GameLabs Studio, "The AI Game Development Lie" (why AI can't make game-ready spritesheets) (vendor) | https://gamelabstudio.co/blog/why-ai-cant-make-game-ready-spritesheets | 3 Aug 2026 | guide | - | fetched
S-D05-033 | DEV Community (@alvy, maker of SpriteFlow), from text prompt to sprite sheet (vendor) | https://dev.to/alvy/from-text-prompt-to-sprite-sheet-generating-game-ready-2d-character-animations-with-ai-3g7a | "Oct 8", year inferred 2026 | guide | - | fetched
S-D05-034 | Stork (Dani Roth), why an AI pattern has a seam (vendor, sells a pattern generator) | https://www.stork.ai/blog/why-ai-pattern-has-a-seam | 15 Jun 2026 | guide | - | fetched
S-D05-035 | GIGAZINE, hands-on review of Unfaker (unfake.js demo) | https://gigazine.net/gsc_news/en/20251202-unfaker-fix-ai-pixel-art/ | 2 Dec 2025 | press | - | fetched (lead-verified r2)
S-D05-036 | DEV Community (handsupmin), why AI pixel art looks fake (MonoPix, free MIT tool) | https://dev.to/handsupmin/why-ai-pixel-art-looks-fake-and-how-i-turned-it-into-real-pixel-art-5b1b | 22 Mar 2026 | blog (tool-maker, sells nothing) | - | fetched
S-D05-037 | Monojog, keeping pixel art consistent across an indie game (craft advice) | https://drmonojog.com/keeping-pixel-art-consistent-across-an-indie-game/ | 6 Oct 2026 | blog | - | fetched
S-D05-040 | itch.io comment thread on a hand-made rock-pile asset pack suspected of AI over its colour count | https://itch.io/post/9242362 | about 2024 | forum | - | fetched
S-D05-041 | Ha et al., "Organic or Diffused: Can We Distinguish Human Art from AI-generated Images?" (CCS 2024): detectors and expert artists flag human art as AI at high rates | https://arxiv.org/html/2402.03214v3 | 2 Jul 2024 (v3) | study | - | fetched
S-D05-042 | Lospec, pixel art outlines | https://lospec.com/articles/pixel-art-outlines/ | 3 Apr 2016 | guide | - | fetched
S-D05-043 | ArtTechniques, pixel art techniques (hand-placed anti-aliasing, checker dithering) | https://arttechniques.com/techniques/pixel-art | 2026 (page says © 2026) | guide | - | fetched
S-D05-046 | Urban Dictionary, "mixels" (human usage predates AI) | https://www.urbandictionary.com/define.php?term=mixels | 2009 | other | - | search only
S-D05-047 | Flowlab community, "(Mini rant) STOP USING MIXELS" (human pixel art) | https://community.flowlab.io/t/mini-rant-stop-using-mixels/38287 | about 2022 | forum | - | search only (HTTP 403)
S-D05-048 | Sorceress, AI tileset generator (halos and fringes on transparent edges) (vendor) | https://sorceress.games/blog/ai-tileset-generator-game-ready-tilesets-from-a-prompt | 2026 | guide | - | search only
S-D05-049 | Lux (@thisislux), Pixel Parmesan, "AI and the Future of Pixel Art" (first-hand, named artist; a disclosure and workflow post, not a complaint) | https://pixelparmesan.com/blog/ai-and-the-future-of-pixel-art | 8 Nov 2022 | blog | - | fetched
S-D05-050 | Hacker News comment, "…not pixel art in the sense I understand it" (same thread as S-D05-011; counts with it) | https://news.ycombinator.com/item?id=44208033 | 2025 | forum | - | search only (title snippet)
S-D05-051 | Hacker News, "Show HN: Fixing Google Nano Banana Pixel Art with Rust" (commenters mention inconsistent lights and shadows, and palette issues) | https://news.ycombinator.com/item?id=46058566 | date not seen | forum | - | search only
S-D05-052 | itch.io, "Broken pixel outlines in purchased asset pack" (buyer reports 1px and 2px outlines mixed; a reply says the pack is marked AI-assisted) | https://itch.io/t/6294084/broken-pixel-outlines-in-purchased-asset-pack | about 172 days before the search (no absolute date) | forum | - | search only
S-D05-053 | Pixel Joint forum, "Pixel Joint Forum: AI pixelart generation" (TID=27553) (listed by the gatherer without a claim; not cited by any tell) | https://pixeljoint.com/forum/forum_posts.asp?TID=27553 | 21 Jul 2023 | forum | - | search only
S-D05-054 | Pinnguaq, "Pixel Art 3B: Advanced Tiles In GraphicsGale" (educational publisher, non-vendor; human-craft lesson, not about AI) | https://pinnguaq.com/learn/pixel-art/pixel-art-3b-advanced-tiles-in-graphicsgale/ | 13 Jan 2020 | guide | - | fetched
S-D05-055 | DEV, nonatofabio, "AI Generated pixel art needs a build system, not better prompts" (says the light source can move between sprites) | https://dev.to/nonatofabio_28/ai-generated-pixel-art-needs-a-build-system-not-better-prompts-280c | about 42 days before the search (no absolute date) | blog | - | search only
S-D05-056 | Elseland, "How to Generate Pixel Art Game Assets With AI" (vendor status unchecked; halo and matte contamination in a diagnosis table) | https://www.elseland.ai/blog/ai-pixel-art-game-assets | 2026 (diagnosis table dated 20 Aug 2026 per summary) | guide | - | search only
S-D05-057 | BG Clear, "Sprite Background Remover: Keep Pixel Edges and Frame Size" (vendor; also the engine-filtering point) | https://www.bgclear.ai/blog/background-remover-for-game-assets/ | updated Sep 2026 per summary | guide | - | search only
S-D05-058 | Seeles, "How We Generate Pixel Art with AI: Complete Guide" (vendor; a different page from S-D05-010 by the same vendor, so counts once with it; alpha bleed) | https://www.seeles.ai/resources/blogs/ai-generate-pixel-art-game-assets | undated | guide | - | search only
S-D05-059 | Pixel-editor.com, "Pixel Art Outlines & Anti-Aliasing: Complete Guide" (listed by the gatherer without a claim; not cited by any tell) | https://www.pixel-editor.com/articles/pixel-art-outlines | undated | guide | - | search only
S-D05-060 | Godot forum, "Tilemap misalignment by one pixel?" (engine side) | https://forum.godotengine.org/t/tilemap-misalignment-by-one-pixel/114361 | undated | forum | - | search only
S-D05-061 | Makerfern, "Why Your Transparent PNG Has a Checkerboard" (vendor status unchecked) | https://makerfern.com/blog/transparent-png-checkerboard | undated | blog | - | search only
S-D05-062 | Bluesky profile bio of a pixel artist stating no AI use (a stance, not a complaint; not cited by any tell) | https://bsky.app/profile/pixelartbyme.bsky.social | undated | bio | - | search only
S-D05-063 | Bugnet, "Fix: Godot Sprites Showing Black Lines or Gaps Between Tiles" (engine side) | https://bugnet.io/blog/fix-godot-sprites-black-lines-gaps-between-tiles | undated | blog | - | search only
(IDs S-D05-038, 039, 044 and 045 were reserved in the raw file but not used.)
