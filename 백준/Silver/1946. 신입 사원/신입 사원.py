import sys

input = sys.stdin.readline

for _ in range(int(input())) :
    l = []
    cnt, top = 1, 0
    for _ in range(int(input())) :
        a = tuple(map(int, input().split()))
        l.append(a)
    l.sort(key=lambda x: (x[0], x[1]))
    for i in range(1, len(l)) :
        if l[i][1] < l[top][1] :
            top = i
            cnt += 1 
    print(cnt)