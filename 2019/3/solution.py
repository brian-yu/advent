
def extract_segments(path):
    x, y = 0, 0
    steps = 0

    segments = []
    for instruction in path:
        direction, length = instruction[0], int(instruction[1:])
        if direction == 'U':
            new_x, new_y = x, y + length
        elif direction == 'D':
            new_x, new_y = x, y - length
        elif direction == 'L':
            new_x, new_y = x - length, y
        elif direction == 'R':
            new_x, new_y = x + length, y
        segments.append(((x,y), (new_x, new_y), steps))
        x, y = new_x, new_y

        steps += length

    return segments



def find_intersection_points(segment1, segment2):
    s1x1, s1y1 = segment1[0]
    s1x2, s1y2 = segment1[1]
    s2x1, s2y1 = segment2[0]
    s2x2, s2y2 = segment2[1]

    prev_length_1 = segment1[2]
    prev_length_2 = segment2[2]

    if segment1[0] == (0, 0) or segment2[0] == (0, 0):
        return []

    points = []

    if min(s1x1, s1x2) <= s2x1 <= max(s1x1, s1x2) and min(s2y1, s2y2) <= s1y1 <= max(s2y1, s2y2):
        for x in range(s2x1, s2x2 + 1):
            length_1 = prev_length_1 + abs(x - s1x1)
            length_2 = prev_length_2 + abs(s1y1 - s2y1)
            points.append((x, s1y1, length_1 + length_2))

    if min(s1y1, s1y2) <= s2y1 <= max(s1y1, s1y2) and min(s2x1, s2x2) <= s1x1 <= max(s2x1, s2x2):
        for y in range(s2y1, s2y2 + 1):
            length_1 = prev_length_1 + abs(s1x1 - s2x1)
            length_2 = prev_length_2 + abs(y - s1y1)
            points.append((s1x1, y, length_1 + length_2))

    if len(points) > 1:
        print(points)
    return points

def find_intersections(segments1, segments2):
    intersections = []
    for a in segments1:
        for b in segments2:
            points = find_intersection_points(a, b)
            intersections.extend(points)

    return intersections

def dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

def find_closest_point(intersections):
    min_dist = float('inf')
    for point in intersections:
        min_dist = min(min_dist, dist((0, 0), point))
    print(min_dist)

def find_point_min_steps(intersections):
    min_steps = float('inf')
    for point in intersections:
        min_steps = min(min_steps, point[2])
    print(min_steps)





input_arr = [line.rstrip('\n').split(',') for line in open('input.txt').readlines()]

segments1 = extract_segments(input_arr[0])
segments2 = extract_segments(input_arr[1])

intersections = find_intersections(segments1, segments2)

find_closest_point(intersections)
find_point_min_steps(intersections)




