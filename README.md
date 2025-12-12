# 🧠 Study Fatigue & Burnout Risk Analyzer

## Why I built this

I built this project out of pure curiosity.

I wanted to see what a project like this would actually turn into if I tried to model something from my own life instead of abstract data or benchmarks. School gets intense, routines aren’t always consistent, and I was curious whether patterns in things like sleep, study time, stress, and energy could be learned in a meaningful way.

This wasn’t about “fixing” anything or making big claims — I just wanted to explore how AI could be used as a tool to reflect on habits rather than judge them.

---

## What this project does

This project is a **human-centered AI system** that learns patterns between daily study habits and how fatigued I feel the following morning.

Each day is represented by:
- sleep duration
- study time
- break time
- number of subjects studied
- self-reported energy level
- self-reported stress level

Using this data, the model outputs a **fatigue risk indicator** (1–5) for the next morning.

This is **not** a medical tool, diagnosis, or mental health predictor.  
It’s a small decision-support system designed to help reflect on routines.

---

## How it works (high level)

1. Collect daily study and lifestyle data
2. Train a simple baseline ML model (Ridge regression)
3. Evaluate performance using held-out data
4. Use the trained model to estimate next-day fatigue from new inputs

The goal is not maximum accuracy — it’s understanding patterns and uncertainty.

---

## Data note (important)

The dataset included in this repository is **synthetic**.

I generated realistic sample data to:
- demonstrate the full ML pipeline
- keep personal data private
- make the project reproducible for anyone viewing it

The system is designed so real personal data can be logged locally without ever being uploaded.

---

## What I learned from building this

This project taught me a few important things about AI:

- AI should **support human judgment**, not replace it  
- Data quality matters more than model complexity  
- Simple models can still be useful when applied thoughtfully  
- Even small projects benefit from being honest about limitations  

Interestingly, just thinking through the features and outputs helped me reflect on my own routine and make small improvements — which wasn’t something I expected going in.

---

## AI usage disclosure

I did use AI tools during this project, but strictly as a **learning and guidance resource**.

I didn’t copy-paste solutions. Instead, AI helped me:
- understand concepts
- debug issues
- think through design choices

The implementation, structure, and decisions were my own.

---

## Limitations

- Uses synthetic data instead of real personal logs
- Small dataset by design
- Fatigue is self-reported and subjective
- Assumes independence between days
- No long-term temporal modeling yet

These limitations are intentional and acknowledged — this project is exploratory, not final.

---

## What’s next

- Replace synthetic data with private real-world logging
- Add uncertainty estimates to predictions
- Explore temporal models (fatigue accumulation over time)
- Continue building human-centered AI projects

---

## Final takeaway

This project isn’t about predicting burnout or optimizing productivity.

It’s about using AI responsibly — as a way to explore patterns, reflect on habits, and support better decision-making without removing human judgment.
