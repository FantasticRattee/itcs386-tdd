# TDD run history

These are real observed runs from the collaborative, AI-assisted lab session on
2026-10-20 (Asia/Bangkok), not a claim that every line was written independently.
Existing commits were preserved; no dates or earlier commits were rewritten.
The raw result archive is [evidence/tdd_runs.json](evidence/tdd_runs.json), with
machine-specific paths redacted. Timestamps in that JSON are UTC.

## Earlier work and baseline

- `146720d`: the student's first leap-year test passed.
- `e15ed49`: the student's corrected expectation for 1900.
- `60be1ca`: preserves the student's existing guided Part 0 work, including the
  then-uncommitted leap/bank tests, before assisted completion (11 tests passed).
- Part 0 deliberately tests supplied production code after it exists. Part A is
  test-first, as specified by the worksheet.

## Observed steps

| Step / purpose | Exit | Commit | Actual pytest result |
| --- | ---: | --- | --- |
| 0.3 GREEN: six parametrized leap-year inputs | 0 | `18b96a8` | 13 passed in 0.01s |
| 0.4 GREEN: negative years rejected | 0 | `e641e77` | 14 passed in 0.01s |
| 0.5 GREEN: all six fixture-based bank cases | 0 | `2a30709` | 16 passed in 0.01s |
| 0.6 RED: exact float comparison exposes rounding | 1 | `ee8dad8` | 1 failed, 16 passed in 0.01s |
| 0.6 GREEN targeted: rerun last failure | 0 | run only | 1 passed in 0.00s |
| 0.6 GREEN: approximate decimal comparison | 0 | `3a11768` | 17 passed in 0.01s |
| 0.7 GREEN: quiet | 0 | run only | 17 passed in 0.01s |
| 0.7 GREEN: verbose | 0 | run only | ============================== 17 passed in 0.01s ============================== |
| 0.7 GREEN: stop on failure | 0 | run only | 17 passed in 0.01s |
| 0.7 GREEN: name filter | 0 | run only | 10 passed, 7 deselected in 0.01s |
| 0.7 GREEN: last-failed selection | 0 | `f30746f` | 17 passed in 0.01s |
| 0.8 RED: shipping exposes three specification defects | 1 | `164effd` | 5 failed, 26 passed in 0.02s |
| 0.8 GREEN: original shipping specification satisfied | 0 | `fcead01` | 31 passed in 0.01s |
| A1 RED: first client before kitchen module exists | 2 | `300ca3b` | 1 error in 0.04s |
| A1 GREEN: Fake It with the constant 600 | 0 | `959ae40` | 32 passed in 0.01s |
| A2 RED: second example rejects the fake constant | 1 | `00ca6f7` | 1 failed, 32 passed in 0.02s |
| A2 GREEN: general multiplication formula | 0 | `9ec27db` | 33 passed in 0.01s |
| A3 RED: return values and original quantity preservation | 1 | `9f93ac0` | 2 failed, 31 passed in 0.02s |
| A3 GREEN: return a new value object | 0 | `be48107` | 33 passed in 0.01s |
| A4 RED: contents must define equality | 1 | `21c0537` | 1 failed, 33 passed in 0.02s |
| A4 RED: fake equality caught by unequal amounts | 1 | `1f72c52` | 1 failed, 33 passed in 0.02s |
| A4 GREEN: compare amounts | 0 | `ef2645e` | 34 passed in 0.01s |
| A4 REFACTOR: earlier clients compare whole quantities | 0 | `eaa2c00` | 34 passed in 0.01s |
| A5 RED: quantities must carry and preserve units | 1 | `e71d7f4` | 5 failed, 31 passed in 0.02s |
| A5 GREEN: amount-and-unit value objects | 0 | `9e57c53` | 36 passed in 0.01s |
| A5 REFACTOR: unit factories simplify callers | 0 | `e33dd1e` | 36 passed in 0.01s |
| A6 RED: first addition client requests a converter | 2 | `71c8692` | 1 error in 0.04s |
| A6 GREEN: Fake It addition with 500 grams | 0 | `08e19f4` | 37 passed in 0.01s |
| A6 RED: addition must retain an unevaluated plan | 1 | `6988731` | 1 failed, 37 passed in 0.02s |
| A6 RED: converter cannot yet reduce the new Sum | 1 | `4a58af8` | 1 failed, 37 passed in 0.02s |
| A6 GREEN: polymorphic reduction evaluates the plan | 0 | `f828d47` | 38 passed in 0.02s |
| A7 GREEN baseline: same-unit behavior already exists | 0 | `2b7f4b2` | 39 passed in 0.02s |
| A7 RED oracle check: intentional wrong expected amount | 1 | `745be5a` | 1 failed, 38 passed in 0.02s |
| A7 GREEN oracle check: restore the correct expectation | 0 | `8d141ae` | 39 passed in 0.02s |
| A7 RED: mixed-unit addition needs a rate API | 1 | `c701445` | 1 failed, 39 passed in 0.02s |
| A7 RED: empty add_rate exposes the incorrect raw total 201 | 1 | `e80d378` | 1 failed, 39 passed in 0.02s |
| A7 RED: storing rates alone cannot fix raw addition | 1 | `9c7481b` | 1 failed, 39 passed in 0.02s |
| A7 RED: converter travels through reduction | 1 | `54814b3` | 1 failed, 39 passed in 0.02s |
| A7 GREEN: reduce both operands before adding | 0 | `1ad5082` | 40 passed in 0.02s |
| A7 GREEN: direction regression rejects divide-instead-of-multiply | 0 | `da2da18` | 41 passed in 0.02s |
| A8 RED optional: scale a deferred mixed-unit sum | 1 | `8368f6b` | 1 failed, 41 passed in 0.02s |
| A8 GREEN optional: scale each operand without mutation | 0 | `f1af532` | 42 passed in 0.02s |

## Independent verification and scope

An independent reviewer exported each of the 37 lab-step commits after `60be1ca`
through `f1af532` into isolated temporary directories and reran pytest. All 37
matched their labels: RED was nonzero, GREEN/REFACTOR was zero; no mismatches.
A1's missing module and A6's missing Converter are intentional collection errors,
per the worksheet. A7's temporary 501 expectation is explicitly an oracle-check
exercise, not a production defect. The final A8 snapshot passed 42 tests.

A separate code review and inline probes checked shipping boundary neighbors,
converter isolation/direction, non-mutating quantities and deferred sum scaling.
This is lab-scope validation, not proof for every possible input or production use.

## Reading the history

```bash
git log --oneline --reverse
git show <commit>:test_kitchen.py
git show <commit>:kitchen.py
```

RED snapshots intentionally contain incomplete or failing code. Use the current
branch tip for the completed implementation. Do not run old snapshots expecting
them all to pass.

