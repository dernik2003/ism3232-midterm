# Terminal Record: Brightline Print Shop

## 1. Building the project

```bash
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
git init -b main
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pytest ruff
python3 -m pip freeze > requirements.txt
mkdir tests
touch business_rules.py main.py commands.md README.md .gitignore tests/__init__.py tests/test_business_rules.py
printf '.venv/\n__pycache__/\n.pytest_cache/\n.ruff_cache/\n' > .gitignore
code .
git add .
git commit -m "Initialize midterm project structure"
git remote add origin https://github.com/dernik2003/ism3232-midterm.git
git branch -M main
git push -u origin main
```

## 2. The virtual environment

```bash
which python3
```

```text
/Users/nikitalemeshenko/ism3232-midterm/.venv/bin/python3
```

The Python path includes `.venv/bin/python3`, confirming that the virtual environment is active.

## 3. The project structure

```bash
tree -L 2
```

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-313.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The `.venv` folder exists locally but is excluded from GitHub by `.gitignore`.

## 4. Every function and test

```bash
rg 'def '
```

```text
business_rules.py:def calculate_print_cost(copy_price: float, copies: int) -> float:
business_rules.py:def get_volume_discount(copies: int, student_org: bool = False) -> float:
business_rules.py:def calculate_job_total(
business_rules.py:def requires_proof(total: float) -> bool:
business_rules.py:def needs_overnight_run(copies: int, total: float) -> bool:
business_rules.py:def total_invoiced(jobs: list) -> float:
business_rules.py:def largest_job(jobs: list) -> str:
business_rules.py:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
tests/test_business_rules.py:def test_print_cost_multiplies_price_by_copies():
tests/test_business_rules.py:def test_print_cost_zero_copies_is_zero():
tests/test_business_rules.py:def test_discount_below_200_copies_is_zero():
tests/test_business_rules.py:def test_discount_exactly_200_copies_is_eight_percent():
tests/test_business_rules.py:def test_discount_999_copies_is_eight_percent():
tests/test_business_rules.py:def test_discount_exactly_1000_copies_is_fifteen_percent():
tests/test_business_rules.py:def test_student_org_below_200_gets_no_bonus():
tests/test_business_rules.py:def test_student_org_changes_discount_at_200():
tests/test_business_rules.py:def test_student_org_gets_twenty_percent_at_1000():
tests/test_business_rules.py:def test_job_total_applies_volume_discount():
tests/test_business_rules.py:def test_job_total_applies_student_bonus():
tests/test_business_rules.py:def test_setup_fee_applies_below_forty_dollars():
tests/test_business_rules.py:def test_setup_fee_not_added_at_exactly_forty_dollars():
tests/test_business_rules.py:def test_setup_fee_uses_discounted_cost_not_original_cost():
tests/test_business_rules.py:def test_proof_not_required_at_exactly_300_dollars():
tests/test_business_rules.py:def test_proof_required_above_300_dollars():
tests/test_business_rules.py:def test_overnight_not_required_at_500_copies_and_small_total():
tests/test_business_rules.py:def test_overnight_required_above_500_copies_and_small_total():
tests/test_business_rules.py:def test_overnight_not_required_at_400_dollars_and_few_copies():
tests/test_business_rules.py:def test_overnight_required_above_400_dollars_and_few_copies():
tests/test_business_rules.py:def test_overnight_required_when_both_conditions_are_true():
tests/test_business_rules.py:def test_total_invoiced_for_two_jobs():
tests/test_business_rules.py:def test_total_invoiced_empty_list_is_zero():
tests/test_business_rules.py:def test_largest_job_returns_title_of_highest_total():
tests/test_business_rules.py:def test_largest_job_returns_first_title_on_tie():
tests/test_business_rules.py:def test_largest_job_empty_list_returns_empty_string():
tests/test_business_rules.py:def test_largest_job_first_only():
tests/test_business_rules.py:def test_format_job_line_formats_no_flags_and_two_decimals():
tests/test_business_rules.py:def test_format_job_line_formats_yes_flags_and_two_decimals():
tests/test_business_rules.py:def test_format_job_line_formats_mixed_flags():
```

`business_rules.py` defines 8 functions and `tests/test_business_rules.py` defines 30 tests.

## 5. Which files print

```bash
rg -l 'print'
```

```text
main.py
business_rules.py
README.md
tests/test_business_rules.py
tests/__init__.py
commands.md
```

Only `main.py` calls `print()` to display the report; `business_rules.py` also appears in the search because `calculate_print_cost` contains the text `print`, and the other matches are files that mention the same word.

## 6. The commit history

```bash
git log --oneline
```

```text
cfd4753 changed title to largest job total
7f00c4c fixed section 6
2719554 Correct largest job report label
04aaa52 Update command history references
ae608c6 updated commands.md - removed a note
bffd5a1 Updated Readme
80ccfd1 Clarify terminal search results in the command record
2ec9945 Simplify README wording and clarify project description
373b1a1 Add verified terminal record
d545362 Revise project documentation
317dfa0 Document project setup and business rules
454500a Add 30 tests for pricing rules and edge cases
92934ea Implement print shop pricing and business rules
5178398 Add print shop report and summary calculations
a2d1582 Add Python dependencies and test package
```

There were 15 commits immediately before committing this terminal record.
