import re
import math
import time

file = open('input.txt')
lines = [line.rstrip('\n') for line in file.readlines()]

timestamp = int(lines[0])
buses = [int(bus) if bus != 'x' else bus for bus in lines[1].split(',')]
filtered_buses = filter(lambda bus: bus != 'x', buses)

def find_soonest_bus(timestamp, buses):
    soonest_bus = None
    min_time_difference = None
    for bus in buses:
        if timestamp % bus == 0:
            return bus, 0
        
        bus_arrival = math.ceil(timestamp / bus) * bus
        if bus_arrival - timestamp < (min_time_difference or float('inf')):
            soonest_bus = bus
            min_time_difference = bus_arrival - timestamp
    
    return soonest_bus, min_time_difference


soonest_bus, time_difference = find_soonest_bus(timestamp, filtered_buses)
print(soonest_bus * time_difference)

def validate_sequence(timestamp, buses):
    for i in range(1, len(buses)):
        bus = buses[i]

        if bus == 'x':
            continue
        if (timestamp + i) % bus != 0:
            return False
    
    return True

def debug(buses, limit=3):
    print(f"======")
    print(buses)
    timestamp = buses[0]
    solutions = []
    while len(solutions) < limit:
        if validate_sequence(timestamp, buses):
            solutions.append(timestamp)
            print(timestamp)
            for i, bus in enumerate(buses):
                if bus == 'x':
                    continue
                print(f"\t+ {i}) / {bus} = {(timestamp + i) / bus}")
        timestamp += buses[0]
    
    print(f"difference: {solutions[1] - solutions[0]}")

# debug([7], 3)
# debug([7, 13], 3)
# debug([7, 13, 'x', 'x'], 3)
# debug([7, 13, 'x', 'x', 59], 3)
# debug([7, 13, 'x', 'x', 59, 'x'], 3)
# debug([7, 13, 'x', 'x', 59, 'x', 31], 3)
# debug([7, 13, 'x', 'x', 59, 'x', 31, 19], 3)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def find_timestamp_for_sequence(buses):
    timestamp = buses[0]
    difference = buses[0]

    for i in range(1, len(buses) + 1):
        subarray = buses[:i]
        latest_bus = subarray[-1]

        if latest_bus == 'x':
            continue
        
        while not validate_sequence(timestamp, subarray):
            timestamp += difference
        
        difference = lcm(difference, latest_bus)

    return timestamp

print(find_timestamp_for_sequence(buses))