# What I learned building a team-solve harness

*Draft. Every number links to a file in [memdoor-demos/results](../results/README.md).*

A paper went around last week: five Qwen3.8-27B agents sharing a ledger on disk match
Claude Fable 5 on LiveCodeBench. Their harness is a Python program. I wanted to know two
things: can my coding agent build that harness from one prompt, as a workflow rather than
a script, and does it hold up when you run it and pay the bill yourself.

Short answer: yes, and mostly. Seven of their first ten problems solved on all hidden tests
for $4.95, one pass, against their ten of ten in four passes of five. The gap is one hard
problem the 27B could not crack and one problem my harness lost on its own mistakes. The
rest of this post is what the mistakes taught me, because that is where the value was.

![the ten](../results/the-ten.svg)

## The setup

One prompt builds the harness: six lines naming the paper's file, the five roles, the loop
and the model line. The coder reads their code, loads Memdoor's workflow skill and writes
one YAML task per role per round, 92 tasks, the ledger passed between them through files.
No orchestrator code; the only program is the shell line that runs the public samples.

One line solves a problem: `/workflow:gvs5h` in the problem's folder.

Every call goes through my own OpenRouter key and lands in the gateway's ledger with the
run that made it, so each number below is a sum over a run id.

## 1. The orchestration is worth ten points. The model alone is not Claude.

The paper's own table, same grader, their hundred problems: 27B one call 77 to 80, 27B
with their harness 87 to 89, Fable 5 one call 86 to 89. The harness closes the gap, not the
model. That is the whole reason to build harnesses out of small models.

## 2. Ground truth decides the harness.

Their manager may only say done when the public samples pass. Two of my first six problems
said done with the samples green and failed 39 and 40 hidden tests. The fix was the oldest
trick in competitive programming: a brute-force reference and a random generator, written
once, and a command task per round that diffs the two on 200 small inputs before done is
allowed. arc196_a went from 4 of 43 to 43 of 43, arc196_d from 2 of 42 to 42 of 42. Both are
problems Fable 5 alone misses in some passes.

## 3. The reference can be wrong, and the harness must know which program failed.

On arc196_c the brute force raised an IndexError. My stress step said "solution.py or
brute.py crashed" and the manager spent three rounds fixing a solution that had passed the
samples. A verdict has three states, not two: ok, failed, and inconclusive because the
reference itself broke. Inconclusive now names brute.py, and the worker is allowed to
rewrite it.

## 4. A loop needs a mechanical stop, and idle rounds must cost nothing.

A workflow is a DAG, so the loop is unrolled into ten numbered rounds. The first build kept
running rounds after the manager said done and overwrote a correct solution; another run
reissued the same task to the worker forever. Eight idle rounds were 60 percent of one
problem's bill. The rules went into the engine and the skill: a round after done is skipped
by a shell condition on the task (`when:`), the manager stops when it reissues the same task
twice, and a cancelled run ends instead of retrying its upstreams.

## 5. Cap the reply.

One worker thought for 434,019 tokens on a host that allows 235K. A dollar for one call. The
paper ran at 128K; the model line now carries `max_tokens 128000` and the gateway caps every
task's reply under the provider's ceiling.

## 6. Reasoning can eat the answer.

Four plan calls on arc196_c came back with finish=stop, 19K to 51K tokens of reasoning and
an empty answer. Not cut off: finished. The same prompt without thinking answers in one go.
The gateway now asks an llm task again without thinking when a reply is empty after
reasoning. I had also put the manager-side roles on thinking low to save money; that made
it worse, and it was not the paper's setting. Everything went back to high.

## 7. A harness that knows one input format runs blind on the other.

27 of the hundred problems are LeetCode-style: no stdin, a class with a method the grader
calls. My rig had no sample files for them, so the samples said "no inputs found" every
round, the stress test never ran, and the harness went ten rounds blind. The ledger looked
healthy. 3777 was solved anyway, which is how I almost missed it. Now the samples are written
as argument files, a small driver calls the method, and 3717 and 3765 went through in four
and three minutes.

## 8. The workflow engine is part of the harness.

The scheduler re-expanded a task on every visit of the backfill walk. On a 92-task DAG that
is every path from the sinks to the roots: tens of thousands of submits a minute, half a
gigabyte of log a minute, 7 GB in half an hour and 40 GB the night before. A waiting task is
now expanded once and woken by its requirement's completion; the walk's trace lines log at
debug; the gateway's log has a 1 GB ceiling and prunes in batches so it never locks its own
writers. None of that is visible in a benchmark table, all of it decides whether the run
finishes.

## 9. One problem, one receipt, then the next.

I burned $3.51 before I had a single end-to-end receipt, by launching the hundred the way
you launch a script. The rule since: one problem through the whole rig, read the row, read
the bill, then the next. Every bug above was found by a single watched run. The batch of ten
was run one at a time with a row landing per problem.

## 10. Let the agent build it; fix only what a run proved wrong.

I never hand-wrote the YAML. Each time the run exposed a wrong line, I fixed that line, and
when the lesson was general it went into the workflow skill as a rule, so the next build
from the next prompt does not repeat it: tasks are the orchestration, decide instead of
asking when headless, a loop has a bound and a stop rule, a condition is a check.

## 11. Keep the data.

Every number here traces to a file: the ledger each run left behind, the meter rows of every
call with its OpenRouter generation id, the runner's rows, the per-problem report. A table
without the files behind it is a claim.

## What is not apple to apple

My grades are raw with the benchmark's own grader; the authors also report a patched grade.
They served the model on their own hardware; mine went to whichever of four OpenRouter
hosts answered first, with different output windows. Ten problems, one pass, against their
hundred times five. The hundred is next, one pass, and the same workflow with the model
line pointed at a 27B running on a box of my own.
