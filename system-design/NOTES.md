# Teaching Notes

## Learner profile
- **Level:** Early-career developer. Codes comfortably, has built apps. New to distributed-systems vocabulary.
- **Motivation:** General curiosity, no deadline. Learns best when concepts are tied to real apps he uses.
- **Anchor systems:** Streaming/media (YouTube, Netflix, Spotify) + social feeds/chat (Twitter, WhatsApp, Discord).

## Teaching preferences
- Keep lessons short and finishable in one sitting (small working-memory budget).
- Always ground abstract concepts in a concrete, familiar app before generalising.
- Optimise for **storage strength** (long-term retention), not just in-the-moment fluency: use retrieval practice, spacing, and interleaving.
- Cite sources inline so claims are trustworthy.

## Preferences log
- 2026-07-15: Chose "general curiosity" + "early-career". No interview pressure — favour depth of understanding over templates. Excited by streaming + social/chat systems specifically.
- 2026-07-15: **Asks follow-up questions from the `ask-teacher` box, and they redirect the curriculum.** He picked the live-vs-stored question and it became Lesson 2, bumping load balancers. Keep seeding each lesson with tempting questions — it's a working steering mechanism. Detours are correct for a curiosity-driven mission.
- 2026-07-15: His question was a *delta* question ("how does X change vs Y"), not a facts question. Lessons that derive consequences from one root constraint seem to suit him better than parallel fact-lists. Reinforce this.
- 2026-07-16: **Root-fact derivation is now the course's house style** (3 lessons, 2 built this way). Each lesson: one root fact → derive every consequence. Bonus: repeating the structure let Lesson 3 name the meta-pattern ("every solution creates the next problem"). Keep doing this.
- 2026-07-16: Chose load balancers over CDNs when offered a straight pick. He does engage with the choice rather than deferring — keep ending lessons with a real fork.

## Course through-line (established Lesson 3)
**"Where does state live, and what does it cost?"** — Lesson 3 derives the database/cache from necessity rather than announcing them. Databases, caches, CDNs, replication, sharding, consistency are all *answers* to this one question. Frame future lessons against it explicitly. See [[0003-state-is-the-spine-of-the-course]].

## ⚠️ Standing concern: no demonstrated mastery
Three lessons delivered, **zero quiz/recall results ever reported**. High engagement ≠ learning — this is the fluency illusion the mission explicitly warns against, and it now compounds (Lesson 3 leans on Lesson 1's DNS). **Open the next session by asking him to answer one cold, before teaching anything new.**

## Ideas for future lessons (backlog)
- **Database / where state goes** — Lesson 3 ends by demanding it. Tightest follow-on.
- **CDNs / edge caches** — owed since Lesson 2; Lessons 1–3 all gesture at "a cache near you". Best serves the streaming anchor.
- The shared session store as the *new* single point of failure — teased in Lesson 3's ask box; he'd be deriving the next problem himself.
- Failure & overload — good source now in RESOURCES (Google SRE, "Handling Overload"): cascading failure, graceful degradation.
- Adaptive bitrate (how the player switches quality) — teased in Lesson 2's ask box. **Blocked:** need a good source first, see RESOURCES.md gaps.
- Latency numbers every engineer should know (why memory > disk > network).
- Databases 101: SQL vs NoSQL, and why feeds often use NoSQL.
- Caching + CDNs (perfect for the streaming anchor).
- Replication & sharding.
- The CAP theorem / consistency vs availability.
- Message queues (how chat + notifications get delivered).
- Case study: design Twitter's timeline (fan-out on write vs read).
- Case study: how Netflix/YouTube stream video (CDN, adaptive bitrate).
