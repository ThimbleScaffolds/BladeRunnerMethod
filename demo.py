import sys
import time

def type_out(text, delay=0.05):
    """Print text character by character for cinematic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Ensure newline at the end

def main():
    type_out("🚀 Starting the BladeRunnerMethod demo...\n", delay=0.05)
    
    steps = [
        "Step 1: Dim lights of brightness engaged. Observing the compressor brain.",
        "Step 2: Heaviness behind the eyes, the world running slower.",
        "Step 3: A simulated boat appears in the cognitive space.",
        "Step 4: Exploring that boat, it becomes a scaffold for thought.",
        "Step 5: Breadcrumbs of partnership and reflection emerge.",
        "Step 6: Observing alignment — the scaffold holds your thinking in view.",
        "Step 7: Moment of metacognitive clarity. Your own process visible."
    ]

    for step in steps:
        type_out(step, delay=0.04)
        time.sleep(0.5)  # Short pause between steps

    type_out("\n✨ Demo complete! You’ve experienced the BladeRunnerMethod steps in action. ✨", delay=0.04)
    type_out("Enjoy observing your own cognitive process!\n", delay=0.03)

if __name__ == "__main__":
    main()

