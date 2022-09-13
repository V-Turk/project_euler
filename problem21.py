
a = [];
l = [];
for x in range (1, 10001):
    b = 0;
    for i in range(1, int(x**(1/2))+1):
        if x % i == 0:
            b += i;
            if x // i != i and x // i != x:
                b += (x // i)
    print(x, b)
    a.append(b)
count = 0;
for y in range(1, 10001):
    for z in range(y+1,10001):
        if y == int(a[z-1]) and z == int(a[y-1]) and y != z:
            print(a[y-1], a[z-1])
            count += (a[y-1]);
            count += (a[z-1]);
print(count)

