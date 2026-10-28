#!/usr/bin/env python3
"""run-solution.py <file.py> <func_name>: LeetCode-style problems are graded by calling a method, not
by stdin. Reads the arguments from stdin, one JSON value a line (the form LiveCodeBench gives samples
in), calls Solution().<func_name>(*args) from <file.py> and prints the result as JSON."""
import json, sys, importlib.util
import typing
path, fn = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("candidate", path)
mod = importlib.util.module_from_spec(spec)
mod.__dict__.update({k: getattr(typing, k) for k in typing.__all__})  # the starter code's annotations
spec.loader.exec_module(mod)
args = [json.loads(line) for line in sys.stdin.read().splitlines() if line.strip() != ""]
result = getattr(mod.Solution(), fn)(*args)
print(json.dumps(result, separators=(",", ":")))
