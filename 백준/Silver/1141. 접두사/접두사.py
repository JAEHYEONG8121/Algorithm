import sys
input = sys.stdin.readline

n = int(input())
l = [input().rstrip() for i in range(n)]
l.sort()
cnt = 1

for i in range(len(l)-1) :
    if l[i] == l[i+1][:len(l[i])] :
        pass
    else :
        cnt += 1
print(cnt)