a = [2,3,5]

b = 7
while len(a) != 10001:
	k = 0
	for i in a:
		if b % i == 0:
			k += 1
			break
	if k == 0:
		a.append(b)
	b += 2

print(a[-1])
