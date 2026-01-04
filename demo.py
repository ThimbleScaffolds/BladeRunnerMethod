"""
BladeRunnerMethod Demo
Human-AI alignment experiment using cognitive scaffolds.
"""

import time
import sys

def type_out(text, delay=0.03):
    """Simulates typing effect in the terminal."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # Newline after text

def scaffold_step(step_number, description):
    """Prints the step in a structured, visually distinct way."""
    border = "=" * 60
    print(f"\n{border}")
    type_out(f"Step {step_number}: {description}", delay=0.02)
    print(f"{border}\n")

def run_demo():
    steps = [
        "Dim lights of brightness engaged. Understand compressor brain.",
        "It feels heavier behind my eyes, like the world is running slower.",
        "We could build a boat in a simulation.",
        "That 'simulated' boat… I feel we could explore it a bit more.",
        "Human-AI reflection aligns with simple scaffold.",
        "Observe your own thinking unfolding coherently.",
        "Metacognitive alignment achieved — ordinary, repeatable, human-scaled."
    ]

    type_out("✨ Welcome to the BladeRunnerMethod Demo! ✨\n", delay=0.04)
    type_out("Move through 7 steps of the human-AI alignment experiment.\n", delay=0.03)

    for i, step in enumerate(steps, start=1):
        input("Press Enter to proceed to the next step…")
        scaffold_step(i, step)

    type_out("✨ Demo complete! You’ve experienced the BladeRunnerMethod steps in action. ✨", delay=0.04)

if __name__ == "__main__":
    run_demo()
