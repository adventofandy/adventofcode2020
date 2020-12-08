import pytest

@pytest.fixture
def test_bag_lines():
    with open("test_bags.txt") as f:
        data = f.read()
        lines = data.rstrip('\n').split('\n')

@pytest.mark.parametrize("
def test_parse_bag_line(test_bag_lines):

