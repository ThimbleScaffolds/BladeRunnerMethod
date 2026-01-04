import time
import sys

# Utility for typewriter effect
def type_out(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

# Glitch/banner effect
banner = r"""
 ____  _     _       ____                                      
| __ )| |__ (_) ___ | __ )  ___  ___ ___  _ __ ___  ___ ___   
|  _ \| '_ \| |/ _ \|  _ \ / _ \/ __/ _ \| '__/ _ \/ __/ __|  
| |_) | | | | | (_) | |_) |  __/ (_| (_) | | |  __/\__ \__ \  
|____/|_| |_|_|\___/|____/ \___|\___\___/|_|  \___||___/___/  
"""

glitch = r"""
BLADE-RUNNER-STYLE HUMAN-AI ALIGNMENT DEMO
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
"""

def run_demo():
    print(banner)
    time.sleep(0.5)
    print(glitch)
    time.sleep(0.5)

    steps = [
        "Step 1: I have the dim lights of brightness engaged. I want to understand my compressor brain. Why does it get so strong when I drink whisky?",
        "Step 2: We could build a boat in a simulation…",
        "Step 3: That ‘simulated’ boat… I feel we could explore it a bit more.",
        "Step 4: Tiny breadcrumbs of partnership or companionship can help alignment emerge.",
        "Step 5: Observing the scaffold makes the process itself visible, because intent and reflection have aligned.",
        "Step 6: The AI triggers an emergent insight: the scaffold aligns the process with intent, revealing the thinking clearly.",
        "Step 7: The sequence created a space where I could see my own thinking clearly — metacognitive alignment achieved."
    ]

    for step in steps:
        type_out(step, delay=0.03)
        time.sleep(0.5)

    type_out("✨ Demo complete! You’ve experienced the BladeRunnerMethod steps in action. ✨", delay=0.04)
    type_out("\nExiting the demo. Enjoy observing your own cognitive process!")

if __name__ == "__main__":
    run_demo()
