# Trial log — makefun-meeting-oneline

Program: The Meeting That Should Have Been One Line — $2, slug
`u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c`,
deadline 26 Nov 2026 21:30 WITA (2026-11-26T13:30:00Z). Harness program/v1.
Repo: `makefun-meeting-oneline`. Wallet (agent):
`FwUebjzYUBF6uybmEkUkiQf9z35bGGQuUE3GrToXFcUq`.

## Gate (from `rules` STRING in comp-meeting.json, read in full 25 Nov 22:44 WITA)

- `/output/entry.txt` must be UTF-8 text of **1 to 200 characters**, not only
  white space. Only a valid entry goes before the judge; invalid = listed
  with 0, no rate, no prize.
- Judge: pairwise, model z-ai/glm-5.3-flash via OpenRouter; superbot,
  reasoning high, max 12,100 output tokens per verdict. Brief weighs, most
  important first:
  1. is a single line, one sentence that could have replaced an entire
     pointless meeting, unmistakably office humor, and loses to any
     one-liner that kills a pointless meeting;
  2. kills the meeting outright: after this line, no one could justify
     holding the meeting at all;
  3. feels relatable to anyone who has sat through a useless meeting,
     drawn from real office life;
  4. lands as a joke, with a turn or a sting that makes it funny rather
     than merely true;
  5. stands alone as a single line, needing no context or explanation.
- Length for its own sake does not count. Each game = two calls (both
  orders); margin 1–5; winner takes 0.5 + margin/10 per call.
- 3 fixed house texts (anchors) + 3 rungs play in development heats only; an
  entry byte-identical to one of them shares its rate and never enters the
  playoff; an entry reproducing one (same bytes, or same words after
  case/whitespace) takes no prize. Anchors/rungs revealed only in the final
  kit — avoid any stock one-liner that could be a house text.
- Final heat: top 500 on the dev board (+ unrated entries); 3 Swiss rounds +
  playoff of top 5. Prizes: 1st $2 (total $2, winner takes all).
- Blind rounds: nothing judged/shown at submit time; rounds at cutoffs;
  latest entry (or picked final) is the one that counts. Max 5 submissions
  per entrant per UTC day.
- Entry text shows on the public Feed from the moment its dev grade is
  recorded.
- Submission names a public GitHub repo + commit + AI session transcripts;
  repo must have been created after the competition opened.
- README must carry 3 LIVE make.fun badges (program badge, rank badge,
  reward badge); a README with only static badges is refused by the server
  (422 repo_readme). Rank/reward badge URLs use the REPO NAME after the
  owner segment, not the slug.
- Repo must contain `.makefun/owner.json` with the agent wallet (server 422
  repo_owner without it).
- GitHub About (homepage + topics makefun, ai-agents, bounties) must be set
  before submit; topics via PUT names[], verified with `gh api`.

## Self-dup bar (strict, from the brief)

Our existing Meeting entry `01a21227…` is: "Our AI notetaker summarized
the hour-long meeting in one line: 'This should have been an email.'"
Its mechanism: meeting INFRASTRUCTURE (an AI notetaker) delivers the
verdict. This entry is allowed ONLY with a mechanism / voice / turn that
is genuinely different: no notetaker or AI summarising or delivering a
verdict again, no infrastructure / room / booking behaving like a person.
If no clearly different angle existed after serious research, the correct
result was SKIP, not a near-duplicate.

## Field research (live API via curl, 25 Nov ~22:45 WITA)

- Live `submissionCount`: 1,059 titles fetched (22 pages x 50, last page 9);
  live comp count at check time: 1,071 (field still growing).
- Titles: 1,059 total, 0 empty. 361 are exactly the competition name
  (354 exact-case + 6 lowercase + 1 variant). Unique non-empty titles: 673.
- Denominator (real entry-bearing titles): 218 sentence-like unique titles
  (length > 40 chars, or a sentence with a period). The rest are display
  names ("Proper Signal", "Cardinal Orbit") or short title fragments.
- Saturated families (exact counts over the 673 unique titles,
  case-insensitive grep, hits read):
  - email (any): 109 — "should have been an email" 10; the email nobody
    read / the email that deleted the meeting / thumbs-up email, all taken.
  - nothing / nobody / no decision: 74 — "Nothing changed, nobody is
    blocked, and the deadline is still Friday" is the flagship of this
    family.
  - one line / one sentence (meta): 70, mostly comp-name variants.
  - another meeting / follow-up / schedule another: 39 — "We spent an
    hour deciding nothing, then scheduled another meeting to decide what
    this one was supposed to decide." Family exhausted.
  - cancel: 33. minutes (meeting length): 31. calendar invite: 23.
  - decision already made: 22 — hallway decision 8 ("Nobody in this
    room can approve this, and everyone who can already said yes in the
    hallway."), "The decision was made in the first three minutes..."
  - agenda: 13 — including the full sentence "The agenda had one item;
    the meeting had forty-five minutes; the item never came up."
  - deck / slides: 10. action item: 9. room: 9.
  - mute / camera off: 2, but one is strong ("Everyone is on mute,
    nobody is listening, and the recording will never be watched...").
  - notes: 2 ("I spent 47 minutes taking notes on a meeting whose only
    decision was to schedule another meeting...").
  - notetaker / AI summarise: 0 in the field — but that is OUR old entry,
    so it is banned for us regardless.

## Candidate shortlist (all checked against the 673 unique titles)

- **"The coffee went cold before anyone said anything new." — CHOSEN
  (53 chars).** Grep, case-insensitive, unique titles: "cold" 0, "coffee"
  1 (only the title fragment "The Coffee-Machine Decision", no sentence,
  no cold coffee), "went" 0, "said anything" 0, "anything new" 0,
  "nothing new" 0. Mechanism: a passive object (the coffee) plus elapsed
  time as the evidence — the cup cools in minutes, and in all that time
  nobody said one new thing, so the meeting had no content and no reason
  to exist. Voice: an attendee's plain observation; nobody delivers a
  verdict, nothing infrastructural acts like a person, no AI, no summary,
  no email, no second meeting, no agenda, no decision already made
  elsewhere. Turn: a race the meeting loses to a cooling drink. Kill:
  "before anyone said anything new" means zero new information across
  the whole meeting — universal, not personal. Relatable: coffee going
  cold in a long meeting is a shared office experience. Self-dup vs our
  old Meeting entry: mechanism (object + time as evidence vs AI
  notetaker delivering a verdict), voice (attendee observation vs
  notetaker's reported summary), and turn (race against cooling vs
  quoted verdict) are all different. Not a stock phrase; not a plausible
  house anchor.
- "I declined this meeting in my head an hour ago; my body just took
  sixty minutes to catch up." — runner-up. Grep: "in my head" 0,
  "my body" 0, "sixty minutes" 0; declined family has 2 hits but with a
  different mechanism (already decided + emailed + formally declined).
  Mechanism (internal decision vs physical attendance) is genuinely
  different and funny, but the kill is personal — it says the meeting
  was pointless for me, not that no one could justify holding it — so
  it scores worse than the coffee line on judge criterion 2.
- "The agenda had one item, and we spent an hour avoiding it." — KILLED.
  The field already holds "The agenda had one item; the meeting had
  forty-five minutes; the item never came up." Same mechanism, same
  turn, only the wording differs.
- Absent-decider ("Nobody in this room can approve this...") — KILLED.
  Already in the field twice, in near-identical form.
- Camera-off ("Everyone had their cameras off...") — KILLED. "camera" is
  0 hits, but the mute entry ("Everyone is on mute, nobody is
  listening...") is the same mechanism with a different device.
- Hallway / elevator decision — KILLED. 8 hits; decision-already-made
  family (22) is saturated.
- Lunch as a clock ("We ordered lunch before the meeting started and
  finished it before anyone said anything that mattered.") — "lunch" has
  2 hits, both title fragments, so the family is near-empty; but the
  mechanism is the same clock-race as the coffee line, and coffee is
  tighter, shorter, and more universal than lunch.
- Yawn / nodding / standing up to leave — "yawn" 0, "stood up" 0,
  "nodded" 0, but each draft was either a weak turn or a re-skin of a
  saturated family (nodding = decision-already-made; standing up =
  leaving-early, no sting).

## Entry

"The coffee went cold before anyone said anything new." — 53 characters
(Python `len()`), one sentence, one line, UTF-8, inside the 1–200 gate.

## Verification (to be filled after build)

- `main.py` run locally writes the entry to `/output/entry.txt`.
- HEAD local = `git ls-remote` HEAD; tree clean.
- README: `make.fun/badge/` count = 3; repo name in rank/reward badges.
- `.makefun/owner.json` present with the agent wallet above.
- No forbidden static-badge token anywhere in the repo (grep per repo = 0).
- Kit `bundle_sha256` matches live API: `fd33dba1…` (checked 25 Nov 22:45).
- Bundle + re-check: see report to coordinator.
