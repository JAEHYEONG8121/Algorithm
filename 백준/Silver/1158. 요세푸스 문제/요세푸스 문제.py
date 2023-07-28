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
        s.append(str(l.pop(idx)))
        
print("<", ", ".join(s), ">", sep="")