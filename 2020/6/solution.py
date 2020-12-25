file = open('input.txt')

groups = [line.split('\n') for line in file.read()[:-1].split('\n\n')]

count = 0

for group in groups:
    questions = set()
    for person in group:
        questions.update(person)
    count += len(questions)

print(count)

count = 0

for group in groups:
    questions = set(group[0])
    for person in group[1:]:
        questions &= set(person)
    count += len(questions)

    print(group)
    print(questions)

print(count)