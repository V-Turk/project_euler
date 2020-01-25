j = 20
n = 1
while n == 1:
	k = 0
	for i in range(2,21):
		if j % i != 0:
			k += 1
			break
	if k == 0:
		n += 1
	j += 20

print(j-20)