def even(n):
	n = n/2

def odd(n):
	n = 3*n+1

maxim = 0

num = 1

for i in range(2,1000000):
	k = int(i)
	s = 0
	count = 0
	print(k)
	while s != 1:
		if k % 2 == 0:
			k = k/2
			count +=1
		elif k == 1:
			s +=1
		else:
			k = 3*k+1
			count +=1
	if count > maxim:
		maxim = count
		num = i

print(num, maxim)
