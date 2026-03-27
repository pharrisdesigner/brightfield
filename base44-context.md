# Base44 Context for Brightfield Scope

## What Base44 currently owns
Base44 is the primary application layer for Brightfield Scope.

It currently or conceptually owns:
- public landing pages
- auth and onboarding
- teams
- memberships and roles
- players
- videos
- clips
- notes
- tags
- sharing
- settings
- billing
- admin controls

## Important product model
Brightfield Scope is designed around:
- Team
- Video
- Clip
- Note
- Player
- Tag
- Share

The product goal is to help coaches review film, create clips quickly, add feedback, and share player-specific teaching moments.

## What this repo should add
This repo adds analysis capabilities that Base44 does not handle well internally, such as:
- visual event detection
- audio event detection
- shot detection
- timestamp extraction
- candidate clip generation
- metadata enrichment

## Integration principle
Base44 should remain the main app surface.
This analysis layer should be easy for Base44 to call through simple HTTP APIs.

## Likely data exchange
Base44 may send:
- video URL
- team ID
- video ID
- source type
- optional tags or analysis preferences

This service may return:
- analysis job ID
- processing status
- timestamps
- detected events
- suggested clip windows
- confidence scores
- optional metadata

## Important constraint
Do not assume this repo should duplicate the full product backend.
It should act as a specialized service layer.
