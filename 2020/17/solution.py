import copy

file = open('input.txt')
starting_state = [list(line.rstrip('\n')) for line in file.readlines()]

class Space:
    def __init__(self, dimensions, starting_state):
        self.dimensions = dimensions
        self.active_cubes = set()
        self.space = {}
        self.neighbor_offsets = self.get_neighbor_offsets()

        for x, row in enumerate(starting_state):
            for y, state in enumerate(row):
                if state == '#':
                    point = [x, y]
                    for _ in range(self.dimensions - 2):
                        point.append(0)
                    self.set_cube_state(tuple(point), state)
    
    def _get_nth_dimension(self, point, n, create_missing_dimensions=False):
        dimension = self.space
        for coord in point[:n]:
            if coord not in dimension:
                if create_missing_dimensions:
                    dimension[coord] = {}
                else:
                    return '.'
            dimension = dimension[coord]
        return dimension

    def set_cube_state(self, point, state):
        if len(point) != self.dimensions:
            raise Exception('invalid point')
        if state != '.' and state != '#':
            raise Exception(f'invalid state: {state}')

        if state == '#':
            last_dimension = self._get_nth_dimension(
                point,
                self.dimensions - 1,
                create_missing_dimensions=True
            )
            last_dimension[point[-1]] = state
            self.active_cubes.add(point)
        
        elif state == '.':
            if point in self.active_cubes:
                self.active_cubes.remove(point)

            dimensions = []
            dimension = self.space
            for coord in point[:-1]:
                dimensions.append(dimension[coord])
                dimension = dimension[coord]
            
            dimensions[-1].pop(point[-1])

            for i in reversed(range(1, self.dimensions - 1)):
                dimension = dimensions[i]
                coord = point[i]
                if coord in dimension and len(dimension[coord]) == 0:
                    dimension.pop(coord)
    
    def get_cube_state(self, point):
        if len(point) != self.dimensions:
            raise Exception('invalid point')

        return self._get_nth_dimension(point, self.dimensions)
    
    def get_neighbors(self, point):
        if len(point) != self.dimensions:
            raise Exception('invalid point')
        
        neighbors = set()

        for offset_arr in self.neighbor_offsets:
            neighbor = tuple(
                point[i] - offset for i, offset in enumerate(offset_arr)
            )
            neighbors.add(neighbor)

        return neighbors
    
    def count_active_neighbors(self, point):
        if len(point) != self.dimensions:
            raise Exception('invalid point')

        neighbors = self.get_neighbors(point)
        return len(neighbors & self.active_cubes)
    
    def get_neighbor_offsets(self):
        def helper(dimension):
            if dimension == 0:
                return [[]]
            offsets = []
            for offset_arr in helper(dimension - 1):
                for offset in [-1, 0, 1]:
                    offsets.append(offset_arr + [offset])
            return offsets
    
        return list(filter(
            lambda x: x != [0 for _ in range(self.dimensions)],
            helper(self.dimensions)
        ))

def run_cycles(space, num_cycles):
    for _ in range(num_cycles):
        next_space = copy.deepcopy(space)
        points = set(space.active_cubes)
        for point in space.active_cubes:
            points |= space.get_neighbors(point)
        
        for point in points:
            state = space.get_cube_state(point)
            active_neighbors = space.count_active_neighbors(point)

            if state == '#':
                if active_neighbors != 2 and active_neighbors != 3:
                    next_space.set_cube_state(point, '.')
            elif state == '.':
                if active_neighbors == 3:
                    next_space.set_cube_state(point, '#')

        space = next_space
    
    return space

space = Space(3, starting_state)
print(len(run_cycles(space, 6).active_cubes))

space = Space(4, starting_state)
print(len(run_cycles(space, 6).active_cubes))
