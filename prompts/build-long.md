Build me a workflow named gvs5h that reproduces the GVS5H harness in
/Users/gregoryd/Dev/GVS5H/codebase/v2-current/escalation/multiagent.py, the one the
paper "Five Qwen3.8-27B models match Claude Fable 5 on LiveCodeBench" is about. Read
that file first and keep its roles, its prompts and its loop; do not invent a better
method.

The harness is one model in fresh contexts, five agents sharing a ledger on disk:

1. the primary plans: reads task.md, writes plan.md (a 3 to 6 sentence strategy) and
   the first task list to tasks.json;
2. the ideation worker: reads the problem and the plan, writes several genuinely
   different approaches with their pitfalls to notes.md, no code;
3. the manager (the primary again): reads the current solution, the notes, the task
   list and the latest worker report; curates the list, decides done or continue, and
   names the single next task; it may only say done when the public sample tests
   passed;
4. the worker: takes that one task, builds on the current solution.py and notes or
   writes a fresh solution for a different approach, replaces solution.py and
   notes.md, reports status and next steps; when the worker is cut off at the token
   limit a summarizer digests its partial reply for the manager;
5. after each worker the public sample tests in tests/ are run against solution.py and
   the manager is told the verdict as ground truth.

Manager and worker alternate for at most 10 rounds; the manager stops early when it
reissues the same task twice. If the loop ends without done, a final worker call
produces the definitive solution.py from everything in the ledger.

Every role is a workflow task Memdoor runs, not a script: an llm task whose model
line routes the call through the gateway,
  model: openrouter:qwen/qwen3.8-27b thinking high order modal,coreweave,parasail,wafer
Do not write code that calls OpenRouter or any API yourself; the sample-test step is
a command task. A workflow is a DAG with no loop: unroll manager and worker into 10
numbered rounds, and make a round whose manager has already said done do nothing but
pass the ledger on. Section formats as in the file.

The orchestration IS the workflow: one YAML task per role per round, the ledger
passed between them through the files on disk and `requires`, the way the team-solve
workflow in ~/.memdoor/workflows/team-solve does it. No pipeline script, no Python
orchestrator, no ledger-keeper code: an llm task's prompt reads the ledger files and
its output is written to the file it owns. The only code allowed is the shell
command that runs the public samples against solution.py.

Decide the layout yourself from the workflow skill; do not stop to ask me questions,
I am not at the keyboard.

The problem folder holds task.md (the statement, with its input and output format)
and tests/N.in with tests/N.out for the public samples. The workflow's result is
solution.py. Run the public samples at the end and write the verdict to
test-status.txt.

Build it, then run it on the sample problem in this folder and show me the ledger.
