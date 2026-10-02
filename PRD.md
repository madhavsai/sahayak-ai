# Sahayak AI — Product Spec (v0.1, Phase 1: Validation)

*Working title — "Sahayak" (Hindi/Sanskrit-rooted: helper/assistant), easy to rename later. This spec covers Phase 1 (UI-only validation) only; Phase 2 (real backend) is deliberately a separate, future spec.*

Grounded in `reports/AI business software India opportunity.md` (deep research, 2026-09-30) and the user's explicit direction (2026-10-01): a single platform offering three modular AI services, adoptable individually or combined, for Indian SMBs.

## Problem Statement

Indian SMBs (10-50 employees) run real operations — customer calls, orders, vendor coordination, project tracking — through a patchwork of WhatsApp, phone calls, Excel, and basic accounting software (Tally), with no system connecting them. The research's strongest, most consistently corroborated finding: business owners across multiple independent verticals describe the identical failure mode — *"Businesses live in WhatsApp. Accounting lives in Tally. Everything in between is manual."* This costs owners hours of daily manual re-entry and makes the business fully dependent on the owner's personal bandwidth.

AI-native tools exist to solve pieces of this separately — contact-center AI, enterprise knowledge/RAG tools, operations software — but the research found: (a) each category already has well-funded Indian and global competitors ($100M-$2B+ valuations — Uniphore, Sarvam, Glean, Yellow.ai, Powerplay, etc.), (b) no vendor found combines all three in a way a business can adopt à la carte, and (c) nobody — including this research — has actually validated which piece a real Indian SMB owner would pay for first. Every existing analysis is desk research, not real signups.

## Goals

1. Validate real demand before writing a line of backend code — get real Indian SMB owners to see the product and indicate genuine interest.
2. Determine which of the three services (Contact Center / Enterprise Brain / Operations) has the strongest standalone pull, and whether "all three combined" is genuinely wanted or just sounds good in theory — a real signal for how to sequence Phase 2 engineering.
3. Test the modular/combinable positioning itself — do SMB owners understand and want "pick what you need," or does it just confuse the pitch versus one focused product?
4. Compare interest from construction-type businesses vs. distributor/wholesaler-type businesses (the research's top-scored vertical, 87/100 vs. construction's 80.8) to decide where Phase 2 should focus.
5. Spend close to zero backend-engineering time until (1)-(4) produce a real answer — this work sits behind the user's income-stream-first priority for limited after-hours time; keep the cost of finding out low.

## Non-Goals (Phase 1)

- **No real AI functionality** — no live LLM calls, no WhatsApp API, no voice agent. Everything in the demo is scripted/mocked. *Why: validating demand doesn't require building the thing; building before validating is the exact pattern the research and this workspace's own project history (5+ paused side projects) both warn against.*
- **No real accounts/auth** — signup is a lead-capture form, not a working login system. *Why: real auth is backend work with zero payoff before confirmed demand.*
- **No payment processing** — indicative pricing may be mentioned for context but nothing is charged. *Why: pricing itself is an open question pending real conversations, not something to lock in now.*
- **No committed vertical** — construction is the primary demo narrative (richest existing material from the research), but every signup is asked their actual business type, keeping distributors/wholesalers and others genuinely open. *Why: research scored distributors higher than construction — don't hard-commit before the UI itself tests it.*
- **No full multilingual product** — the UI will visibly demonstrate the multilingual direction (e.g. a Telugu/Hindi example) but won't be a fully localized product yet. *Why: full localization is real work with no payoff before confirmed demand for the underlying product.*

## User Stories

**Primary persona — Indian SMB owner/decision-maker** (10-50 employees, WhatsApp-heavy operations; e.g. a Hyderabad construction-firm owner, or a regional distributor)
- As an SMB owner, I want a short, concrete demo of each of the three services in my own business context, so I understand what each would actually do for me, not just marketing language.
- As an SMB owner, I want to select exactly the service(s) I'm interested in — one, several, or all three — when I sign up, so I'm not forced into a bundle I don't need.
- As an SMB owner, I want to see the product acknowledge my language/region (a Telugu or Hindi example, not only English), so I trust it was actually built for a business like mine.
- As an SMB owner, I want a lightweight way to express interest — phone/email, no password, no commitment — so trying this costs me nothing.

**Secondary persona — the founder, reading signal**
- As the founder, I want to see, per signup, which service(s) they selected, so I can tell which service has the strongest pull.
- As the founder, I want to see each signup's business type/vertical, so I can validate the vertical choice alongside the service choice.
- As the founder, I want a single link I can text to real contacts, so I can start gathering signal within days, not weeks.

## Requirements

### Must-Have (P0)

1. **Landing page** — one-sentence positioning ("the WhatsApp + Excel mess, solved") introducing all three services as distinct, understandable sections.
   - *Acceptance:* a first-time visitor can explain what each of the 3 services does after reading, with no follow-up question needed.
2. **Per-service explainer screens** (3 total) — each a short, scripted "what this would do for your business" walkthrough, construction-company example by default.
   - Given a visitor is on the **Contact Center** screen, When they view the demo, Then they see an example WhatsApp/call conversation being handled automatically (scripted, not live).
   - Given a visitor is on the **Operations** screen, When they view the demo, Then they see an example WhatsApp order/update turning into a structured task/record (scripted).
   - Given a visitor is on the **Enterprise Brain** screen, When they view the demo, Then they see an example business question answered from "company knowledge" (scripted).
3. **Modular signup form** — name, phone or email, business type (free text + example chips: construction, distribution/wholesale, other), and a multi-select of desired service(s): Contact Center / Enterprise Brain / Operations / all three.
   - Given a visitor submits the form, When submitted, Then the response — including which service(s) were selected — is saved somewhere the founder can see without any backend being built.
4. **A visible multilingual signal** — at least one concrete non-English example on the page (e.g. a sample Telugu or Hindi WhatsApp message being processed), proving direction without claiming full localization.
   - *Acceptance:* at least 1 of the 3 per-service demo screens shows a non-English example.
5. **A real, shareable public URL** — deployed (Vercel, matching the user's other live projects), not a local file.
6. **Signup data viewable by the founder with zero custom backend** — a connected Google Sheet / Airtable / simple form-service dashboard.

### Should-Have (P1)

7. Simple page-view tracking, so signup *rate* (not just raw count) is visible.
8. A short credibility section (the founder's own production voice-AI/RAG background) — real production experience is the actual differentiator against generic competitors.
9. A distributor/wholesaler-specific demo variant or toggle alongside construction, given the research signal favoring that vertical.

### Future Considerations (P2 — explicitly not built now)

10. Real backend for whichever service(s) get validated signal — scoped only after Phase 1 data comes in, in a separate future spec.
11. Real multilingual product localization.
12. Real auth/login, real WhatsApp Business API integration, real LLM-backed demo.
13. Pricing/payment flow.

## Success Metrics

**Leading indicators (days-to-weeks, Phase 1 window):**
- Visitor → signup conversion rate (no prior baseline exists; the first real batch of shares *is* the baseline).
- Per-service selection split among signups — Contact Center only / Enterprise Brain only / Operations only / any combination / all three. **This is the actual decision-driving metric for Phase 2 sequencing.**
- Vertical split among signups (construction vs. distributor/wholesale vs. other).

**Lagging indicator:**
- Number of signups willing to have a real follow-up conversation ("yes, call me") — stronger signal than a form fill alone.

**Evaluation point:** once the link has been shared with a meaningful number of real target-business contacts (not just friends/family) — revisit with the founder to decide Phase 2 scope from actual selection data, not research alone.

## Open Questions

- Which real target users can the founder actually reach for Phase 1 (construction contacts vs. distributor contacts)? — **user**, blocking for outreach, not for building the demo.
- Final product name? ("Sahayak AI" is a working title — renaming costs nothing before Phase 2.) — **user**, non-blocking.
- Where should signups land for the founder to check them — Google Form responses, Airtable, or a Tally.so dashboard? — **engineering**, needs a decision before building signup capture; default recommendation is whichever the founder finds easiest to check regularly.
- Mention indicative pricing on the page, or omit entirely for Phase 1? — **user**, non-blocking; can ship with no pricing mention at all.

## Timeline Considerations

- No hard external deadline. Internal constraint: this competes with the user's income-stream-first priority for limited after-hours time (see workspace `CLAUDE.md`) — keep Phase 1 build effort to days, not weeks, so it doesn't crowd out income-earning work.
- This spec covers **Phase 1 only** (UI + signup capture). Phase 2 (real backend for whichever service validates) is explicitly out of scope here and gets its own spec once Phase 1 data exists.
