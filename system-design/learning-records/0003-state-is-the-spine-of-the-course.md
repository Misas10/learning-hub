# "Where does state live?" is the spine of the course

**Date:** 2026-07-16
**Status:** Active
**Supersedes:** the backlog ordering in [[0001-mission-established]] (load balancers were "Lesson 2"; they landed as Lesson 3)

## What happened

Learner chose load balancers over CDNs when offered the pick at the end of [[0002-learner-drives-curriculum-via-questions]]. Delivered as Lesson 3, *One Server Becomes Many*. Lesson 1's promise ("Lesson 2 — One Server Becomes Many") has been rewritten to point at Lesson 3; nav links across all three lessons reconciled.

## The key structural decision

The lesson does **not** teach load balancers as a traffic-cop box. It teaches them as the thing that forces **interchangeability**, and derives everything from that one root fact:

> you don't control which server gets your request → servers must be interchangeable → state in a server's memory breaks that → so either sticky sessions (the cheat) or move state out (the fix) → "out where?" *invents* the database and the cache by necessity

**This reframes the whole course.** From here, the through-line is *where is state allowed to live, and what does that cost* — databases, caches, CDNs, replication, sharding, and consistency are all answers to a question he now has a felt need for, rather than topics from a list. Use that framing explicitly in future lessons; don't quietly drop it.

## Why this framing (non-obvious)

- Per NOTES.md, he responds to **delta/derivation questions**, not parallel fact-lists. Lesson 2 derived everything from "the next segment doesn't exist yet"; Lesson 3 derives everything from "you don't pick the server." **Third data point: this structure is now the course's house style.** Two root-fact lessons in a row also let Lesson 3 name the recurring pattern out loud ("every solution creates the next problem") — that meta-observation is only available *because* the structure repeats.
- Availability was taught as a **consequence** of interchangeability, not a separate feature. The point that the box named "load balancer" is also how you survive a 3am machine fire is the non-obvious bit worth reinforcing later.
- L4/L7 was deliberately kept to two paragraphs. It's the classic interview-flashcard content and it's the *least* interesting thing here; it would have eaten the working-memory budget that the state insight needed.

## Evidence status — still the open problem

**Three lessons delivered. Zero demonstrated.** He has never reported a quiz result or answered a recall prompt back. Engagement is high (he asks good questions, he picks) but that is *not* mastery — this is exactly the fluency-vs-storage illusion, and it's now compounding, since Lesson 3 assumes Lesson 1's DNS material.

Mitigations in place: Lesson 3 has a recall card pulling Lesson 1 (what does DNS return now?) and an interleaved card pulling Lesson 2 (is a pre-filled CDN cache "state"? — answer: yes, but *rebuildable* state, which is the distinction that matters). **Next session: open by asking him to answer one cold, before teaching anything new.** If he can't walk the interchangeability chain, re-teach rather than proceed.

## Research note

The load-balancing SEO layer is as bad as streaming's — a blog's "least connections is the best default" contradicted NGINX's own docs. Grounded in the primer + NGINX + Google SRE instead. This is now a standing rule in `RESOURCES.md` Gaps. Lesson 3 mentions this disagreement *in the lesson itself* as a live worked example of source evaluation — a small dose of teaching him to distrust content farms, which serves the "reason about a system I've never seen" mission goal.

## Implications for next session

- Offer: **database** (where state goes — the natural next beat, and the lesson practically demands it) or **CDN** (owed since Lesson 2, and the streaming anchor's centre of gravity). Database follows the derivation more tightly; CDN serves the anchor systems better. Either is in ZPD.
- Threads deliberately left dangling in the ask-box: shared session store as the *new* SPOF (best of them — he'd be deriving the next problem himself), in-flight requests when a server dies, WebSockets vs round-robin, why the LB doesn't just cache responses.
- Still blocked: adaptive bitrate (no good source yet — see `RESOURCES.md`).
