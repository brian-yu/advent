import re
from copy import deepcopy
from collections import defaultdict
import math

file = open('input.txt')
tile_inputs = [tile.split('\n') for tile in file.read()[:-2].split('\n\n')]

class Tile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile
    
    def flip(self):
        return Tile(self.id, list(reversed(self.tile)))
    
    def rotate(self):
        num_rows = len(self.tile)
        num_cols = len(self.tile[0])
        return Tile(
            self.id,
            [[self.tile[num_cols - c - 1][r] for c in range(num_cols)] for r in range(num_rows)]
        )
    
    def top(self):
        return "".join(self.tile[0])
    
    def right(self):
        return "".join([self.tile[i][-1] for i in range(len(self.tile[0]))])
    
    def bottom(self):
        return "".join(self.tile[-1])
    
    def left(self):
        return "".join([self.tile[i][0] for i in range(len(self.tile[0]))])
    
    def sides(self):
        return [self.top(), self.right(), self.bottom(), self.left()]
    
    def variations(self):
        variations = []
        normal = self
        flipped = self.flip()
        for _ in range(4):
            normal = normal.rotate()
            flipped = flipped.rotate()
            variations.extend([normal, flipped])
        return variations
    
    def __repr__(self):
        return str(self.id)
    
    def __eq__(self, other):
        return isinstance(other, Tile) and self.tile == other.tile
    
    def __hash__(self):
        return hash(str(self.id) + "".join(self.sides()))
    
    def __getitem__(self, key):
        return self.tile[key]
    
    def __len__(self):
        return len(self.tile)

tiles = []
for tile in tile_inputs:
    match = re.match(r'Tile (\d+):', tile[0])
    id = int(match.group(1))
    tiles.append(Tile(id, tile[1:]))


def get_tile_side_map(tiles):
    tile_sides = {
        'top': defaultdict(set),
        'bottom': defaultdict(set),
        'left': defaultdict(set),
        'right': defaultdict(set),
    }
    for tile in tiles:
        for variation in tile.variations():
            tile_sides['top'][variation.top()].add(variation)
            tile_sides['bottom'][variation.bottom()].add(variation)
            tile_sides['left'][variation.left()].add(variation)
            tile_sides['right'][variation.right()].add(variation)
    return tile_sides

def get_possible_tiles(tile_sides, tile_positions, r, c):
    top, bottom, left, right = None, None, None, None
    if r - 1 >= 0:
        top = tile_positions[r - 1][c]
    if r + 1 < len(tile_positions):
        bottom = tile_positions[r + 1][c]
    if c - 1 >= 0:
        left = tile_positions[r][c - 1]
    if c + 1 < len(tile_positions[r]):
        right = tile_positions[r][c + 1]
    
    possible_sets = []
    if top:
        possible_sets.append(tile_sides['top'][top.bottom()])
    if bottom:
        possible_sets.append(tile_sides['bottom'][bottom.top()])
    if left:
        possible_sets.append(tile_sides['left'][left.right()])
    if right:
        possible_sets.append(tile_sides['right'][right.left()])
    
    possible = set(possible_sets[0])
    for possible_set in possible_sets[1:]:
        possible &= possible_set
    
    return possible

def get_next_position(tile_positions, r, c):
    if c == len(tile_positions[r]) - 1:
        return r + 1, 0
    return r, c + 1

def get_corners(tiles, tile_sides):
    corners = set()
    for tile in tiles:
        adjacent_tiles = (
            tile_sides['bottom'][tile.top()] |
            tile_sides['right'][tile.left()] |
            tile_sides['left'][tile.right()] |
            tile_sides['top'][tile.bottom()]
        )
        if len({tile.id for tile in adjacent_tiles} - {tile.id}) == 2:
            corners.add(tile)
    return corners

def display_tiles(tile_positions):
    for row in tile_positions:
        rows = []
        if not row[0]:
            continue
        for _ in range(len(row[0])):
            rows.append([])
        for tile in row:
            if not tile:
                continue
            for tr, tile_row in enumerate(tile):
                rows[tr].extend(tile_row + [' '])
        
        print("\n".join(["".join(row) for row in rows]))
        print()

def match_tiles_helper(tile_sides, tile_positions, used_tile_ids, r, c):
    if r >= len(tile_positions):
        return tile_positions

    possible_tiles = list(filter(
        lambda tile: tile.id not in used_tile_ids,
        get_possible_tiles(tile_sides, tile_positions, r, c)
    ))

    for tile in possible_tiles:
        next_r, next_c = get_next_position(tile_positions, r, c)
        tile_positions[r][c] = tile
        maybe_result = match_tiles_helper(tile_sides, tile_positions, used_tile_ids | {tile.id}, next_r, next_c)
        if maybe_result:
            return maybe_result
    
    tile_positions[r][c] = None
    
    return None

def match_tiles(tiles):
    n = int(math.sqrt(len(tiles)))
    
    tile_sides = get_tile_side_map(tiles)
    tile_positions = [[None for col in range(n)] for row in range(n)]

    for corner in get_corners(tiles, tile_sides):
        for variation in corner.variations():

            tile_positions[0][0] = variation

            maybe_result = match_tiles_helper(tile_sides, tile_positions, {variation.id}, 0, 1)
            if maybe_result:
                return maybe_result
    
    return None

tile_grid = match_tiles(tiles)
display_tiles(tile_grid)
print(
    tile_grid[0][0].id *
    tile_grid[0][-1].id *
    tile_grid[-1][0].id *
    tile_grid[-1][-1].id
)

def remove_borders(tile_grid):
    n = len(tile_grid) * (len(tile_grid[0][0]) - 2)
    rows = [[] for _ in range(n)]
    for r, row_of_tiles in enumerate(tile_grid):
        for tile in row_of_tiles:
            for tile_r, tile_row in enumerate(tile[1:-1]):
                rows[r * len(tile_row[1:-1]) + tile_r].extend(tile_row[1:-1])
    
    return rows

image = remove_borders(tile_grid)

SEA_MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')

print("\n".join(SEA_MONSTER) + '\n')

image_tile = Tile(0, image)

def section_contains_sea_monster(tile, r, c):
    if r + len(SEA_MONSTER) >= len(tile):
        return False
    if c + len(SEA_MONSTER[0]) >= len(tile[r]):
        return False
    
    for nr in range(r, r + len(SEA_MONSTER)):
        for nc in range(c, c + len(SEA_MONSTER[0])):
            if SEA_MONSTER[nr - r][nc - c] == '#' and tile[nr][nc] != '#':
                return False
    return True

def mark_sea_monster(tile, r, c):
    if not section_contains_sea_monster(tile, r, c):
        return False
    
    for nr in range(r, r + len(SEA_MONSTER)):
        for nc in range(c, c + len(SEA_MONSTER[0])):
            if SEA_MONSTER[nr - r][nc - c] == '#':
                tile[nr][nc] = 'O'
    
    return True

def mark_all_sea_monsters(tile):
    marked = False
    for r in range(len(tile)):
        for c in range(len(tile[0])):
            marked |= mark_sea_monster(tile, r, c)
    return marked

for variation in image_tile.variations():
    if mark_all_sea_monsters(variation):
        print("\n".join("".join(row) for row in variation))

        count = 0
        for r, row in enumerate(variation):
            for c in range(len(variation[r])):
                if variation[r][c] == '#':
                    count += 1
        print(count)

