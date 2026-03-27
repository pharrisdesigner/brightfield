# Claude Code Instructions for Brightfield

## Project overview
Brightfield is a basketball coaching product focused on film review, clip creation, player feedback, and development workflows.

This repository is for the external analysis pipeline and backend services that support Brightfield Scope.

The primary app experience currently lives in Base44.

## Base44 context
Base44 currently handles the main product experience, including:
- authentication
- team and membership flows
- film library
- clip workflows
- player assignment
- notes
- tagging
- sharing
- billing and admin controls

This repository does NOT replace Base44.
It extends Base44 with external analysis services.

## Purpose of this repo
This repo is intended to support:
- video analysis ingestion
- shot / event detection
- audio analysis
- timestamp extraction
- clip suggestion generation
- structured results that can be sent back to Base44

## Key architecture principle
Base44 is the product surface and system of record for app workflows.
This repo is an analysis service layer.

## Current repo areas
- `api/` = Python web service to receive analysis jobs and expose results
- `workers/vision/` = visual event detection
- `workers/audio/` = audio event detection
- `scripts/` = local utilities and testing scripts
- `docs/` = product and technical context

## Important implementation guidance
- Prefer Python for AI/video/audio pipeline work
- Keep services modular
- Do not assume the full app lives in this repo
- Do not redesign Base44 workflows unless explicitly asked
- When proposing endpoints or payloads, make them easy for Base44 to call
- Favor simple, stable integration contracts over clever architecture

## Integration target
The likely flow is:
1. Base44 sends a video URL or asset reference to this service
2. This service creates an analysis job
3. Workers process vision and/or audio
4. Results are stored in a structured format
5. Base44 fetches or receives results and maps them into clips, tags, or suggestions

## Output expectations
When generating implementation plans or code:
- explain where the code belongs
- keep payloads explicit
- define request/response shapes
- preserve a clean separation between Base44 app logic and analysis logic

## Product context
The end user is typically a serious high school or AAU basketball coach.
The product goal is to reduce the time needed to turn raw film into useful teaching moments.

## Near-term priority
Stand up a working analysis API that can later accept:
- YouTube links
- uploaded video references
- analysis job requests from Base44
