# Change-impact map

Updated: 2026-10-20. Read this map before changing lab behavior. The
impact-check workflow uses it to keep code, tests and handoff documentation aligned.

## Artifact inventory

- Canonical production code: `leap.py`, `bank.py`, `shipping.py`, `kitchen.py`.
- Canonical checks: matching `test_*.py` modules; all tests run with pytest.
- Live overview: `README.md`. `REFLECTION.md` awaits the student's own answers,
  not invented experience. `TDD_HISTORY.md` and `evidence/tdd_runs.json` index
  observed runs.
- No diagrams, generated code, external services, database or embedded figures.

## Impact matrix

| Change | Code files | Diagrams / figures | Documentation | Also sync |
| --- | --- | --- | --- | --- |
| Leap-year behavior | `leap.py`, `test_leap.py` | None | README Part 0, TDD history | Whole pytest suite |
| Account behavior / fixture | `bank.py`, `test_bank.py` | None | README Part 0, TDD history | Fresh fixture per test |
| Shipping fee rules | `shipping.py`, `test_shipping.py` | None | README Part 0, TDD history | Preserve specification docstring |
| Quantity / Sum / Converter | `kitchen.py`, `test_kitchen.py` | None | README Part A, TDD history, reflection counts | Test-list checkboxes and RED/GREEN commits |
| Runtime / delivery | `requirements.txt`, `.gitignore` | None | README setup/submission | Fresh-copy verification; exclude local environments |

## Internal graph and contracts

`test_leap.py -> leap.py`; `test_bank.py -> bank.py`;
`test_shipping.py -> shipping.py`; `test_kitchen.py -> kitchen.py`.
Quantity and Sum must expose compatible reduction methods. Converter owns the
directional conversion-rate table and is passed into expression reduction.

## Known sync debts

Part 0 and Part A through optional A8 are implemented and 42 tests pass.
Personal reflection remains pending student input/review; do not label the whole
submission complete until it is present. Counts in README and reflection must be
recomputed whenever tests or production code change.
Original worksheet PDFs are read-only references outside the public repository.
