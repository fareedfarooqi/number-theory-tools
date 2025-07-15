# Number Theory Tools

A small collection of Python utilities and fuzzing harnesses for number-theory functions (prime factorisation, totient, GCD, modular exponentiation), with both black-box and grey-box testing support.

## Features

- **Totient & factorisation**  
  - `totient_calculator.py`  
    - `unique_prime_factorisation(n)` → `{p: k}`  
    - `calculate_totient(n)` → φ(n)  
- **Modular arithmetic**  
  - `interactive_modular_exponentiation.py`  
  - `interactive_totient.py`  
  - `eulers_theorem(base, exp, mod)`  
  - `flt(base, exp, mod)` (Fermat’s Little Theorem)  
- **GCD**  
  - `get_gcd(a, b)` via the Euclidean algorithm  
- **Fuzzing harness**  
  - `fuzz_totient_afl.py` for AFL++ grey-box fuzzing  
- **Black-box fuzzing scripts**  
  - `scripts/fuzz_totient.sh`  
  - `scripts/fuzz_modular_exponentiation.sh`  
- **Dockerfile** for reproducible AFL++ environment

---

## Requirements

- Python 3.11+  
- `sympy` (for `isprime`)  
- `python-afl` (for grey-box harness)  
- (Optional) `pytest` for unit tests  

```text
sympy>=1.0
python-afl>=0.7
pytest>=8.0
```

---

## Installation

1. Clone this repo and enter its directory:
   ```bash
   git clone https://github.com/fareedfarooqi/number-theory-tools.git
   cd number-theory-tools
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install Python dependencies:
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

---

## Usage

### Interactive Calculators

#### Totient
```bash
python3 interactive_totient.py

Enter a positive integer to compute its Euler totient.
```

---

### Modular Exponentiation
```bash
python3 interactive_modular_exponentiation.py

Provide base, exponent, and modulus to see results via Fermat’s or Euler’s methods.
```

```bash
cd scripts
./fuzz_totient.sh
./fuzz_modular_exponentiation.sh
```

Each will print PASS/FAIL for a series of random test cases.

---

## Grey-Box Fuzzing (AFL++)

### Native (macOS/Linux)

Ensure AFL++ and `python-afl` are installed, then run:

```bash
py-afl-fuzz \
  -i seeds/initial_seeds \
  -o afl-out \
  -- python3 fuzz_totient_afl.py
```

- **NOTE**: If you are running on MacOS, then most likely by default the command above will not work due to OS restrictions. You can run it in a docker container instead.

### In Docker

Build the image:

```bash
docker build -t number-theory-fuzzer .
```

Fuzz the default totient harness:

```bash
docker run --rm -it -v "$PWD":/src number-theory-fuzzer
```

To fuzz another harness (e.g. modular exponentiation) --> coming SOON:

```bash
docker run --rm -it -v "$PWD":/src number-theory-fuzzer \
  py-afl-fuzz -i modexp_seeds/ -o afl-out-modexp -- python3 fuzz_modexp_afl.py
```

---

## Running Tests

With the virtualenv active:

```bash
pytest -q
```