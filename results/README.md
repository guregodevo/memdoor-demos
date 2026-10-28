# Results: what is kept and where it comes from

Every number in the top-level README traces to a file here.

- `harness-stress-27b.tsv`: one row per problem of the ten, solved or not, hidden tests,
  calls, cost, and a note on what happened. Hand-kept from the files below.
- `the-ten-rows.tsv`: the bench runner's own rows as they landed (id, run status, public
  samples, hidden tests, seconds). A problem run more than once has more than one row;
  "failed" is the run's status (the manager never said done), not the grade.
- `the-ten-report.md`: `bench/report.py` over those rows, the run logs and the ledger:
  calls, tokens and cost per problem for the run id in each log.
- `meter-stress-harness.jsonl`: every model call of every stress-harness run, as the
  gateway's ledger recorded it (`~/.memdoor/meter.jsonl`): time, run id, model, tokens,
  duration, cost, OpenRouter generation id. Sum the rows of a run id for its bill; the
  generation id answers to OpenRouter's generation API for the host that served it.
- `runs/<id>/`: the ledger the harness left in each problem's folder after its last run:
  `plan.md`, `notes.md`, `tasks.json`, the per-round manager replies, worker replies,
  digests, sample and stress verdicts, `brute.py`, `gen.py`, `solution.py` and
  `test-status.txt`. The problem statements and tests are LiveCodeBench's and are not
  copied; `bench/materialize.py` and `bench/functional-tests.py` rebuild them.
- `harness-27b-ten-partial.tsv`, `single-27b-thinking-24.tsv`, `*-thinking-off-100.tsv`:
  the earlier arms, kept for the record (the README says what each was).

Grades are `bench/grade.py` with LiveCodeBench's own grader, raw (the authors also report
a patched grade). The authors' per-problem verdicts come from `runs/patched_verdicts.json`
in their repository, read by `bench/authors.py`.
