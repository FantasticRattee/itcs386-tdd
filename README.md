# itcs386-tdd

ITCS386 Week 9 lab: Python unit testing with pytest and test-driven development.
Source: W9-TDD_Lab_Exercise_v7.pdf, 17 pages. Original course PDFs are not copied
into this public repository.

## Current status and collaboration

The code and tests for Part 0 and Part A (including optional A8) are complete:
42 tests pass. [REFLECTION.md](REFLECTION.md) is a draft containing the student's
confirmed learning note and measured facts for Question 1. Personal responses to
Questions 2-6 still await discussion and review; the submission is not complete.

The student and an AI assistant worked through this lab together. The student
entered and ran the early Part 0 examples while receiving explanations; after
requesting help completing the rest, the assistant executed additional test/code
steps and explained the concepts. The actual RED/GREEN runs and commits are
indexed in [TDD_HISTORY.md](TDD_HISTORY.md). No backdated history was fabricated.

## Setup

Python 3.10 or newer is required by the worksheet and pinned pytest version.
The completed suite was verified with Python 3.14.6 and pytest 9.1.1.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

On Windows, use `python` instead of `python3`, and activate with
`.venv\Scripts\activate` (Command Prompt) or `.venv\Scripts\Activate.ps1`
(PowerShell). Do not copy an existing virtual environment between machines.

## Files

| Worksheet scope | Production code | Tests / document |
| --- | --- | --- |
| Part 0: leap years | `leap.py` | `test_leap.py` (10 cases) |
| Part 0: account / fixtures / decimals | `bank.py` | `test_bank.py` (7 cases) |
| Part 0: shipping bug hunt | `shipping.py` | `test_shipping.py` (14 cases) |
| Part A: quantities / expressions / conversion | `kitchen.py` | `test_kitchen.py` (11 tests) |
| Part B: personal reflection | Not applicable | `REFLECTION.md` (draft; Questions 2-6 pending) |

Additional supporting files are `requirements.txt`, `.gitignore`,
[DEPENDENCIES.md](DEPENDENCIES.md), [TDD_HISTORY.md](TDD_HISTORY.md) and the
machine-path-redacted run archive in `evidence/`.

## Running tests (Step 0.7)

Activate the project virtual environment before these commands. Alternatively,
use `.venv/bin/python` instead of `python` on macOS/Linux.

```bash
python -m pytest -q       # one dot per test
python -m pytest -v       # names and results
python -m pytest -x       # stop at the first failure
python -m pytest -k leap  # only names/files matching leap
python -m pytest --lf     # last failures; all tests if none are recorded
```

## What the parts teach

- Part 0: assertions compare expected and actual results; `pytest.raises` checks
  expected exceptions; parametrization runs each row separately; fixtures give
  every requesting test a fresh account; `pytest.approx` handles float rounding.
  Shipping fixes are driven by the existing specification, not altered answers.
- Part A: Fake It starts with a constant, Triangulate forces a general formula,
  and Obvious Implementation is used when the next change is clear. Multiplication
  returns a new quantity. `plus` returns a deferred `Sum`. A `Converter` carries
  directional rates; the two sides are converted before their amounts are added.
- Part B: answer the six reflection questions honestly, using actual counts and
  experience rather than inventing difficulty or independent authorship.

In `leap.py`, `if` chooses an answer. A test checks that answer against a known
rule. Having an `if` does not guarantee its condition, order or return value is
correct. Passing the selected tests is not proof for all possible inputs.

## Submission and names

The worksheet (pages 1 and 17) requires ONE repository named `itcs386-tdd`.
Keep the exact module/test filenames above and `REFLECTION.md`. It does not give
a student-ID prefix or a mandatory ZIP filename; do not rename importable modules.

After finishing/reviewing the reflection, submit either:

1. The updated public repository link on MyCourses. Ensure the completed local
   commits have been pushed and are visible before submitting the URL.
2. A ZIP of the repository INCLUDING its hidden `.git` directory, so the marker
   can inspect the RED/GREEN commit history. `itcs386-tdd-submission.zip` is a
   suggested name only, not a worksheet-mandated convention. Exclude `.venv/`,
   `.vscode/`, `__pycache__/` and `.pytest_cache/`.

Repository: <https://github.com/FantasticRattee/itcs386-tdd>.
Completion work is local until an explicit push is performed. No MyCourses
submission was made by the assistant. The PDF gives no calendar deadline: check
the actual MyCourses assignment for its deadline and any additional instructions.

## Deliberate scope limits

This is the worksheet's example, not a production banking or unit-validation
library. Negative withdrawals, non-numeric/non-finite shipping weights and
Quantity comparison with arbitrary unrelated objects are not specified here.
Hashability is deliberately deferred as the worksheet suggests; quantities are
not usable as set members/dictionary keys. The original supplied bank behavior
and shipping specification are preserved rather than silently expanded.
