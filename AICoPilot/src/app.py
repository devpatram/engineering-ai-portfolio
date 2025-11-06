import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Run a dry demo.")
    args = parser.parse_args()
    print("AICoPilot demo — replace with your LLM integration and retrieval code.")
    print("Tip: Add policy blocks under ./knowledge and index them.")

if __name__ == "__main__":
    main()
