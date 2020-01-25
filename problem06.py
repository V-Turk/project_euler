a = (100*(100+1))/2
b = 0
for i in range(1,101):
	b = b + i**2

print(int(a**2 - b))