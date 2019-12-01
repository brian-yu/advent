
polymer = open('input.txt').read().rstrip()

def removeIfPossible(s):
    ans = []
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i+1].lower() == s[i].lower() and s[i+1] != s[i]:
            i += 2
        else:
            ans.append(s[i])
            i += 1
    return "".join(ans)


def react(s):
    i = removeIfPossible(s)
    while i != s:
        s = i
        i = removeIfPossible(i)

    return i

# ans = react(polymer)
# print(len(ans))

def removeUnit(s, u):
    return s.replace(u, "").replace(u.upper(), "")

def findShortest(s):
    minLength = len(s)
    for unit in set(s.lower()):
        removed = removeUnit(s, unit)
        reacted = react(removed)
        if len(reacted) < minLength:
            minLength = len(reacted)
        print(unit, minLength)
    return minLength

print(findShortest("dabAcCaCBAcCcaDA"))
print(findShortest(polymer))
