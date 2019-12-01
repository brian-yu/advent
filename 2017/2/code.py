f = open("input.txt")

checksum1 = 0
checksum2 = 0

for line in f:
	nums = [int(i) for i in line.strip().split("\t")]

	checksum2 += [i//j for i in nums for j in nums if i % j == 0 and i != j][0]
	checksum1 += max(nums) - min(nums)

print(checksum1)
print(checksum2)
