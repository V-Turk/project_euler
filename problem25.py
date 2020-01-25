f = [1,1,2,3,5,8,13,21,34,55,89,144]
k = 1
while k == 1:
	b = f[-1] + f[-2]
	f.append(b)
	if len(str(b)) >= 1000:
		k +=1
	print(b)

print(len(f))