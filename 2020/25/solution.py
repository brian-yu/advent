file = open('input.txt')
card_public_key, door_public_key = [
    int(line.rstrip('\n')) for line in file.readlines()
]

def apply_transform(value, subject):
    return (value * subject) % 20201227


def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = apply_transform(value, subject)
    return value


def find_loop_size(subject, public_key):
    loop_size = 0
    value = 1

    while value != public_key:
        value = apply_transform(value, subject)
        loop_size += 1
    
    return loop_size


card_loop_size = find_loop_size(7, card_public_key)
door_loop_size = find_loop_size(7, door_public_key)


print(transform(door_public_key, card_loop_size))
print(transform(card_public_key, door_loop_size))
