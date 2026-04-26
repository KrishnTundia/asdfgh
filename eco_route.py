"""Core calculation logic for Eco-Route AI.

This module exposes helpers to:
- estimate trip emissions via ``calculate_eco_impact``
- generate a professional AI prompt via ``build_environmental_scientist_prompt``

It can also be run directly as a CLI for quick demos.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ImpactResult:
    """Normalized response model for route impact calculations."""

    total_co2_grams: float
    trees_saved_equivalent: float
    quantum_insight: str


def build_environmental_scientist_prompt(
    *, distance_km: float, vehicle_type: str, traffic_level: str
) -> str:
    """Create a professional prompt for generating practical eco-driving advice."""

    return (
        "You are an environmental transport scientist. "
        "Given one trip profile, provide exactly one practical recommendation "
        "that can reduce trip emissions by about 5%. "
        f"Trip profile: vehicle={vehicle_type}, distance={distance_km} km, "
        f"traffic={traffic_level}. "
        "The tip must be actionable, realistic for daily commuters, and under 25 words."
    )


def calculate_eco_impact(
    distance_km: float,
    vehicle_type: str,
    traffic_level: str,
    *,
    ai_tip: str | None = None,
) -> ImpactResult:
    """Calculate CO2 impact using a lightweight "Quantum-Optimization" heuristic."""

    emission_factors = {
        "gas": 192,
        "hybrid": 105,
        "ev": 50,
    }
    traffic_multiplier = {
        "low": 1.0,
        "moderate": 1.2,
        "heavy": 1.5,
    }

    factor = emission_factors.get(vehicle_type, emission_factors["gas"])
    multiplier = traffic_multiplier.get(traffic_level, traffic_multiplier["low"])
    base_emissions = distance_km * factor * multiplier

    # Fallback AI output keeps backend deterministic in hackathon environments.
    insight = (
        ai_tip
        or "Maintain smooth acceleration and a steady cruising speed to cut avoidable energy loss in traffic."
    )

    return ImpactResult(
        total_co2_grams=round(base_emissions, 2),
        trees_saved_equivalent=round(base_emissions / 20000, 4),
        quantum_insight=insight,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Eco-Route AI carbon impact calculator")
    parser.add_argument("--distance-km", type=float, required=True, help="Trip distance in kilometers")
    parser.add_argument(
        "--vehicle-type",
        choices=["gas", "hybrid", "ev"],
        required=True,
        help="Vehicle powertrain type",
    )
    parser.add_argument(
        "--traffic-level",
        choices=["low", "moderate", "heavy"],
        required=True,
        help="Traffic intensity level",
    )
    parser.add_argument(
        "--ai-tip",
        default=None,
        help="Optional AI-generated eco tip override (for API integrations)",
    )
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    result = calculate_eco_impact(
        distance_km=args.distance_km,
        vehicle_type=args.vehicle_type,
        traffic_level=args.traffic_level,
        ai_tip=args.ai_tip,
    )
    prompt = build_environmental_scientist_prompt(
        distance_km=args.distance_km,
        vehicle_type=args.vehicle_type,
        traffic_level=args.traffic_level,
    )

    print("Impact:", asdict(result))
    print("Prompt:", prompt)


if __name__ == "__main__":
    main()
