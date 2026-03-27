# Brightfield Integration Contract Draft

## Example: create analysis job

### Request

POST /analyze

```json
{
  "video_id": "vid_123",
  "team_id": "team_456",
  "source_url": "https://example.com/video.mp4",
  "source_type": "youtube",
  "analysis_modes": ["vision", "audio"]
}
### Response

```json
{
  "job_id": "job_789",
  "status": "queued"
}

##  Example: get job status
Request

GET /jobs/job_789

### Response

```json
{
  "job_id": "job_789",
  "status": "processing",
  "progress": 55
}
### Example: get analysis results
Request

GET /jobs/job_789/results

### Response

```json
{
  "job_id": "job_789",
  "status": "complete",
  "events": [
    {
      "type": "shot_attempt",
      "start_seconds": 123.4,
      "end_seconds": 128.9,
      "confidence": 0.84
    }
  ],
  "suggested_clips": [
    {
      "title": "Shot attempt",
      "start_seconds": 121.0,
      "end_seconds": 130.0,
      "confidence": 0.84
    }
  ]
}

### Notes
### Payloads should stay simple
### Base44 should be able to call these endpoints easily
### Avoid over-coupling service internals to the app
