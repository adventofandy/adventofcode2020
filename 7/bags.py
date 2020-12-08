import sys
import re

def parse_bag_line(bag_line):
    def parse_inside_bags(in_str):
        if in_str == "no other bags":
            return []

        inside_bag_strs = in_str.split(', ')
        print(f'Inside strs: {inside_bag_strs}')
        regex = re.compile(
            r'^(?P<num>\d*) (?P<bag_name>.*) bags?$')
        inside_bag_matches = [regex.search(f).groupdict() 
                for f in inside_bag_strs]
        inside_bags_lists = [[d['bag_name']]*int(d['num']) 
                for d in inside_bag_matches] 
        inside_bags = [j for i in inside_bags_lists for j in i]
        print(f'Inside: {inside_bags}')
        return inside_bags

    regex = re.compile(
            r'^(?P<this_bag>.*) bags contain (?P<inside_bags>.*).$')
    match = regex.search(bag_line)
    match_dict = match.groupdict()
    print(match_dict['this_bag'])
    print(match_dict['inside_bags'])

    this_bag = match_dict['this_bag']
    inside_bags = parse_inside_bags(match_dict['inside_bags'])
    return {this_bag: inside_bags}

def find_parent_bags(bag_dict, bag):
    parent_bags = [t[0] for t in bag_dict.items() if bag in t[1]]
    pp_bags = [find_parent_bags

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read()
        lines = data.rstrip('\n').split('\n')

    bag_dicts = [parse_bag_line(l) for l in lines]
    merged_dict = dict(pair for d in bag_dicts for pair in d.items())
    print(merged_dict)

    bag_search = sys.argv[2]

