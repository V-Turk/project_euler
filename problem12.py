a = [];
i = 1;
j = 1;
x = 0;
b = [];
while i < 2:
    b = [];
    x = x + j;
    for k in range(1,int(x**(1/2))+1):
        if x % k == 0:
            b.append(k)
            if x // k != k:
                b.append(x // k)
    print(j,x,len(b))
    if len(b) >= 500:
        i += 1;
        print("|||||    ",x, len(b))
    j += 1;
