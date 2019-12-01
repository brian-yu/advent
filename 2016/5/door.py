import hashlib

ID = "cxdnnyjw"
#ID = "abc"


positions = [str(i) for i in range(8)]
p = ["_" for i in range(8)]
i = 0
while len([i for i in p if i != "_"]) < 8:
	m = hashlib.md5((ID+str(i)).encode())
	hex = m.hexdigest()
	if hex[0:5] == "00000":
		try:
			pos = int(hex[5])
		except:
			pass
		if hex[5] in positions and p[pos] == "_":
			p[pos] = hex[6]
		print("\r" + p)
	i += 1
print("".join(p))