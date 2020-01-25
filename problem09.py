for b in range(1,997):
	for a in range(b,1001):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			k = a*b*c
			break
print(k)