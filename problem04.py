a = []
for i in range(100,1000):
	for j in range(100,1000):
		k = i * j
		p = str(k)
		if len(p)%2==0:
			r = 0
			for q in range(int(len(p)/2)):
				if p[q] != p[(-q)-1]:
					r += 1
					break
			if r == 0:
				a.append(k)
		else:
			r = 0
			for q in range(int(len(p)/2)):
				if p[q] != p[(-q)-1]:
					r += 1
					break
			if r == 0:
				a.append(k)

print(max(a))


