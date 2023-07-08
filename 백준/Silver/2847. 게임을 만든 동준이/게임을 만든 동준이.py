n = int(input())
l = [int(input()) for i in range(n)]
lst = []
cnt = 0

for i in range(len(l)) :
    lst.append(l.pop())

for i in range(len(lst)-1) :
    if lst[i] > lst[i+1] :
        pass
    else :
        cnt += lst[i+1] - (lst[i]-1)
        lst[i+1] -= lst[i+1] - (lst[i]-1)
        
print(cnt)