import sys
from totient_calculator import calculate_totient

def main():
    data = sys.stdin.buffer.read().decode("ascii", errors="ignore").strip()

    try:
        # We don't care about the output in this blackbox fuzz testing.
        _ = calculate_totient(int(data))
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()