n, m = map(int, input().split())
l = [i for i in range(1, n+1)]

for _ in range(m) :
    i, j = map(int, input().split())
    l[i-1], l[j-1] = l[j-1], l[i-1]
for i in l :
    print(i, end = ' ')