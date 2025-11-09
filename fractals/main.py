import pygame
from fractals.sapfinski import run_sierpinski
from fractals.tree_pifagor import run_pythagoras
from fractals.l_systems import run_lsystem
from fractals.rules.lsystem_rules import L_SYSTEM_RULES
from fractals.rules.custom_rules import CUSTOM_RULES

def main():
    print("fractal project started")
    print("default: sierpinski triangle")
    print("press:")
    print("  1 - sierpinski triangle")
    print("  2 - pythagoras tree")
    print("  3 - l-system preset")
    print("  4 - custom l-system")
    print("  esc - exit\n")


    while True:
        choice = input("choose fractal (1-4): ").strip()

        if choice == "1":
            run_sierpinski()
        elif choice == "2":
            run_pythagoras()
        elif choice == "3":
            print("\navailable l-systems:")
            for name in L_SYSTEM_RULES:
                print("-", name)
            key = input("choose preset: ").strip()
            r = L_SYSTEM_RULES.get(key, L_SYSTEM_RULES["plant"])
            run_lsystem(r["axiom"], r["rules"], r["angle"], 8, 4, key)
        elif choice == "4":
            print("\navailable custom systems:")
            for name in CUSTOM_RULES:
                print("-", name)
            key = input("choose custom: ").strip()
            r = CUSTOM_RULES.get(key, list(CUSTOM_RULES.values())[0])
            run_lsystem(r["axiom"], r["rules"], r["angle"], 8, 4, key)
        elif choice.lower() in ("esc", "exit", "q"):
            print("exit program...")
            break
        else:
            print("unknown command")

if __name__ == "__main__":
    main()
