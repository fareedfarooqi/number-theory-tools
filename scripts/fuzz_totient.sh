#!/usr/bin/env bash

# So I'm just placing all my seed files into an array.
seeds=(../seeds/seed-1.txt ../seeds/seed-2.txt ../seeds/seed-3.txt ../seeds/seed-4.txt ../seeds/seed-5.txt)

loop_count=1

# We have an infinite loop. It'll stop once the program crashes.
while true; do
    # So we are randomly picking a file to be our seed file.
    idx=$(( RANDOM % ${#seeds[@]} ))
    seed="${seeds[$idx]}"

    # So here we are passing all three files to our radamsa program.
    # The program will then under the hood select the file and read
    # it's contents and use that as a seed. Radamsa will then mutate
    # that seed in some way and we then store the mutated input.
    test_input=$(radamsa -n 1 "$seed" | head -n1)

    # We skip and empty lines.
    if [ -z "$test_input" ]; then
        continue
    fi

    # We will print out the seed input for the user's convenience.
    echo "======================================"
    echo "TEST $loop_count -- Test Input: $test_input"

    if python3 ../fuzz_totient.py <<< "$test_input"; then
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