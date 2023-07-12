import sys

n, m = map(int, sys.stdin.readline().split())
s = set()
l = []
cnt = 0

for _ in range(n) :
    s.add(input())

for _ in range(m) :
    l.append(input())

for i in l :
    if i in s :
        cnt += 1
print(cnt)    

