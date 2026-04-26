# Eco-Route AI: The Carbon-Conscious Commuter 🌍

### 🚀 Quantum Sprint Submission — For Social Good

## What this project is used for
Eco-Route AI helps you estimate the carbon impact of a trip and generate one practical tip to reduce emissions. It is useful for:
- hackathon demos,
- backend APIs (Flask/FastAPI),
- route comparison dashboards,
- behavior-change nudges for commuters.

## Why run it
Run this project if you want to:
- quantify trip CO2 in seconds,
- show climate impact in a user-friendly way (`trees_saved_equivalent`),
- plug in an LLM tip without blocking your core calculations,
- demonstrate an AI + sustainability concept quickly.

## How to run
### 1) Prerequisite
- Python 3.10+

### 2) Run from terminal
```bash
python eco_route.py --distance-km 12.5 --vehicle-type gas --traffic-level heavy
```

Example output (shape):
```text
Impact: {'total_co2_grams': ..., 'trees_saved_equivalent': ..., 'quantum_insight': '...'}
Prompt: You are an environmental transport scientist...
```

### 3) Use in Python code
```python
from eco_route import calculate_eco_impact, build_environmental_scientist_prompt

result = calculate_eco_impact(12.5, "gas", "heavy")
prompt = build_environmental_scientist_prompt(
    distance_km=12.5,
    vehicle_type="gas",
    traffic_level="heavy",
)
print(result)
print(prompt)
```

## 💡 The Problem
Most navigation tools optimize for time, not emissions. That can push commuters through congested routes that increase idling, fuel burn, and avoidable CO2 output.

## 🌟 The Solution
**Eco-Route AI** is a *Quantum-Efficient* route impact assistant. Instead of only answering “what’s fastest?”, it also answers “what’s cleanest?” by estimating route-level carbon impact and giving one practical behavior tip.

## 🛠️ How It Works
- **Quantum-Optimization Engine:** Combines distance, vehicle profile, and traffic intensity to estimate emissions quickly.
- **AI Insights Layer:** Uses an environmental-scientist prompt pattern to produce one actionable, low-friction tip.
- **Impact Translation:** Converts CO2 grams into an annualized “trees saved equivalent” value for user-friendly impact framing.

## 🏆 Why It Wins
- **Social Good:** Helps reduce transport-sector emissions through daily behavior shifts.
- **Applied AI:** Couples deterministic carbon math with practical LLM-generated recommendations.
- **Hackathon-Ready:** Lightweight Python logic drops into Flask/FastAPI quickly.

## 📈 Future Roadmap
- Add route alternatives from map APIs and compute per-route impact deltas.
- Integrate real-time EV grid intensity for location-aware EV estimates.
- Add user trip history and progress tracking with privacy-preserving analytics.
