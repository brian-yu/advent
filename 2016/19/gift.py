

# def findNext(elf, elves):
# 	i = (elf+1)%len(elves)
# 	while elves[i] == 0:
# 		i = (i+1)%len(elves)
# 	return i



# def exchange(num):
# 	elves = [1 for i in range(num)]
# 	hasGift = [1 for i in range(num)]
# 	#print(elves)

# 	numPres = set()

# 	i = 0
# 	while num not in numPres:
		
# 		if elves[i] != 0:
# 			#print(elves)
# 			j = findNext(i, elves)
# 			elves[i] += elves[j]
# 			elves[j] = 0
# 			numPres.add(elves[i])
# 		i = (i+1) % num
# 	#print(elves)

# 	return i

def findNext(elf, elves):
	i = (elf+1)%len(elves)
	while elves[i] == 0:
		i = (i+1)%len(elves)
	return i



def exchange(num):
	elves = [i+1 for i in range(num)]
	
	i = 0
	while len(elves) > 2:
		across = (i + len(elves)//2)%len(elves)
		# print(elves)
		if len(elves) % 100 == 0:
			print(len(elves)) 
		# print(across)
		
		
		del elves[across]
		i = (i+1) % len(elves)
	#print(elves)

	return elves[(i-1)%len(elves)]


print(exchange(3001330))