# itcs386-tdd
ITCS386 Week 9 lab: Python unit testing with pytest and test-driven development.

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
