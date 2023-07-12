n, m = map(int, input().split())
l = [i for i in range(1, n+1)]

for _ in range(m) :
    i, j = map(int, input().split())
    num = int((j - i)/2 + 0.5)
    if num == 0 :
        pass
    else :
        for k in range(num) :
            l[i - 1 + k], l[j - 1 - k] = l[j - 1 - k], l[i - 1 + k]
for i in l :
    print(i, end = ' ')