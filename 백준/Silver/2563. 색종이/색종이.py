l = [ [0] * 100 for _ in range(100)]
n = int(input())
for i in range(n) :
    r, c = map(int, input().split())
    for j in range(r-1,r+9) :
        for k in range(c-1, c+9) :
            l[j][k] = 1

cnt = sum(i.count(1) for i in l)
print(cnt)