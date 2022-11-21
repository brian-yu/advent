

class Body:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.satellites = []

    def __repr__(self):
        return self.name

class Universe:
    def __init__(self, bodies):
        self.bodies = bodies
        self.root = bodies['COM']

    def get(self, name):
        return self.bodies[name]


def build_tree(orbits):

    bodies = {}

    for orbit in orbits:
        body_name, satellite_name = orbit.split(")")
        body = bodies.get(body_name, Body(body_name))
        satellite = bodies.get(satellite_name, Body(satellite_name))

        body.satellites.append(satellite)
        satellite.parent = body

        bodies[body_name] = body
        bodies[satellite_name] = satellite

    return Universe(bodies)


def count_orbits(body, depth=0):

    orbits = 0

    for satellite in body.satellites:
        orbits += count_orbits(satellite, depth + 1)

    return orbits + depth

def lowest_common_ancestor(root, a, b):
    a_itr = a
    ancestors = set()
    while a_itr != None:
        ancestors.add(a_itr)
        a_itr = a_itr.parent

    while b != None:
        if b in ancestors:
            return b
        b = b.parent

    return None

def distance(node, ancestor):
    dist = 0
    while node != ancestor:
        dist += 1
        node = node.parent
    return dist

    



lines = [line.rstrip('\n') for line in open('input.txt', 'r').readlines()]

universe = build_tree(lines)
print(count_orbits(universe.root))
lca = lowest_common_ancestor(universe.root, universe.get('YOU'), universe.get('SAN'))
print(lca)
traversals = distance(universe.get('YOU'), lca) + distance(universe.get('SAN'), lca) - 2
print(traversals)


def traverse(body):
    print(body.name)
    print(body.satellites)
    for satellite in body.satellites:
        traverse(satellite)
