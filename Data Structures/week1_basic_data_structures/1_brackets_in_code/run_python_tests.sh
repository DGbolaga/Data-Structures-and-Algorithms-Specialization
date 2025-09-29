#!/bin/bash 

for i in $(seq -f "%02g" 1 54); do
  test_file="tests/$i"
  answer_file="tests/$i.a"

  if [ -f "$test_file" ]; then
    output=$(python3 check_brackets.py < "$test_file")
    expected_output=$(cat "$answer_file")

    if [[ "$output" == "$expected_output" ]]; then
      echo "Test $i: PASSED"
    else
      echo "Test $i: FAILED"
    fi
  fi
done