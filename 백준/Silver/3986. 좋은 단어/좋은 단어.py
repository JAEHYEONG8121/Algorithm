n = int(input())
cnt = 0

for _ in range(n) :
    s = input()
    l = []
    
    for i in s :
        if l and l[-1] == i :
            l.pop()
        else :
            l.append(i)
    if not l :
        cnt += 1
print(cnt)