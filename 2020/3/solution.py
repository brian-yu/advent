file = open('input.txt')

grid = [list(line.rstrip('\n')) for line in file.readlines()]

def count_chars(grid, right, down, target="#"):
    row = 0
    col = 0

    height = len(grid)
    width = len(grid[0])

    count = 0

    while row < height:
        row += down
        col = (col + right) % width

        if row >= height:
            break

        if grid[row][col] == target:
            count += 1
    
    return count

print(count_chars(grid, 3, 1))

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

result = 1

for right, down in slopes:
    result *= count_chars(grid, right, down)

print(result)
