from csv import DictReader
from pathlib import Path

def build_checklist(control_map_path: str):
    rows = list(DictReader(open(control_map_path, newline='', encoding='utf-8')))
    lines = ["# Review Checklist", ""]
    for r in rows:
        lines.append(f"- [{'{'} {'}'}] {r['Control Id']} — {r['Description']} (src: {r['Policy']})")
    return "\n".join(lines)

if __name__ == "__main__":
    print(build_checklist("templates/control-map.csv"))
