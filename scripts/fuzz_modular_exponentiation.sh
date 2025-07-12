#!/usr/bin/env bash

# Please note I only test ASCII characters in this script.

# All our seed files.
seeds=(../seeds/seed-6.txt ../seeds/seed-7.txt ../seeds/seed-8.txt)

loop_count=1

clean_token() {
  grep -oE '[A-Za-z]+' <<<"$1" \
    || grep -oE '^-?[0-9]+' <<<"$1" \
    || echo ""
}

while true; do
    idx=$(( RANDOM % ${#seeds[@]}))
    seed="${seeds[$idx]}"

    radamsa -n 1 "$seed" > "fuzz_file.txt"
    num_items=$(cat "fuzz_file.txt" | wc -l)

    # So radamsa may sometimes output 1, 2, 3, 4 etc outputs. We only need 3
    # outputs for our function. If we don't get 3 outputs from radamsa we skip.
    if [ "$num_items" -ne 3 ]; then
        continue
    fi

    lines=()
    while IFS= read -r line; do
        lines+=("$line")
    done < "fuzz_file.txt"
    
    base_raw="${lines[0]}"
    exp_raw="${lines[1]}"
    mod_raw="${lines[2]}"

    # Clean each to only digits (and optional leading minus)
    base=$(  clean_token "$base_raw" )
    exponent=$( clean_token "$exp_raw"   )
    modulo=$( clean_token "$mod_raw"     )

    # if any of them came back empty, skip this fuzz case
    if [[ -z $base || -z $exponent || -z $modulo || $modulo -eq 0 ]]; then
        continue
    fi

    if (( ${#modulo} > 12 )); then
        # Note my algorithm is not optimised to handle a very large modulo.
        continue
    fi

    echo "======================================"
    echo "TEST $loop_count -- Test Input:"
    echo "  Base = $base"
    echo "  Exponent = $exponent"
    echo "  Modulo = $modulo"

    if python3 ../fuzz_modular_exponentiation.py "$base" "$exponent" "$modulo"; then
        echo "Status -- PASS ✅"
    else
        code=$?
        echo
        echo "💥 Crash detected (exit code $code)"
        echo "Bad input: $test_input"
        echo "Status -- FAILED ❌"
        echo "======================================"
        break
    fi

    loop_count=$(( loop_count + 1 ))
done
