import re

file = open('input.txt')

lines = list(map(lambda x: x.rstrip('\n'), file.readlines()))

def first_validator(a, b, char, password):
    count = sum([1 if c == char else 0 for c in password])
    return a <= count <= b

def second_validator(a, b, char, password):
    a_char = password[a - 1]
    b_char = password[b - 1]
    return (a_char == char) != (b_char == char)

def validate_password(line, validator):
    match = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
    if not match:
        raise Exception(f"Unexpected string format: '{line}'")

    a, b = [int(match.group(i)) for i in [1, 2]]
    char, password = [match.group(i) for i in [3, 4]]

    return validator(a, b, char, password)

print(sum([validate_password(line, first_validator) for line in lines]))

print(sum([validate_password(line, second_validator) for line in lines]))