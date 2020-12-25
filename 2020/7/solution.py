import re

file = open('input.txt')

rules = [line.rstrip('.\n') for line in file.readlines()]

bags = {}

for rule in rules:
    outer, inner = rule.split(' contain ')

    outer_color = re.match(r'([a-z ]+) bags?', outer).group(1)
    
    inner_bags = {}

    for inner_bag in inner.split(', '):
        if inner_bag == 'no other bags':
            continue
        match = re.match(r'(\d+) ([a-z ]+) bags?', inner_bag)
        quantity = int(match.group(1))
        color = match.group(2)
        
        inner_bags[color] = quantity
    
    bags[outer_color] = inner_bags


def contains_target_bag(bags, color, target):
    result = False
    for inner_bag_color in bags[color]:
        if inner_bag_color == target:
            return True
        result |= contains_target_bag(bags, inner_bag_color, target)
    
    return result

def sum_of_inner_bags(bags, color):
    count = 0
    for inner_bag_color, quantity in bags[color].items():
        count += quantity * (1 + sum_of_inner_bags(bags, inner_bag_color))

    return count

print(sum(contains_target_bag(bags, color, 'shiny gold') for color in bags))

print(sum_of_inner_bags(bags, 'shiny gold'))
