# Skill Pack Design

A skill pack is a named bundle of Hermes skills installed together for a client or workflow.

## Boundary

Skills should contain repeatable procedures.

They should not contain:

- client secrets
- private API keys
- one client's raw source documents
- claims that only apply to one business

Client-specific context belongs in the client's LLM wiki.

## Recommended layers

1. Generic skill: reusable procedure
2. Client wiki: facts, sources, examples, brand voice, decisions
3. Client prompt: tells Hermes which skills and wiki to use
