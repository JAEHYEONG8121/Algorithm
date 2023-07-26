n, k = map(int, input().split())
l = [i for i in range(1, n+1)]
s = []
idx = 0

while(1) :
    if len(l) == 0 :
        break
    else :
        idx += (k-1)
        if idx >= len(l) :
            idx %= len(l)
        s.append(l.pop(idx))
print("<", end="")
for i in range(len(s)) :
    if i == len(s)-1 :
        print(s[i], end="")
    else :
        print(s[i], end=", ")
print(">")