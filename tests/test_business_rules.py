"""Tests for the Brightline Print Shop business rules."""

from business_rules import (
    calculate_job_total,
    calculate_print_cost,
    format_job_line,
    get_volume_discount,
    largest_job,
    needs_overnight_run,
    requires_proof,
    total_invoiced,
)


def test_print_cost_multiplies_price_by_copies():
    assert round(calculate_print_cost(1.25, 8), 2) == 10.00


def test_print_cost_zero_copies_is_zero():
    assert round(calculate_print_cost(1.25, 0), 2) == 0.00


def test_discount_below_200_copies_is_zero():
    assert get_volume_discount(199) == 0.00


def test_discount_exactly_200_copies_is_eight_percent():
    assert get_volume_discount(200) == 0.08


def test_discount_999_copies_is_eight_percent():
    assert get_volume_discount(999) == 0.08


def test_discount_exactly_1000_copies_is_fifteen_percent():
    assert get_volume_discount(1000) == 0.15


def test_student_org_below_200_gets_no_bonus():
    assert get_volume_discount(199, student_org=True) == 0.00


def test_student_org_changes_discount_at_200():
    assert get_volume_discount(200, student_org=False) == 0.08
    assert get_volume_discount(200, student_org=True) == 0.13


def test_student_org_gets_twenty_percent_at_1000():
    assert get_volume_discount(1000, student_org=True) == 0.20


def test_job_total_applies_volume_discount():
    assert round(calculate_job_total(1.20, 250), 2) == 276.00


def test_job_total_applies_student_bonus():
    assert round(calculate_job_total(0.80, 500, student_org=True), 2) == 348.00


def test_setup_fee_applies_below_forty_dollars():
    assert round(calculate_job_total(39.99, 1), 2) == 54.99


def test_setup_fee_not_added_at_exactly_forty_dollars():
    assert round(calculate_job_total(40.00, 1), 2) == 40.00


def test_setup_fee_uses_discounted_cost_not_original_cost():
    assert round(calculate_job_total(0.21, 200), 2) == 53.64


def test_proof_not_required_at_exactly_300_dollars():
    assert requires_proof(300.00) is False


def test_proof_required_above_300_dollars():
    assert requires_proof(300.01) is True


def test_overnight_not_required_at_500_copies_and_small_total():
    assert needs_overnight_run(500, 100.00) is False


def test_overnight_required_above_500_copies_and_small_total():
    assert needs_overnight_run(501, 100.00) is True


def test_overnight_not_required_at_400_dollars_and_few_copies():
    assert needs_overnight_run(100, 400.00) is False


def test_overnight_required_above_400_dollars_and_few_copies():
    assert needs_overnight_run(100, 400.01) is True


def test_overnight_required_when_both_conditions_are_true():
    assert needs_overnight_run(501, 400.01) is True


def test_total_invoiced_for_two_jobs():
    jobs = [
        {"title": "A", "copy_price": 0.25, "copies": 100, "student_org": False},
        {"title": "B", "copy_price": 1.20, "copies": 250, "student_org": False},
    ]
    assert round(total_invoiced(jobs), 2) == 316.00


def test_total_invoiced_empty_list_is_zero():
    assert round(total_invoiced([]), 2) == 0.00


def test_largest_job_returns_title_of_highest_total():
    jobs = [
        {"title": "Small", "copy_price": 0.25, "copies": 100, "student_org": False},
        {"title": "Large", "copy_price": 1.20, "copies": 250, "student_org": False},
    ]
    assert largest_job(jobs) == "Large"


def test_largest_job_returns_first_title_on_tie():
    jobs = [
        {"title": "First", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "Second", "copy_price": 1.00, "copies": 100, "student_org": False},
    ]
    assert largest_job(jobs) == "First"


def test_largest_job_empty_list_returns_empty_string():
    assert largest_job([]) == ""


def test_largest_job_first_only():
    jobs = [{"title": "Only", "copy_price": 1.00, "copies": 1, "student_org": False}]
    assert largest_job(jobs) == "Only"


def test_format_job_line_formats_no_flags_and_two_decimals():
    assert (
        format_job_line("Flyers", 40.0, False, False)
        == "Flyers: $40.00 | proof: no | overnight run: no"
    )


def test_format_job_line_formats_yes_flags_and_two_decimals():
    assert (
        format_job_line("Booklets", 456.75, True, True)
        == "Booklets: $456.75 | proof: yes | overnight run: yes"
    )


def test_format_job_line_formats_mixed_flags():
    assert (
        format_job_line("Banners", 360.0, True, False)
        == "Banners: $360.00 | proof: yes | overnight run: no"
    )
