l1 = [list(map(int, input().split())) for _ in range(9)]
result = 0

for i in range(9) :
    if max(l1[i]) >= result :
        result = max(l1[i])
        n = i + 1
        m = l1[i].index(result) + 1
print(result)
print(n, m)