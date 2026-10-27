Improve the gvs5h workflow in .memdoor/workflows/gvs5h without changing its roles,
prompts or loop: add a stress test as the ground truth for "done", because the public
samples let wrong solutions through (two problems passed 3/3 samples and failed 39 and
40 hidden tests).

After the public samples pass in a round, and only then (`when:`):

1. a worker llm task writes brute.py, a brute-force reference for task.md: the slowest
   obviously correct method, no cleverness, small inputs only;
2. a worker llm task writes gen.py, a random generator printing one small valid input of
   task.md per run (read the constraints; keep n tiny so brute.py finishes in a second);
3. a command task runs gen.py 200 times, feeds each input to solution.py and brute.py
   with a 2 s limit, and writes the first mismatch (the input, both outputs) or
   "stress ok" to stress-N.txt;
4. the manager of the next round reads stress-N.txt as ground truth, like the samples:
   a mismatch is a failing test with its input, and done is allowed only after
   "stress ok".

Keep the same model line on every llm task, `thinking high` only on the worker tasks
and `thinking low` on the manager, planner, ideation and summarizer tasks. Decide the
layout yourself from the workflow skill; do not stop to ask me questions, I am not at
the keyboard. Do not run it.
