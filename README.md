# ISM3232 Midterm: Brightline Print Shop

- **Name:** Nikita Lemeshenko
- **Version:** GAMMA
- **Date:** October 25, 2026

## What This Program Does

This Python application calculates and reports invoices for Brightline Print Shop.
Each print job is priced using the number of copies, volume discounts, and any
student organization discount or setup fee. The report identifies jobs that need
a printed proof or overnight press run and summarizes total invoices.

## Business Rules

1. The base printing cost equals the price per copy multiplied by the number of copies.
2. Jobs below 200 copies receive no volume discount; 200–999 copies get 8%; and 1,000 or more get 15%.
3. Registered student organizations receive five additional percentage points of discount for jobs of at least 200 copies.
4. Add a $15 setup fee when the discounted cost is less than $40.
5. Require a printed proof when the final job total exceeds $300.
6. Require an overnight press run when the job exceeds 500 copies or its final total exceeds $400.

## How to Run

From the repository folder, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## How to Test

The project contains 30 pytest tests covering all eight functions and all threshold boundaries.
With the virtual environment active, run:

```bash
ruff format --check .
ruff check .
pytest -v
```

## Files in This Repository

- `business_rules.py` — print-shop calculations and report-line formatting.
- `main.py` — sample jobs and the printed business report.
- `commands.md` — terminal commands, output evidence, and Git commit record.
- `README.md` — overview, rules, installation, testing, and disclosure.
- `requirements.txt` — Python dependencies exported with `pip freeze`.
- `.gitignore` — excluded local environments, Python caches, and tool caches.
- `tests/__init__.py` — test-package initializer.
- `tests/test_business_rules.py` — pytest tests for calculations and boundaries.

## AI Use Statement

AI assistance was used to draft and test this project; all submitted work and any
instructor permission to use AI must be represented accurately.
