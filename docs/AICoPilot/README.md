# AICoPilot — AI Compliance & Proposal Co‑Pilot

**Status:** Scaffold • Add specifics and redacted artifacts  
**Pitch:** Internal AI assistant that helps teams draft compliance-safe responses and proposals faster by grounding outputs in approved policies and prior exemplars.

## Problem
Manual policy lookup and proposal drafting is slow and error-prone.

## Solution
- A retrieval-augmented assistant that:
  - Maps prompts to approved policy blocks (knowledge base)
  - Suggests proposal sections and compliance language
  - Highlights gaps and requests missing inputs

## Artifacts
- `docs/brief.md` — exec brief
- `prompts/system.md` — system instructions (safe prompting)
- `src/` — Python scaffolding for local experimentation

## Results (example placeholders)
- 25–40% faster first-draft creation
- Fewer rework cycles per proposal (qualitative)
- Centralized policy blocks reduce inconsistency

## How to Run
```bash
cd AICoPilot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/app.py --demo
```

## Next
- Add policy snippets (redacted) under `knowledge/`
- Capture before/after examples
- Add unit tests for prompt guards
