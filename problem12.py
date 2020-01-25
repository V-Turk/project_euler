import math

a = [1,3,6,10]
b = []
k = 0
while k == 0:
	for i in range(5,1000000):
		j = a[-1] + i
		a.append(j)
		count = 1
		if j%10 == 0:
			for l in range(1,int(j/2)+1):
				if j % l == 0:
					count += 1
					if count >= 500:
						k = 1
			print(j,count)

print(j)



