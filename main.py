from analyzers.core_analyzer import analyze_core
from analyzers.memory_pattern import classify_pattern
from analyzers.exploitability_score import calculate_score
from binary.elf_hardening import analyze_binary
from utils.logger import log
import os

def header():
    print("=" * 60)
    print("CRASHVECTOR :: Real Crash & Exploitability Analyzer")
    print("=" * 60)

def run():
    header()

    binary = "./crash_test"
    core = "core"

    if not os.path.exists(binary) or not os.path.exists(core):
        print("[!] No real crash data found.")
        print("    Run a crashing program first.")
        return

    signal, explanation = analyze_core(binary, core)

    print("[*] Crash Signal:", signal)
    print("[*] Crash Explanation:", explanation)

    pattern = classify_pattern(explanation)
    print("[*] Memory Corruption Pattern:", pattern)

    protections = analyze_binary(binary)

    print("\n[*] Binary Hardening")
    for k, v in protections.items():
        print(f"    {k.upper():10}: {'ENABLED' if v else 'MISSING'}")

    risk = calculate_score([pattern], protections)

    print("\n[*] Exploitability Risk:", risk)

    log(f"Signal={signal}, Pattern={pattern}, Risk={risk}")

    print("\n[+] Real analysis complete.")

if __name__ == "__main__":
    run()
