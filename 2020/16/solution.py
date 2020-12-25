import re

file = open('input.txt')
chunks = [chunk.split('\n') for chunk in file.read().split('\n\n')]

class Field:
    def __init__(self, s):
        match = re.match(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', s)
        self.name = match.group(1)
        self.first_range_min = int(match.group(2))
        self.first_range_max = int(match.group(3))
        self.second_range_min = int(match.group(4))
        self.second_range_max = int(match.group(5))
    
    def validate(self, value):
        return (
            self.first_range_min <= value <= self.first_range_max or
            self.second_range_min <= value <= self.second_range_max
        )
    
    def validate_batch(self, values):
        return all(self.validate(value) for value in values)
    
    def mark_valid_values(self, valid_values):
        max_value = max(self.first_range_max, self.second_range_max) 
        if max_value >= len(valid_values):
            valid_values.extend(
                [False] * (max_value - len(valid_values) + 1)
            )
        for i in range(self.first_range_min, self.first_range_max + 1):
            valid_values[i] = True
        for i in range(self.second_range_min, self.second_range_max + 1):
            valid_values[i] = True
    
    def __hash__(self):
        return hash(self.name)
    
    def __repr__(self):
        return self.name

fields = [Field(line) for line in chunks[0]]
my_ticket = [int(field) for field in chunks[1][1:][0].split(',')]
other_tickets = [[int(field) for field in  ticket.split(',')] for ticket in chunks[2][1:-1]]


def get_valid_field_values(fields):
    valid_field_values = []

    for field in fields:
        field.mark_valid_values(valid_field_values)
    
    return valid_field_values

def get_invalid_field_values(valid_field_values, ticket):
    invalid_field_values = []
    for field_value in ticket:
        if field_value >= len(valid_field_values) or not valid_field_values[field_value]:
            invalid_field_values.append(field_value)
    
    return invalid_field_values

def get_ticket_scanning_error(fields, tickets):
    valid_field_values = get_valid_field_values(fields)

    invalid_field_values = []

    for ticket in tickets:
        invalid_field_values.extend(
            get_invalid_field_values(valid_field_values, ticket)
        )
        
    return sum(invalid_field_values)

print(get_ticket_scanning_error(fields, other_tickets))

def get_valid_tickets(fields, tickets):
    valid_field_values = get_valid_field_values(fields)

    valid_tickets = []
    for ticket in tickets:
        if len(get_invalid_field_values(valid_field_values, ticket)) == 0:
            valid_tickets.append(ticket)
    
    return valid_tickets

def prune_possibilities(fields, position_to_field_map):
    pruned = False

    for field in fields:
        possible_count = 0
        possible_position = None

        for field_idx, possible_fields in position_to_field_map.items():
            if field in possible_fields:
                possible_position = field_idx
                possible_count += 1

        already_pruned = len(position_to_field_map[possible_position]) == 1
        if possible_count == 1 and not already_pruned:
            position_to_field_map[possible_position] = set([field])
            pruned = True
    
    return pruned

def get_field_positions(fields, tickets):
    valid_tickets = get_valid_tickets(fields, tickets)
    
    position_to_field_map = {}
    for field_idx in range(len(tickets[0])):
        position_to_field_map[field_idx] = set(fields)
        for field in fields:
            field_values = [ticket[field_idx] for ticket in valid_tickets]
            if not field.validate_batch(field_values):
                position_to_field_map[field_idx].remove(field)
    
    while prune_possibilities(fields, position_to_field_map):
        pass
    
    field_to_position_map = {}
    for position, fields in position_to_field_map.items():
        if len(fields) > 1:
            raise Exception('multiple possible fields for position')
        field_to_position_map[fields.pop()] = position
    
    return field_to_position_map

field_to_position_map = get_field_positions(fields, other_tickets + [my_ticket])

accumulated_product = 1
for field, field_idx in field_to_position_map.items():
    if field.name.startswith('departure'):
        accumulated_product *= my_ticket[field_idx]
print(accumulated_product)