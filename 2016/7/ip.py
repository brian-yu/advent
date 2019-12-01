

def isABBA(s):
	return (len(s) == 4) and (s[2:] == s[:2][::-1]) and (s[0] != s[1])

def isABA(s):
	return (len(s) == 3) and (s[0] == s[2]) and (s[0] != s[1])

def hasABBA(s):
	if len(s) < 4:
		return False
	for i in range(len(s)):
		if isABBA(s[i:i+4]):
			return True
	return False

def findABA(s):
	ABAs = []
	for i in range(len(s)):
		if isABA(s[i:i+3]):
			ABAs.append(s[i:i+3])
	return ABAs

def isSSL(s):
	opens = [i for i in range(len(s)) if s[i] == "["]
	closing = [i for i in range(len(s)) if s[i] == "]"]
	if len(opens) != len(closing):
		return False


	inside = []
	outside = []
	last = 0
	for i in range(len(opens)):
		outside.append(s[last:opens[i]])
		inside.append(s[opens[i]+1:closing[i]])
		last = closing[i] + 1
	outside.append(s[last:])

	#print(outside)
	ABA = [j for i in [findABA(i) for i in outside] for j in i]
	print(ABA)
	BAB = [j for i in [findABA(i) for i in inside] for j in i]
	print(BAB)#{i[::-1] for i in ABA}

	print([i[1]+i[0]+i[1] in ABA for i in BAB])
	# print(inside)

	return True in [i[1]+i[0]+i[1] in ABA for i in BAB]


def isValid(s):
	opens = [i for i in range(len(s)) if s[i] == "["]
	closing = [i for i in range(len(s)) if s[i] == "]"]
	if len(opens) != len(closing):
		return False


	inside = []
	outside = []
	last = 0
	for i in range(len(opens)):
		outside.append(s[last:opens[i]])
		inside.append(s[opens[i]+1:closing[i]])
		last = closing[i] + 1
	outside.append(s[last:])

	return (True not in [hasABBA(i) for i in inside]) and (True in [hasABBA(i) for i in outside])

f = open("input.txt")

count = 0
SSL = 0
for line in f:
	count += isValid(line.strip())
	SSL += isSSL(line.strip())

print(count)
print(SSL)

print(isSSL("aba[bab]xyz")) #t
print(isSSL("xyx[xyx]xyx")) #f
print(isSSL("aaa[kek]eke")) #t
print(isSSL("zazbz[bzb]cdb")) #t
