from functools import reduce

# def decode(code):
# 	i = 0
# 	s = ""
# 	while i < len(code):
# 		char = code[i]
# 		if char == "(":
# 			i += 1
# 			comp = ""
# 			while code[i] != ")":
# 				comp += code[i]
# 				i += 1
# 			i += 1 
# 			num, rep = [int(n) for n in comp.split("x")]
# 			#print(code[i:i+num] * rep)
# 			s += decode(code[i:i+num] * rep)
# 			i += num
# 		else:
# 			s += char
# 			i += 1
# 	return s

def findSegments(code):
	while i < len(code):
		char = code[i]
		if char == "(":
			start = i
			i += 1
			comp = ""
			while code[i] != ")":
				comp += code[i]
				i += 1
			i += 1 
			num, rep = [int(n) for n in comp.split("x")]
			segments.append(code[start:i+num])
			i += num
	return segments

def numLetters(s):
	return sum(1 for i in s if ord(i) >= 65 and ord(i) <=90)

def findSegments(code):
	segments = []
	lone = []
	i = 0
	while i < len(code):
		char = code[i]
		if char == "(":
			start = i
			i += 1
			comp = ""
			while code[i] != ")":
				comp += code[i]
				i += 1
			i += 1 
			num, rep = [int(n) for n in comp.split("x")]
			segments.append(code[start:i+num])
			i += num
		else:
			lone.append(char)
			i += 1
	return segments, lone

def extractNums(segment):
	arr = segment[segment.index("(")+1:segment.index(")")].split("x")
	return int(arr[0]), int(arr[1])

def decode(s):
	segments, lone = findSegments(s)

	if len(segments) == 0:
		return 1

	total = 0

	for segment in segments:
		length, reps = extractNums(segment)
		if segment.count("(") == 1:
			total += length * reps
		else:
			total += reps * decode(segment[segment.find(")")+1:])

	return total + len(lone)


f = open("input.txt")

for line in f:
	s = line.strip()



print(decode(s))