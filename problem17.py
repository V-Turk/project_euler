jedinice = ['','one','two','three','four','five','six','seven','eight','nine']

deset = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

desetice = ['','','twenty', 'thirty','forty','fifty','sixty','seventy','eighty','ninety']

sto = 'hundred'

hiljadu = 'thousand'

and1 = 'and'
s = 0
for i in range(1,1001):
	a = str(i)
	if i < 10:
		s += len(jedinice[i])
		print(i, jedinice[i])
	elif i < 20:
		a1 = int(a[1])
		s += len(deset[a1])
		print(i, deset[a1])
	elif i < 100:
		a1 = int(a[0])
		a2 = int(a[1])
		s += len(desetice[a1]) + len(jedinice[a2])
		print(i, desetice[a1] + jedinice[a2])
	elif i < 1000:
		a1 = int(a[0])
		a2 = int(a[1])
		a3 = int(a[2])
		if a2 == 1:
			s += len(jedinice[a1]) + len(sto) + len(and1) + len(deset[a3])
			print(i, jedinice[a1] + sto + and1 + deset[a3])
		elif a2 == 0:
			if a3 == 0:
				s += len(jedinice[a1]) + len(sto)
				print(i, jedinice[a1] + sto)
			else:
				s += len(jedinice[a1]) + len(sto) + len(and1) + len(jedinice[a3])
				print(i, jedinice[a1] + sto + and1 + jedinice[a3])
		else:
			s += len(jedinice[a1]) + len(sto) + len(and1) +len(desetice[a2]) + len(jedinice[a3])
			print(i, jedinice[a1] + sto + and1 + desetice[a2] + jedinice[a3])
	else:
		s += len(jedinice[1]) + len(hiljadu)
		print(i, jedinice[1] + hiljadu)

print(s)
print(len(desetice[0]))