import joblib
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "model.joblib"

def ask_float(prompt, lo, hi):
    while True:
        try:
            v = float(input(prompt).strip())
            if v < lo or v > hi:
                print(f"Enter between {lo} and {hi}.")
                continue
            return v
        except ValueError:
            print("Enter a number.")

def ask_int(prompt, lo, hi):
    while True:
        try:
            v = int(input(prompt).strip())
            if v < lo or v > hi:
                print(f"Enter between {lo} and {hi}.")
                continue
            return v
        except ValueError:
            print("Enter a whole number.")

def main():
    model = joblib.load(MODEL_PATH)

    print("\nEnter today's values (demo):")
    x = [
        ask_float("Sleep hours (0-14): ", 0, 14),
        ask_int("Study minutes (0-1200): ", 0, 1200),
        ask_int("Break minutes (0-600): ", 0, 600),
        ask_int("Subjects studied (0-10): ", 0, 10),
        ask_int("Energy after studying (1-5): ", 1, 5),
        ask_int("Stress end of day (1-5): ", 1, 5),
    ]

    pred = float(model.predict([x])[0])
    pred_clipped = int(np.clip(round(pred), 1, 5))

    print("\nPredicted next-morning fatigue (1-5):", round(pred, 2))
    print("Rounded fatigue level:", pred_clipped)
    print("\nReminder: this is a non-medical indicator and depends on data quality.")

if __name__ == "__main__":
    main()
