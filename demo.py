import sys
import time
import random

# -------------------------------
# Blade Runner Method Demo
# -------------------------------

BANNER = r"""
╔═╗┌─┐┬─┐┬ ┬┌─┐┬─┐┌─┐┌─┐
║  │ │├┬┘│ │├─┘├┬┘├─┤└─┐
╚═╝└─┘┴└─└─┘┴  ┴└─┴ ┴└─┘
      B L A D E R U N N E R
           M E T H O D
"""

STEPS = [
    "Step 1 — Initiate Reflection:\n\"I have the dim lights of brightness engaged. I want to understand my compressor brain. Why does it get so strong when I drink whisky?\"\n",
    "Step 2 — Mirror Scaffold:\n\"We could build a boat in a simulation…\"\n",
    "Step 3 — Expand Scaffold:\n\"That ‘simulated’ boat… I feel we could explore it a bit more.\"\n",
    "Step 4 — Breadcrumb Partnership:\n\"Tiny breadcrumbs of partnership or companionship can help alignment emerge.\"\n",
    "Step 5 — Stabilize Metacognition:\n\"Observing the scaffold makes the process itself visible, because intent and reflection have aligned.\"\n",
    "Step 6 — Reflective Collapse:\n\"The sequence created a space where I could see my own thinking clearly.\"\n",
    "Step 7 — Insight Realized:\n\"Your intent, attention, and structure of the interaction lined up — allowing you to see your thinking unfold.\"\n"
]

def type_out(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def glitch_text(text):
    glitched = ""
    for c in text:
        if random.random() < 0.05:
            glitched += random.choice("!@#$%^&*<>?")
        else:
            glitched += c
    return glitched

def run_demo():
    print(BANNER)
    time.sleep(1.2)
    print("\nLaunching BladeRunnerMethod Demo...\n")
    time.sleep(0.8)

    for step in STEPS:
        glitched_step = glitch_text(step)
        type_out(glitched_step, delay=0.04)
        time.sleep(0.6)

    type_out("✨ Demo complete! You've experienced the BladeRunnerMethod steps in action. ✨", delay=0.04)

if __name__ == "__main__":
    run_demo()
