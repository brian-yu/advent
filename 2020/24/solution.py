from enum import Enum


class Direction(Enum):
    E = "e"
    SE = "se"
    SW = "sw"
    W = "w"
    NW = "nw"
    NE = "ne"


class Color(Enum):
    Black = 0
    White = 1


COMPLEMENTARY_COLORS = {
    Color.Black: Color.White,
    Color.White: Color.Black,
}


DIRECTIONS = {direction.value for direction in Direction}


COMPLEMENTARY_DIRECTIONS = {
    Direction.E: Direction.W,
    Direction.SE : Direction.NW,
    Direction.SW : Direction.NE,
    Direction.W: Direction.E,
    Direction.NW : Direction.SE,
    Direction.NE : Direction.SW,
}


def parse_moves(s):
    moves = []
    start = 0
    for end in range(1, len(s)):
        move = s[start:end]
        if move in DIRECTIONS:
            moves.append(Direction(move))
            start = end
    moves.append(Direction(s[start:]))

    return moves


class HexCursor:
    def __init__(self, tiling, r, c):
        self.tiling = tiling
        self.r = r
        self.c = c

        self._validate_position()
    
    def _validate_position(self):
        if (
            (not (0 <= self.r < len(self.tiling.grid))) or
            (not (0 <= self.c < len(self.tiling.grid)))
        ):
            raise Exception(f'Cursor out of grid bounds: r={self.r}, c={self.c}')
    
    def _apply_direction(self, direction):
        r = self.r
        c = self.c

        even_column = c % 2 == 0
        
        if direction == Direction.E:
            r -= 1
        elif direction == Direction.SE:
            c += 1
            if even_column:
                r -= 1
        elif direction == Direction.SW:
            c += 1
            if not even_column:
                r += 1
        elif direction == Direction.W:
            r += 1
        elif direction == Direction.NW:
            c -= 1
            if not even_column:
                r += 1
        elif direction == Direction.NE:
            c -= 1
            if even_column:
                r -= 1
        else:
            raise Exception(f'Invalid direction: {direction}')
        
        return r, c
    
    def move(self, direction):
        self.r, self.c = self._apply_direction(direction)
        self._validate_position()

    def flip(self):
        self.tiling._flip(self.r, self.c)
    
    def color(self):
        return self.tiling.grid[self.r][self.c]
    
    def count_neighboring_colored_tiles(self, color):
        count = 0
        for neighbor in self.neighbor_cursors():
            if neighbor.color() == color:
                count += 1
        return count
    
    def neighbor_cursors(self):
        cursors = []
        for direction in Direction:
            nr, nc = self._apply_direction(direction)
            neighbor = HexCursor(self.tiling, nr, nc)
            cursors.append(neighbor)
        return cursors
    
    def __eq__(self, other):
        return (
            self.r == other.r and
            self.c == other.c and
            self.tiling == other.tiling
        )

    def __hash__(self):
        return hash(f"{self.r}|{self.c}|{hash(self.tiling)}")
    
    def __repr__(self):
        return f"Cursor({self.r}, {self.c}, {self.color().name})"

class HexTiling:
    def __init__(self, radius, grid=None):
        self.radius = radius
        self.diameter = 2 * self.radius
        self.grid = (
            grid or
            [[Color.White for i in range(self.diameter)] for j in range(self.diameter)]
        )

        self.cursors_to_flip = set()

        self.colored_tiles = {color: set() for color in Color}
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.colored_tiles[Color.White].add((r, c))
    
    def center_cursor(self):
        return HexCursor(self, self.radius, self.radius)
    
    def count_colored_tiles(self, color):
        return len(self.colored_tiles[color])
    
    def cursors_for_colored_tiles(self, color):
        cursors = []
        for r, c in self.colored_tiles[color]:
            cursors.append(HexCursor(self, r, c))
        return cursors
        
    def queue_cursor_to_flip(self, cursor):
        self.cursors_to_flip.add(cursor)
    
    def _flip(self, r, c):
        curr_color = self.grid[r][c]
        next_color = COMPLEMENTARY_COLORS[self.grid[r][c]]
        self.grid[r][c] = next_color
        self.colored_tiles[curr_color].remove((r, c))
        self.colored_tiles[next_color].add((r, c))
    
    def flip_queued_cursors(self):
        for cursor in self.cursors_to_flip:
            cursor.flip()
        self.cursors_to_flip = set()


with open('input.txt') as file:
    moves_list = [parse_moves(line.rstrip('\n')) for line in file.readlines()]

radius = max(len(moves) for moves in moves_list)
tiling = HexTiling(radius * 5)

for moves in moves_list:
    cursor = tiling.center_cursor()
    for direction in moves:
        cursor.move(direction)
    cursor.flip()

print(tiling.count_colored_tiles(Color.Black))

def process(tiling, n):

    black_cursors = set(tiling.cursors_for_colored_tiles(Color.Black))

    for day in range(n):
        neighbors = set()
        for cursor in black_cursors:
            neighbors |= set(cursor.neighbor_cursors())
        
        next_black_cursors = set()
        for cursor in black_cursors | neighbors:
            num_black_neighbors = cursor.count_neighboring_colored_tiles(Color.Black) 

            if cursor.color() == Color.Black:
                if num_black_neighbors == 0 or num_black_neighbors > 2:
                    tiling.queue_cursor_to_flip(cursor)
                else:
                    next_black_cursors.add(cursor)
            elif cursor.color() == Color.White:
                if num_black_neighbors == 2:
                    tiling.queue_cursor_to_flip(cursor)
                    next_black_cursors.add(cursor)

        tiling.flip_queued_cursors()
        black_cursors = next_black_cursors

        print(f"Day {day + 1}: {tiling.count_colored_tiles(Color.Black)}")

        

process(tiling, 100)
print(tiling.count_colored_tiles(Color.Black))
