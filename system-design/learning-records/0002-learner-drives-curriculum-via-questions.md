# Learner drives the curriculum by asking; live-vs-stored taught as Lesson 2

**Date:** 2026-07-15
**Status:** Active

## What happened

Lesson 1 ended with an `ask-teacher` box offering example questions, one of which was "curious how this changes for a live video vs. a stored one?" The learner took that exact bait and asked it. Lesson 2 was therefore **live vs stored video**, not the planned *One Server Becomes Many* (load balancers), which is deferred to Lesson 3+.

## Why this matters (non-obvious bits)

1. **The bait worked, so keep baiting.** The example questions in the `ask-teacher` box are not decoration — they function as a menu that shapes the curriculum. Continue seeding each lesson with 3–4 genuinely tempting questions, because the learner picks from them. This is a cheap, working steering mechanism.
2. **Curiosity-driven mission means detours are correct, not disruptive.** Per [[0001-mission-established]] there's no deadline and no interview. A question asked is a moment of maximum motivation; answering it beats defending a lesson order. Don't feel obliged to preserve the backlog sequence.
3. **He asked a "how does X change" question, which is a derivation question.** He wasn't asking for two facts — he was asking for a delta. That's a good instinct and worth reinforcing explicitly, so the lesson was built around *deriving* every difference from one root fact (the next segment doesn't exist yet) rather than presenting two parallel architectures to memorise.

## Evidence status

- **Lesson 1: still not demonstrated.** He never did the Lesson 1 quiz (or didn't report it). Asking a good follow-up question shows engagement, *not* mastery. Lesson 2 hedges by including a recall card that pulls Lesson 1 material (DNS/latency) forward — spacing. **Still no hard evidence either lesson landed.** Next session, ask him to answer something from Lesson 1 cold before piling on.
- Lesson 2 deliberately introduced "a cache near you / the edge" *without* teaching CDNs, to build felt need for that lesson. Two lessons have now gestured at it.

## Implications for next session

- Offer a genuine choice: **CDNs** (now well-motivated, and the streaming anchor's centre of gravity) vs **load balancers** (twice promised, still owed). Let him pick; both are in ZPD.
- Open question surfaced but not taught: adaptive bitrate. `RESOURCES.md` gap says find a source first.
- If he picks neither and asks something new — that's the pattern working. Follow it.

## Research note

Streaming has an unusually bad secondary-source ecosystem: search results contradicted each other on cache-hit ratios, and a popular stat traced back to an article that doesn't contain it. Grounded the lesson in RFC 8216 + Fastly + Netflix's own docs instead. See the Gaps section of `RESOURCES.md`. Apple's HLS developer docs are JS-rendered and cannot be fetched — use the RFC.
