a = 1
for i in range(1,101):
	a *= i

b = str(a)
s = 0
for i in b:
	s += int(i)

print(s)
