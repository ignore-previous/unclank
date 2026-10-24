---
name: unclank-quiz
description: Pre-release check for quizzes, tests, exams, question banks, multiple-choice items and flashcards, before they are printed, handed out or published. It finds the item flaws that make a quiz unreliable or easy to game, such as a wrong or doubled key, the right answer being the longest option, a skewed answer position, cues in the stem, weak distractors, praise-heavy feedback and wordy flashcards. Use it whenever someone asks to check, review, proofread or fix a quiz, test or exam, whoever wrote it, or asks why their quiz feels machine-made. It also covers writing items and feedback during a build.
---

# unclank-quiz

Checks the items a learner meets: stems, options, keys, explanations, feedback and flashcards, one by one and as a set. Most of these flaws are old item-writing faults, and human writers make them too. AI generation makes some of them more frequent, and the worst ones (a wrong key, two right answers) hurt learners, not only style. The research suggests readers and test-takers react to **clusters** and to sets that are too even, not to single hits.

Every check here comes from evidence-backed research. Each one has a tell ID (e.g. [D09-001]). The reasoning, dates and sources are in `references/evidence.md`. Read an entry there before telling someone that a hit matters, when they push back, or when you need the fix details. Most studies tested older models, so treat the rates as a guide to what to check.

## Modes

- **Audit mode** (the default when asked to "check", "review" or "audit"). Report the hits first and change nothing until the user asks for fixes. Follow "How to audit" below.
- **Build mode** (when writing items, feedback or cards). Apply the checklist as you write, so the flaws never appear. Mention briefly what you set. Don't produce an audit report or the UNCLANK-AUDIT block. List anything you couldn't finish (a file you can't create or delete, a fact to verify) as next steps for the user. Details are under "Build mode rules" at the end of the checklist.

## Not a tell: don't flag or "fix" these

- Clean grammar and spelling. It is care, not a flaw, though the content still needs checking [D09-N01].
- Options of about equal length and consistent formatting. That is good practice. The tell is a key that is longer than its distractors [D09-N02].
- Few true/false items in a multiple-choice set. Not misusing that format is fine [D09-N02].
- A cue flaw taken as proof that AI wrote the item. Humans make these flaws too [D09-N03].
- Students rating the items as fine. That is no proof the items discriminate or that the keys are right, so still run the checks [D09-N04].

## Checklist

Labels: **Avoid** means fix it before the items ship. **Choose deliberately** means it's fine if it was chosen, and a signal when it's an unchosen default. Confidence: **strong** means 3+ independent sources, **moderate** means 2, **anecdotal** means one opinion, so treat it as a hint.

### Correctness (check these first, item by item)
- [Avoid · strong] **Wrong key or confident factual error** [D09-010]. For each item, work out the answer yourself from the stem, then compare with the marked key. Check every stated fact in the stem, options and explanation. Where a source passage was supplied, the key must be traceable to it. If you are not sure, write "verify with a subject expert". Never pass an item silently. A second model's check is not enough.
- [Avoid · moderate] **More than one defensible answer, or none** [D09-004]. Test every distractor against the stem: could it be right in some reasonable reading? Flag an item if two options can be defended or if no option fits. When you can't judge, list it under "Check this" with "verify with a subject expert".

### Cues that give the answer away
- [Avoid · moderate] **Key is the longest option** [D09-001]. Count the characters of each option. One item is a hit when the key is clearly longer, about a quarter longer than the next-longest option. A key only a few characters longer is not a hit on its own [D09-N02]. Also compare detail: a precise, hedged key next to short vague distractors is the pattern. Across a set of 8 or more, count how often the key is the strictly longest. Report it as a set finding if it is well above chance (about 1 in 4 for four options), and count near-ties separately. A near-tie between an equally specific key and distractor is not a hit and needs no "Check this" entry; count it only in the set tally. The quarter-longer cut-off is an editorial rule of thumb, not a figure from the research.
- [Avoid · moderate] **Stem-to-key cues** [D09-002]. One item is enough. List the content words the stem shares with each option, and flag a key that repeats the stem's words more than the distractors do. Search stems and keys for absolute terms ("always", "never", "all", "only", "none") and for logical hints, such as a stem that grammatically fits only one option.
- [Avoid · moderate] **Answer-key position skew** [D09-003]. Needs a set of about 12 or more items. Tally the key's position (A, B, C, D) across the set. Flag it if one position holds far more than its share, or one is almost never used (model output often underuses D). A fixed repeating order, such as A, C, B, D over and over, is a skew too. With fewer than 12 items, flag only an extreme skew, such as half the keys in one position. If the keys are in code, check whether options are shuffled after generation. An option clearly meant as an abstention, such as "Not sure" or "I don't know", is a design choice, not skew. Leave only that option out of the tally, say how many answer options remain, and keep checking skew and fixed cycles among them. Any other option that is never the key still counts. This exception is editorial judgement, not research. Report it as "Choose deliberately" only when the files show the quiz is scored and the abstention option is never the key.
- [Avoid · anecdotal] **"All of the above" and "None of the above" filler** [D09-006]. Search the options for these phrases. Flag all-of-the-above. Flag none-of-the-above unless it is the tested key of a deliberate item. They are rare in AI items, so treat a hit as a low-priority check.
- [Avoid · anecdotal] **Negative stems** [D09-012]. Search stems for "NOT", "EXCEPT", "least likely" and "which is false". Flag each one as low priority and offer the positive form. A clearly marked "which is the exception" stem is fine.

### Distractors and difficulty
- [Avoid · moderate] **Weak or implausible distractors** [D09-005]. Read each distractor and ask what real mistake would lead a learner to pick it. Flag options no one would choose: obviously absurd, off-topic or a rephrased key. If response data exists, flag any option chosen by under 5% of learners. Without response data, mark the finding "inferred" and don't claim the distractor fails.
- [Avoid · moderate] **Recall-only items and flat, easy difficulty** [D09-007]. Needs a set. Label each item remember, understand, apply or analyse. Flag a set that is mostly remember and understand, or has no scenario items. If the user asked for a level and the items land below it, flag that too. Difficulty from real learner data is the confirming check.
- [Avoid · moderate] **Weak item discrimination** [D09-014]. This can't be seen in one item. Check only if response data from a pilot or live run is supplied: flag items whose discrimination index is 0.20 or less. Otherwise say it needs a pilot and make no hit. Don't judge items by difficulty alone.

### Explanations and feedback
- [Avoid · moderate] **Explanation that doesn't name the misconception** [D09-009]. Read each explanation. Flag one that only restates the key, gives a general walkthrough, or names no mistaken idea behind any distractor. A line per distractor naming its misconception is the fix, not the test.
- [Avoid · moderate] **Praise in feedback** [D09-008]. Search feedback text for praise openers ("Great question", "Great job", "Well done", "Excellent", "Good work"). Check open-ended feedback hardest. Feedback should give the reason and name the learner's specific error. Praise in feedback on a wrong answer is the clearest case.

### Flashcards
- [Avoid · moderate] **Cards that lack context, take several answers, or run wordy** [D09-013]. Read each card on its own. Flag a card whose answer needs the source text to make sense, a card with more than one valid answer or fact, and a long card. Spot-check some cards against the source for invented facts.

### Sets of items
- [Avoid · anecdotal] **Repetitive templates** [D09-011]. Needs a set. Compare stem openings and skeletons ("Which of the following…", "What is the primary…"). Flag it when most of the set shares one stem skeleton, or items vary only in a noun or number. A few stems with the same opening are normal. Explanations and feedback that follow one consistent layout, such as a line per option, are good practice, not this tell. Report it as a set finding.

### Build mode rules
- Trace every key to a source passage, and tell the user which keys still need a human check [D09-010].
- Test each distractor against the stem so only one option is defensible [D09-004].
- Keep options at the same length and detail, and keep the key from being the longest [D09-001].
- Write the key in different words from the stem, with no absolute terms [D09-002].
- Shuffle option order in code after generation, keeping any abstention option such as "Not sure" last, then check the position tally [D09-003].
- Build distractors from real learner misconceptions, not filler [D09-005, D09-006].
- Set a level for each item, with scenarios for apply and analyse items, and use varied stem shapes [D09-007, D09-011].
- Write explanations that name the misconception behind the wrong answer, with no praise opener [D09-009, D09-008].
- Make each flashcard one fact that stands alone [D09-013].

## How to audit

1. **Find the items:** question files, JSON or code arrays, markdown quizzes, flashcard decks, feedback templates, and any answer-key or response data. Note the item count, as some checks need a set.
2. **Run every check** in the checklist. Read the items; don't guess. Work out each answer yourself. A hit needs evidence you can point to. Report a Choose deliberately item only when the files show the default; you can't see intent, so say it may be deliberate. When you can't judge something (no source passage, no response data, a fact outside what you know), it isn't a hit: list it under "Check this" with "verify with a subject expert", and keep it out of the audit block.
3. **Separate item hits from set hits.** Item hits get a file and the line of the item or its key. Set-level hits (position skew, repeated templates, flat difficulty, longest-key rate) are reported in their own group.
4. **Write the report:**
   - Item hits first, with correctness hits at the top. Give each hit its tell ID, file and line, what you saw, and the fix in one line.
   - Then the set-level findings, each with its count or tally.
   - Say how many hits there are, and whether they form a cluster.
   - List the checks that passed, and the checks you couldn't run, in one line each, then the "Check this" items.
5. **End with the audit block,** exactly in this form. Use one line per hit, and leave out the "Check this" items. The label is exactly `Avoid` or `Choose deliberately`; for an inferred hit, start the note with `inferred:`. For set-level hits give the file and `-` for the line. If there are no hits, write the two marker lines with nothing between them.

```
UNCLANK-AUDIT
D09-001 | Avoid | quiz.md:42 | key is the longest option (88 vs 41, 39, 44 characters)
D09-003 | Avoid | quiz.md:- | key is B in 9 of 12 items, D never
END-UNCLANK-AUDIT
```

## Ground rules

- Check your own or the user's work. Cue flaws don't prove AI wrote an item, and you must not accuse anyone: human item writers make the same flaws [D09-N03].
- Never pass a key you haven't checked. If you can't verify it, say so and name who should.
- Don't flag anything on the Not a tell list. When unsure, say "check this" rather than calling it a hit.
- In audit mode, change nothing until the user asks.
- For the general writing style of stems, explanations and feedback, use `unclank-prose` once it's released (planned).

Last reviewed: 21 Oct 2026. Evidence: `references/evidence.md`. Full research: `research/domains/D09-educational-content.md`.
