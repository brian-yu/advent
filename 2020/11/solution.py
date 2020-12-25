file = open('input.txt')
grid = [list(line.rstrip('\n')) for line in file.readlines()]

NEIGHBOR_OFFSETS = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

def count_occupied_neighbors(grid, r, c):
    count = 0

    for r_offset, c_offset in NEIGHBOR_OFFSETS:
        nr = r + r_offset
        nc = c + c_offset

        if nr < 0 or nr >= len(grid):
            continue
        if nc < 0 or nc >= len(grid[0]):
            continue

        if grid[nr][nc] == '#':
            count += 1
    
    return count

def get_next_state(grid):
    next_grid = [[grid[r][c] for c in range(len(grid[0]))] for r in range(len(grid))]

    changed = False

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            occupied_neighbors = count_occupied_neighbors(grid, r, c)

            if grid[r][c] == 'L' and occupied_neighbors == 0:
                next_grid[r][c] = '#'
                changed = True
            elif grid[r][c] == '#' and occupied_neighbors >= 4:
                next_grid[r][c] = 'L'
                changed = True
    
    return next_grid, changed

def count_occupied_seats_at_equilibrium(grid, state_fn):
    changed = True
    while changed:
        grid, changed = state_fn(grid)
    
    count_occupied = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                count_occupied += 1
    
    return count_occupied

print(count_occupied_seats_at_equilibrium(grid, get_next_state))

def count_occupied_visible_seats(grid, r, c):
    count = 0
    for r_offset, c_offset in NEIGHBOR_OFFSETS:
        nr = r + r_offset
        nc = c + c_offset

        while nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
            if grid[nr][nc] == '#':
                count += 1
                break
            elif grid[nr][nc] == 'L':
                break
            nr += r_offset
            nc += c_offset
    
    return count

def display(grid):
    for row in grid:
        print("".join(row))
    print()

def get_next_state_v2(grid):
    next_grid = [[grid[r][c] for c in range(len(grid[0]))] for r in range(len(grid))]

    changed = False

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            occupied_visible = count_occupied_visible_seats(grid, r, c)

            if grid[r][c] == 'L' and occupied_visible == 0:
                next_grid[r][c] = '#'
                changed = True
            elif grid[r][c] == '#' and occupied_visible >= 5:
                next_grid[r][c] = 'L'
                changed = True
    
    return next_grid, changed

print(count_occupied_seats_at_equilibrium(grid, get_next_state_v2))