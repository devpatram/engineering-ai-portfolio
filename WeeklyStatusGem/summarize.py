import argparse, json, sys

TEMPLATE = """# Weekly Status

**Highlights**
- [Add top 3 outcomes]

**Projects**
{projects}

**Next Week**
- [Planned items]
- [Risks / blockers]

**Notes**
- [Shout-outs, decisions]
"""

def render(events):
    lines = []
    for e in events:
        s = e.get("summary","").strip()
        d = e.get("description","").strip()
        lines.append(f"- **{s}** — {d[:140]}")
    return TEMPLATE.format(projects="\n".join(lines))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", required=True)
    args = ap.parse_args()
    events = json.loads(open(args.events, "r", encoding="utf-8").read())
    sys.stdout.write(render(events))
