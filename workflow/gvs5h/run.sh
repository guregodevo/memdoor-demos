#!/usr/bin/env bash
# run.sh <file.py>: runs a candidate on the input on stdin the way the problem is graded — the method
# named in tests/func_name for a LeetCode-style problem, the script on stdin otherwise.
here=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
if [ -f tests/func_name ]; then
    exec python3 "$here/run-solution.py" "$1" "$(cat tests/func_name)"
fi
exec python3 "$1"
