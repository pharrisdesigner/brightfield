# Brightfield Analysis Architecture

## Purpose
This repo supports external media analysis services for Brightfield Scope.

## High-level flow
1. Base44 app creates or references a video
2. Base44 sends a request to the analysis API
3. API creates an analysis job
4. Vision worker processes visual events
5. Audio worker processes sound events
6. Results are normalized
7. Base44 consumes results and turns them into coach-facing suggestions or clips

## Components

### API
Location: `api/`
Purpose:
- receive analysis requests
- expose health endpoints
- expose job status
- expose results

### Vision worker
Location: `workers/vision/`
Purpose:
- detect basketball-specific visual events
- identify candidate shot attempts
- identify timestamps and clip windows

### Audio worker
Location: `workers/audio/`
Purpose:
- detect sound events such as whistles, crowd spikes, rim/backboard contact, or other useful cues
- support optional transcript or speech-derived markers later

## Design principles
- modular services
- explicit payloads
- stable integration contracts
- Base44 remains the product surface
- this repo remains analysis-focused
