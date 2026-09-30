# System Design Resources

Curated, high-trust sources. Knowledge for lessons is drawn from here — not from parametric guesses.

## Knowledge

- [The System Design Primer — Donne Martin (GitHub)](https://github.com/donnemartin/system-design-primer)
  Free, hugely popular open-source guide. Plain-English breakdowns of scaling, replication, caching, load balancing, plus worked example designs. Use for: the canonical map of building blocks and a first pass on any topic.

- [Book: _Designing Data-Intensive Applications_ — Martin Kleppmann (O'Reilly)](https://dataintensive.net/)
  The definitive deep text on how data systems work and fail — replication, partitioning, consistency, trade-offs. 2nd edition updated Feb 2026. Use for: going deep once a concept is introduced; the "why" behind the trade-offs. Dense — reach for it after a topic is first met in a lesson.

- [Distributed Systems for Fun and Profit — Mikito Takada](https://book.mixu.net/distsys/)
  Free short online book. Gentle conceptual intro to distributed-systems ideas (time, order, replication) with minimal math. Use for: building intuition before the heavier DDIA treatment.

- [ByteByteGo — Alex Xu](https://bytebytego.com/)
  Diagram-rich explanations and real-system deep dives (feeds, chat, video streaming). Alex Xu's _System Design Interview_ books are the companion. Use for: seeing how the anchor systems (Twitter, YouTube, WhatsApp) are actually architected. (Some content paid.)

- [Grokking System Design Fundamentals — Design Gurus](https://www.designgurus.io/course/grokking-system-design-fundamentals)
  Beginner-first course on core building blocks (client-server, databases, caching, load balancers) with simple analogies and minimal jargon. Use for: gentlest on-ramp to a new building block. (Paid.)

- [freeCodeCamp — System Design Concepts Course (Hayk Simonyan)](https://www.youtube.com/watch?v=F2FmTdLtb_4)
  Free full-length video building the foundational mental map. Use for: a video-format walkthrough of the fundamentals.

### Scaling & load balancing

- [Google SRE Book — "Load Balancing at the Frontend"](https://sre.google/sre-book/load-balancing-frontend/)
  Free online, written by the people operating this at planetary scale. Covers DNS-based balancing and its limits (resolver caching, TTLs), virtual IPs, consistent hashing for stable backend selection, and GRE encapsulation. Use for: what the tidy tutorial diagram is hiding. Harder than the primer — best skimmed after a concept is introduced, as a humbling.

- [NGINX — HTTP Load Balancing](https://nginx.org/en/docs/http/load_balancing.html)
  The implementer's own docs. Precise definitions of round-robin (the default), least-connected, and ip-hash, plus the explicit "no guarantee that the same client will be always directed to the same server." Use for: settling algorithm questions — see the Gaps note below on why this matters.

- [Google SRE Book — "Handling Overload"](https://sre.google/sre-book/handling-overload/) *(not yet used in a lesson)*
  Graceful degradation, cascading failure, and the counterintuitive point that an overloaded backend shouldn't simply stop accepting traffic. Also notes health checks can cost more than serving real requests. Use for: a future lesson on failure and overload.

### Video streaming (the streaming anchor)

- [RFC 8216 — HTTP Live Streaming (IETF)](https://www.rfc-editor.org/rfc/rfc8216)
  The normative HLS spec. Short, plain text, and surprisingly readable in sections. §6.2.1–6.2.2 (VOD vs Live playlist construction) and §6.3.3 (client reload rules) are the authority on how live and stored delivery differ. Use for: settling any "does it actually work that way?" question — blogs contradict each other constantly here; this doesn't.

- [How HLS Works — Jaz (Bluesky engineer)](https://jazco.dev/2024/07/05/hls/)
  Free, ~2,000 words, written right after the author built video for Bluesky knowing "next to nothing about the protocol." Makes segments and manifests concrete with real `.m3u8` files. Use for: the gentlest on-ramp to streaming. **Caveat:** explicitly covers VOD only — pair with RFC 8216 §6.2.2 for live.

- [Netflix Open Connect](https://openconnect.netflix.com/en/)
  Netflix's own documentation for its CDN and the appliances it puts inside ISPs. Confirms pre-filling caches by geography and nightly content fill. Use for: primary-source grounding on how stored video gets near viewers before they ask. (Some deeper partner docs are login-gated and 403 to fetch.)

- [Fastly — Request Collapsing](https://www.fastly.com/documentation/guides/concepts/edge-state/cache/request-collapsing/)
  Vendor docs, but the vendor that implements it. Crisp definition of collapsing simultaneous cache misses into one origin fetch. Use for: why a synchronised live audience is cheap rather than fatal to serve.

## Wisdom (Communities)

- [r/systemdesign](https://www.reddit.com/r/systemdesign/)
  Discussion + critique of designs. Use for: sanity-checking a design sketch, seeing how others reason about trade-offs.
- [r/ExperiencedDevs](https://www.reddit.com/r/ExperiencedDevs/)
  Practitioners discussing real architecture decisions. Use for: how these ideas play out in actual jobs (higher signal than beginner subs).

_Note: user hasn't been asked about joining communities yet — surface gently once he has a design sketch worth sharing._

## Gaps
- ~~No free, beginner-friendly source for the **video-streaming** anchor.~~ Partly closed 2026-07-15: Jaz's *How HLS Works* + RFC 8216 now cover segments/manifests and live-vs-VOD. **Still open:** nothing good yet on **adaptive bitrate** (how the player switches quality mid-stream) — find one before teaching ABR.
- Beware secondary sources on streaming: two search results directly contradicted each other on live vs VOD cache-hit ratios, and one widely-cited "2,000,000 requests → 1 origin fetch" figure did not appear in the article it was attributed to. Verify streaming claims against RFC 8216 or a vendor's own docs.
- **The same problem recurred on load balancing (2026-07-16).** A blog asserted least-connections is "the best default for most web applications"; NGINX's own docs say round-robin is the default and least-connected is better specifically *when request durations vary*. Different claim. **Rule now established for this course: prefer the implementer's or operator's own docs (NGINX, Fastly, Netflix, Google SRE, RFCs) over listicles and "system design" content farms.** The SEO layer around system-design topics is unusually low-quality — it optimises for interview keywords, not correctness.
