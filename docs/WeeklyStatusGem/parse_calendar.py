import argparse, json, re
from pathlib import Path

def parse_ics(text: str):
    items = []
    current = {}
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("BEGIN:VEVENT"):
            current = {}
        elif line.startswith("END:VEVENT"):
            if current:
                items.append(current)
        elif line.startswith("SUMMARY:"):
            current["summary"] = line[len("SUMMARY:"):]
        elif line.startswith("DESCRIPTION:"):
            current["description"] = line[len("DESCRIPTION:"):]
        elif line.startswith("DTSTART:"):
            current["start"] = line[len("DTSTART:"):]
        elif line.startswith("DTEND:"):
            current["end"] = line[len("DTEND:"):]
    return items

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ics", required=True, type=str)
    args = ap.parse_args()
    text = Path(args.ics).read_text(encoding="utf-8", errors="ignore")
    events = parse_ics(text)
    print(json.dumps(events, indent=2))
