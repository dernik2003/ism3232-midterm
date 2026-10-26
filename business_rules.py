"""Business calculations for Brightline Print Shop."""

MIN_VOLUME_COPIES = 200
MIN_BULK_COPIES = 1000
NO_DISCOUNT = 0.0
VOLUME_DISCOUNT = 0.08
BULK_DISCOUNT = 0.15
STUDENT_DISCOUNT_BONUS = 0.05
SETUP_FEE = 15.00
SETUP_FEE_LIMIT = 40.00
PROOF_TOTAL_LIMIT = 300.00
OVERNIGHT_COPIES_LIMIT = 500
OVERNIGHT_TOTAL_LIMIT = 400.00


def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Return the print cost before discounts or fees."""
    return copy_price * copies


def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Return the volume discount, including any student organization bonus."""
    if copies < MIN_VOLUME_COPIES:
        discount = NO_DISCOUNT
    elif copies < MIN_BULK_COPIES:
        discount = VOLUME_DISCOUNT
    else:
        discount = BULK_DISCOUNT

    if student_org and copies >= MIN_VOLUME_COPIES:
        discount += STUDENT_DISCOUNT_BONUS

    return discount


def calculate_job_total(
    copy_price: float, copies: int, student_org: bool = False
) -> float:
    """Return the discounted job cost plus any required setup fee."""
    cost = calculate_print_cost(copy_price, copies)
    discount = get_volume_discount(copies, student_org)
    discounted_cost = cost * (1 - discount)
    if discounted_cost < SETUP_FEE_LIMIT:
        return discounted_cost + SETUP_FEE
    return discounted_cost


def requires_proof(total: float) -> bool:
    """Return whether the job needs a printed proof."""
    return total > PROOF_TOTAL_LIMIT


def needs_overnight_run(copies: int, total: float) -> bool:
    """Return whether the job requires an overnight press run."""
    return copies > OVERNIGHT_COPIES_LIMIT or total > OVERNIGHT_TOTAL_LIMIT


def total_invoiced(jobs: list) -> float:
    """Return the total amount invoiced for the jobs using a loop."""
    total = 0.0
    for job in jobs:
        total += calculate_job_total(
            job["copy_price"], job["copies"], job["student_org"]
        )
    return total


def largest_job(jobs: list) -> str:
    """Return the first job title with the highest invoice amount."""
    largest_title = ""
    largest_total = None
    for job in jobs:
        job_total = calculate_job_total(
            job["copy_price"], job["copies"], job["student_org"]
        )
        if largest_total is None or job_total > largest_total:
            largest_total = job_total
            largest_title = job["title"]
    return largest_title


def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
    """Return one report line with currency and yes/no flags."""
    proof_text = "yes" if proof else "no"
    overnight_text = "yes" if overnight_run else "no"
    return (
        f"{title}: ${total:.2f} | proof: {proof_text} | overnight run: {overnight_text}"
    )
