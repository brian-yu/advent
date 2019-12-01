

def get_fuel(mass):
    return mass // 3 - 2

def recursive_get_fuel(mass):
    total_fuel = 0
    fuel = get_fuel(mass)
    while fuel > 0:
        total_fuel += fuel
        fuel = get_fuel(fuel)
    return total_fuel

lines = [line.rstrip('\n') for line in open('input.txt').readlines()]
masses = [int(line) for line in lines]


print(sum(map(get_fuel, masses)))
print(sum(map(recursive_get_fuel, masses)))
