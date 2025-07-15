# fuzz_totient_afl.py

import sys
import afl
from totient_calculator import calculate_totient

def fuzz_one(data: bytes):
    """
    Called by AFL for each mutated input.
    Decodes data to an integer (supports hex like “0x…” too),
    runs calculate_totient(), and lets any exception bubble up
    as a crash.
    """
    n = int(data.decode("ascii", errors="ignore").strip() or "0", 0)
    _ = calculate_totient(n)

def main():
    afl.init()
    for raw in sys.stdin.buffer:
        fuzz_one(raw)

if __name__ == "__main__":
    main()
