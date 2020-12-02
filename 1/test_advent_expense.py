import pytest
import advent_expense

good_entries_2 = [0, 3]
good_entries_3 = [1, 2, 4]

@pytest.fixture
def good_entries_fix_2():
    return good_entries_2

@pytest.fixture
def good_entries_fix_3():
    return good_entries_3

@pytest.fixture
def example_expense_report():
    return [1721, 979, 366, 299, 675, 1456]

@pytest.fixture
def example_bad_expense_report():
    return [1, 2, 3, 4, 5]

def test_find_sum_2(example_expense_report):
    entries = advent_expense.find_by_sum(example_expense_report, 2, 2020)
    assert entries == good_entries_2 or entries == good_entries_2[::-1]

def test_find_sum_3(example_expense_report):
    entries = advent_expense.find_by_sum(example_expense_report, 3, 2020)
    assert entries == good_entries_3 or entries == good_entries_3[::-1]

def test_find_sum_none(example_bad_expense_report):
    entries = advent_expense.find_by_sum(example_bad_expense_report, 2, 2020)
    assert not entries

def test_get_product_2(example_expense_report, good_entries_fix_2):
    product = advent_expense.calculate_product(example_expense_report, 
            good_entries_2)
    assert product == 514579

def test_get_product_3(example_expense_report, good_entries_fix_3):
    product = advent_expense.calculate_product(example_expense_report, 
            good_entries_3)
    assert product == 241861950
