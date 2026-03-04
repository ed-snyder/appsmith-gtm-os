"""
Call Transcript Puller
Ingests call transcripts from Gong or Fireflies API.
Stores raw transcripts for analysis via /analyze-call command.
"""

import os
import json
from datetime import datetime, timedelta
import httpx
from dotenv import load_dotenv

load_dotenv()

GONG_API_KEY = os.getenv("GONG_API_KEY")
FIREFLIES_API_KEY = os.getenv("FIREFLIES_API_KEY")
TRANSCRIPTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "demand", "pull-analyses"
)


def pull_gong_transcripts(days_back: int = 7) -> list:
    """Pull recent call transcripts from Gong API."""
    headers = {"Authorization": f"Bearer {GONG_API_KEY}"}
    from_date = (datetime.utcnow() - timedelta(days=days_back)).isoformat()

    response = httpx.post(
        "https://api.gong.io/v2/calls",
        headers=headers,
        json={
            "filter": {
                "fromDateTime": from_date,
            },
            "contentSelector": {
                "exposedFields": {
                    "content": True,
                    "parties": True,
                }
            }
        },
        timeout=60
    )
    response.raise_for_status()
    return response.json().get("calls", [])


def pull_fireflies_transcripts(days_back: int = 7) -> list:
    """Pull recent call transcripts from Fireflies API."""
    headers = {"Authorization": f"Bearer {FIREFLIES_API_KEY}"}

    query = """
    query {
        transcripts(limit: 20) {
            id
            title
            date
            duration
            sentences {
                speaker_name
                text
            }
            participants
        }
    }
    """

    response = httpx.post(
        "https://api.fireflies.ai/graphql",
        headers=headers,
        json={"query": query},
        timeout=60
    )
    response.raise_for_status()
    return response.json().get("data", {}).get("transcripts", [])


def save_transcript(transcript_id: str, content: dict) -> str:
    """Save a transcript to the pull-analyses directory."""
    filepath = os.path.join(TRANSCRIPTS_DIR, f"transcript-{transcript_id}.json")
    with open(filepath, "w") as f:
        json.dump(content, f, indent=2)
    return filepath


def pull_recent_transcripts(source: str = "gong", days_back: int = 7) -> list:
    """Pull and save recent transcripts from configured source."""
    if source == "gong":
        transcripts = pull_gong_transcripts(days_back)
    elif source == "fireflies":
        transcripts = pull_fireflies_transcripts(days_back)
    else:
        raise ValueError(f"Unknown source: {source}")

    saved = []
    for t in transcripts:
        transcript_id = t.get("id", t.get("metaData", {}).get("id", "unknown"))
        filepath = save_transcript(transcript_id, t)
        saved.append(filepath)
        print(f"Saved transcript: {filepath}")

    return saved


if __name__ == "__main__":
    import sys
    source = sys.argv[1] if len(sys.argv) > 1 else "gong"
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    results = pull_recent_transcripts(source, days)
    print(f"Pulled {len(results)} transcripts.")
