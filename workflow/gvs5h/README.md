gvs5h reproduces the GVS5H multi-agent harness (escalation/multiagent.py): one model
(`openrouter:qwen/qwen3.8-27b`, thinking high) in fresh contexts, five roles sharing an
on-disk ledger. A primary planner writes plan.md and the first tasks.json; an ideation
worker appends several genuinely different approaches to notes.md; then the manager
(the primary again) and the worker alternate for up to 10 rounds: the manager reads the
current solution, the notes, the task list and the latest worker digest, curates the
list and names ONE next task (it may only say done when the public samples passed);
the worker owns solution.py and notes.md; a summarizer digests each worker reply for
the manager (and reports a token-limit cut-off); after each worker the public samples
in tests/ run against solution.py and the verdict is ground truth for the next manager.
A round whose manager already said done (or which reissued the same task twice) does
nothing but pass the ledger on. A final worker call produces the definitive solution.py
unless the manager already said done with samples passing.

Every role is a workflow task; the ledger is passed between them through the files on
disk and `requires`. No pipeline script and no ledger-keeper program: llm prompts read
the ledger as inlined upstream outputs, and downstream command tasks land each reply on
the file its role owns (the sed/awk one-liners in the commands are heredoc plumbing that
split the mandatory `### SECTION` headers of the harness onto disk, nothing more). The
only real code is check-samples.sh, the public-sample runner. Needs Python 3, bash,
diff, task.md and paired tests/*.in / tests/*.out in the project. Run it with
/workflow:gvs5h. It leaves plan.md, notes.md, tasks.json, solution.py, per-round
manage-reply-rN.md / worker-reply-rN.raw / digest-rN.md / next-rN.txt /
test-output-rN.log, final-test-output.log and test-status.txt.
