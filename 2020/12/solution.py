import re

file = open('input.txt')
lines = [line.rstrip('\n') for line in file]

def parse_line(line):
    match = re.match(r'([NEWSLRF]+)(\d+)', line)
    if not match:
        raise Exception('Invalid input line')

    return match.group(1), int(match.group(2))

def turn(direction, left_or_right, degrees):
    directions = {
        'N': 0,
        'E': 1,
        'S': 2,
        'W': 3,
    }
    order = ['N', 'E', 'S', 'W']

    if left_or_right == 'L':
        offset = -1 * (degrees // 90)
    elif left_or_right == 'R':
        offset = 1 * (degrees // 90)
    else:
        raise Exception('Invalid turn')

    return order[(directions[direction] + offset) % len(order)]

def move(r, c, direction, value):
    directions = {
        'E': (0, 1),
        'W': (0, -1),
        'N': (-1, 0),
        'S': (1, 0),
    }

    r_offset, c_offset = directions[direction]
    r += value * r_offset
    c += value * c_offset
    
    return r, c

def part_one(lines):
    r, c = 0, 0
    direction = 'E'

    for line in lines:
        action, value = parse_line(line)

        if action in {'N', 'E', 'W', 'S'}:
            r, c = move(r, c, action, value)
        elif action == 'L' or action == 'R':
            direction = turn(direction, action, value)
        elif action == 'F':
            r, c = move(r, c, direction, value)

    print(abs(r) + abs(c))
            
part_one(lines)

def rotate(r, c, left_or_right, degrees):
    turns = degrees // 90

    for _ in range(turns):
        if left_or_right == 'L':
            r, c = -c, r
        elif left_or_right == 'R':
            r, c = c, -r
        else:
            raise Exception('Invalid turn')
    
    return r, c


def part_two(lines):
    ship_r, ship_c = 0, 0
    waypoint_r, waypoint_c = -1, 10

    for line in lines:
        action, value = parse_line(line)

        if action in {'N', 'E', 'W', 'S'}:
            waypoint_r, waypoint_c = move(waypoint_r, waypoint_c, action, value)
        elif action == 'L' or action == 'R':
            waypoint_r, waypoint_c = rotate(waypoint_r, waypoint_c, action, value)
        elif action == 'F':
            ship_r += value * waypoint_r
            ship_c += value * waypoint_c

    print(abs(ship_r) + abs(ship_c))

part_two(lines)

