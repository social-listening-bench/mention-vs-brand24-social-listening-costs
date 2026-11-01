#!/usr/bin/env python3
"""
Mention vs Brand24 Social Listening Cost & Sentiment Calculator 2026.
"""
import argparse

def calculate(keywords, mentions, annual):
    # Mention Pro: $83/mo annual or $99/mo monthly (10k mentions, 10 alerts)
    men_cost = 83.0 if annual else 99.0

    # Brand24 Team: $149/mo annual or $179/mo monthly (5k mentions, 7 keywords, AI sentiment & reach)
    b24_cost = 149.0 if annual else 179.0

    diff = b24_cost - men_cost

    print("=" * 60)
    print("Social Listening Comparison: Mention vs Brand24")
    print("=" * 60)
    print(f"Keywords Needed:         {keywords}")
    print(f"Expected Mentions:       {mentions:,}/mo")
    print(f"Mention Pro Plan:        ${men_cost:.2f}/mo (${men_cost*12:.2f}/yr)")
    print(f"Brand24 Team Plan:       ${b24_cost:.2f}/mo (${b24_cost*12:.2f}/yr)")
    print(f"Cost Difference:         ${abs(diff):.2f}/mo ({'Mention Cheaper' if diff > 0 else 'Brand24 Cheaper'})")
    print("=" * 60)
    return men_cost, b24_cost

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mention vs Brand24 Calculator")
    parser.add_argument("--keywords", type=int, default=5)
    parser.add_argument("--mentions", type=int, default=4000)
    parser.add_argument("--annual", action="store_true", default=True)
    args = parser.parse_args()
    calculate(args.keywords, args.mentions, args.annual)
