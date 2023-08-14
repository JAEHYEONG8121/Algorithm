n = int(input())
l = []
for i in range(n) :
    for j in range(n) :
        if (3 * i + 5 * j) == n :
            l.append(i+j)
l.sort()
if len(l) == 0 :
    print(-1)
else :
    print(l[0])