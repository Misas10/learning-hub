# Mission: System Design

## Why
I'm curious how the huge systems I use every day actually work — how YouTube/Netflix/Spotify stream to millions, and how Twitter/WhatsApp/Discord deliver feeds and messages instantly. I want to be able to open the hood on any large app and understand, in real terms, how it's built and why.

## Success looks like
- I can trace what happens end-to-end when I press "play" on a video or load a social feed — naming each component and why it's there.
- I can explain the core building blocks (servers, load balancers, databases, caches, queues, CDNs) and when each is used.
- Given a familiar app (e.g. "design Twitter's timeline"), I can sketch a reasonable architecture and defend the trade-offs.
- I understand the big trade-offs (consistency vs. availability, latency vs. cost) well enough to reason about a new system I've never seen.

## Constraints
- No deadline — this is curiosity-driven, so we optimise for durable understanding over interview cramming.
- Early-career developer: comfortable coding and building apps, but distributed-systems vocabulary (sharding, replication, consistency) is currently fuzzy.
- Learning happens across many short sessions; each lesson must be small enough to finish quickly.

## Out of scope (for now)
- Interview-specific tactics and time-boxed mock drills (may revisit if the mission shifts).
- Deep infrastructure/DevOps (Kubernetes internals, cloud billing, Terraform).
- Writing production distributed-systems code — we focus on understanding and design, not implementation.

## Anchor systems
Whenever possible, teach with examples from **streaming/media** (YouTube, Netflix, Spotify) and **social feeds/chat** (Twitter, WhatsApp, Discord).
