# ISM3232 Midterm: Brightline Print Shop

- **Name:** Nikita Lemeshenko
- **Version:** GAMMA
- **Date:** October 25, 2026

## What This Program Does

This program makes an invoice report for Brightline Print Shop. It works out the price of each job using discounts and setup fees. It also checks if a job needs a printed proof or an overnight run and shows a summary at the end.

## Business Rules

1. The starting cost is the price per copy multiplied by the number of copies.
2. Jobs under 200 copies get no discount. Jobs with 200–999 copies get 8%, and jobs with 1,000 or more get 15%.
3. Student organizations get an extra 5 percentage points off if they order at least 200 copies.
4. Add a $15 setup fee if the cost after discounts is under $40.
5. Jobs over $300 need a printed proof.
6. Jobs with more than 500 copies or a final total over $400 need an overnight run.

## How to Run

Open the project folder in Terminal and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## How to Test

There are 30 tests for the eight functions and the rule limits. Run these commands after activating the virtual environment:

```bash
ruff format --check .
ruff check .
pytest -v
```

## Files in This Repository

- `business_rules.py` — calculates costs, discounts, and report lines.
- `main.py` — contains the jobs and prints the report.
- `commands.md` — records terminal commands and their outputs.
- `README.md` — explains the project and how to run it.
- `requirements.txt` — lists the Python packages.
- `.gitignore` — keeps local files out of GitHub.
- `tests/__init__.py` — marks the tests folder as a Python package.
- `tests/test_business_rules.py` — contains the 30 tests.

## AI Use Statement

I used AI to help with the code, tests, README, and final GitHub check.
