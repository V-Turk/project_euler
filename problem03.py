import math
a = [2,3,5]
b = [2,3,5]

start = 11
end = 25
  
for i in range(7, int(math.sqrt(600851475143)),2):
	k = 0
	for j in a:
		if i % j ==0:
			k += 1
	if k == 0:
		a.append(i)


for i in a:
	if 600851475143 % i == 0:
		b.append(i)

print(b)