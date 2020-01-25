import math
a = [2,3,5]

for i in range(7,2000000,2):
	k = 0
	for j in a:
		if j <= int(math.sqrt(i)):
			if i%j==0:
				k += 1
				break
		else:
			break
	if k == 0:
		a.append(i)
		print(i)

s = 0
for i in a:
	s += i

print(s)
