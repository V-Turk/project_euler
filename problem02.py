
a = [1,2,3,5]
while a[-1] < 4000001:
	k = a[-1] + a[-2]
	a.append(k)
s = 0
for i in a:
	if i % 2 == 0:
		s += i

print(s)