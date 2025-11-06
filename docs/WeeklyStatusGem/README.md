# WeeklyStatusGem — Calendar ➜ Status Report

**Status:** Scaffold • Paste sample .ics snippets to test  
Generates weekly status summaries from exported calendar events.

## Usage
1. Export your calendar for the week (.ics).
2. Run the parser to extract SUMMARY/DESCRIPTION.
3. Feed into your LLM (or use a template) to produce a clean status.

```bash
cd WeeklyStatusGem
python parse_calendar.py --ics sample/week.ics > out/events.json
python summarize.py --events out/events.json > out/status.md
```

> This repo keeps **no sensitive events**; use redacted or dummy data.
