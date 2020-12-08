import pytest
import bags

@pytest.fixture
def test_bag_lines():
    with open("test_bags.txt") as f:
        data = f.read()
        lines = data.rstrip('\n').split('\n')
        assert lines
        return lines

test_line_data = [
        (0, {'light red': ['bright white'] + ['muted yellow']*2}),
        (1, {'dark orange': ['bright white']*3 + ['muted yellow']*4}),
        (2, {'bright white': ['shiny gold']}),
        (3, {'muted yellow': ['shiny gold']*2 + ['faded blue']*9}),
        (4, {'shiny gold': ['dark olive'] + ['vibrant plum']*2}),
        (5, {'dark olive': ['faded blue']*3 + ['dotted black']*4}),
        (6, {'vibrant plum': ['faded blue']*5 + ['dotted black']*6}),
        (7, {'faded blue': []}),
        (8, {'dotted black': []})]

@pytest.mark.parametrize("line_no, exp", test_line_data)
def test_parse_bag_line(test_bag_lines, line_no, exp):
    line = test_bag_lines[line_no]
    parsed_line = bags.parse_bag_line(line)
    assert parsed_line == exp

