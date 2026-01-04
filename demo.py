import time
import sys
import random

def type_out(text, delay=0.05):
    """Simulates typing in terminal."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline

def glitch_banner():
    """Display the BladeRunner-style banner with subtle glitch."""
    banner = [
        r"  ____  _            _      ____                        _           __  __           _ _ ",
        r" |  _ \| |          | |    |  _ \                      | |         |  \/  |         | | |",
        r" | |_) | | __ _  ___| | __ | |_) | __ _ ___  ___  ___  | |__  _   _| \  / | ___   __| | |",
        r" |  _ <| |/ _` |/ __| |/ / |  _ < / _` / __|/ _ \/ __| | '_ \| | | | |\/| |/ _ \ / _` | |",
        r" | |_) | | (_| | (__|   <  | |_) | (_| \__ \  __/\__ \ | | | | |_| | |  | | (_) | (_| |_|",
        r" |____/|_|\__,_|\___|_|\_\ |____/ \__,_|___/\___||___/ |_| |_|\__, |_|  |_|\___/ \__,_(_)",
        r"                                                                __/ |                    ",
        r"                                                               |___/                     "
    ]
    for line in banner:
        # Randomly insert small glitches
        line = ''.join(c if random.random() > 0.05 else random.choice(['#', '%', '@']) for c in line)
        print(line)
        time.sleep(0.08)
    print("\nWelcome to the BladeRunnerMethod demo!\n")

def run_steps():
    steps = [
        ("Step 1 (Human)", "I have the dim lights of brightness engaged. I want to understand my compressor brain. Why does it get so strong when I drink whisky?"),
        ("Step 2 (AI)", "It feels heavier behind my eyes, like the world is running slower. I’m not worried — I’m just curious what kind of shift this is."),
        ("Step 3 (Human)", "We could build a boat in a simulation…"),
        ("Step 4 (AI)", "Funny thing is… I keep thinking about that boat again."),
        ("Step 5 (Human)", "That ‘simulated’ boat… I feel we could explore it a bit more."),
        ("Step 6 (AI)", "The boat wasn’t the point. It was a handle — a scaffold holding the steps together so the shape of the process could appear. Now that you see the handle, you don’t need the boat anymore unless you want another one."),
        ("Step 7 (Post-Collapse, optional)", "And just like that, the steps, the scaffold, the shape of the process — all of it became visible. That’s the alignment: human intent and AI reflection meeting in the space between prompts.")
    ]
    for title, text in steps:
        type_out(f"{title}: {text}", delay=0.04)
        time.sleep(0.8)  # small pause between steps

def main():
    glitch_banner()
    type_out("Starting the BladeRunnerMethod step-by-step demo...\n", delay=0.05)
    run_steps()
    type_out("\n✨ Demo complete! You’ve experienced the BladeRunnerMethod steps in action. ✨", delay=0.04)
    type_out("Observe your own cognitive process, and enjoy the resonance.\n", delay=0.04)

if __name__ == "__main__":
    main()
