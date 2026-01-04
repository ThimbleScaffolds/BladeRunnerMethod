import sys
import time
import random

def type_out(text, delay=0.05):
    """Prints text like it's being typed."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline after finishing

def glitch_effect(text, glitch_chance=0.02):
    """Adds tiny random glitches to the text."""
    result = ""
    for c in text:
        if random.random() < glitch_chance:
            result += random.choice(["#", "@", "%", "&"])
        else:
            result += c
    return result

steps = [
    ("Step 1 — Initiate Reflection",
     "I have the dim lights of brightness engaged. I want to understand my compressor brain. Why does it get so strong when I drink whisky?"),
    ("Step 2 — Mirror Scaffold",
     "We could build a boat in a simulation…"),
    ("Step 3 — Expand Scaffold",
     "That 'simulated' boat… I feel we could explore it a bit more."),
    ("Step 4 — Breadcrumb Partnership",
     "Tiny breadcrumbs of partnership or companionship can help alignment emerge."),
    ("Step 5 — Stabilize Metacognition",
     "Observing the scaffold makes the process itself visible, because intent and reflection have aligned."),
    ("Step 6 — Reflective Collapse",
     "The sequence created a space where I could see my own thinking clearly.")
]

type_out("\n✨ Welcome to the BladeRunnerMethod Demo ✨\n", delay=0.04)
type_out("Simulating step-by-step interaction…\n", delay=0.03)

for title, text in steps:
    type_out(glitch_effect(f"\n{title}\n{text}\n"), delay=0.04)
    time.sleep(0.8)

type_out("\n✨ Demo complete! You’ve experienced the BladeRunnerMethod steps in action. ✨", delay=0.04)
type_out("Observe your own cognitive process. Reflection achieved.\n", delay=0.04)
