
f = open("input.txt")

nums = []

for line in f:
	for num in line.strip():
		nums.append(int(num))

def findSum(nums):
	s = 0
	for i in range(len(nums)):
		num = nums[i]
		nextNum = nums[(i+1)%len(nums)]
		if num == nextNum:
			s += num
	return s


def findHalfSum(nums):
	s = 0
	for i in range(len(nums)):
		num = nums[i]
		nextNum = nums[(i+len(nums)//2)%len(nums)]
		if num == nextNum:
			s += num
	return s

print(findHalfSum(nums))
print(findHalfSum([int(i) for i in "1212"]))
print(findHalfSum([int(i) for i in "1221"]))
print(findHalfSum([int(i) for i in "123425"]))
print(findHalfSum([int(i) for i in "123123"]))
print(findHalfSum([int(i) for i in "12131415"]))