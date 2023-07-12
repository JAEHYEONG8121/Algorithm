n , m = map(int, input().split())
l = [0] * n
for _ in range(m) :
    i, j, k = map(int, input().split())
    for num in range(i-1, j) :
        l[num] = k
for r in l :
    print(r, end=' ')