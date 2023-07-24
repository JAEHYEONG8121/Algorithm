import sys

n = int(sys.stdin.readline())
l = []
cnt = 1

for _ in range(n) :
    l.append(int(sys.stdin.readline()))
last = l[-1]

for i in reversed(range(len(l))) :
    if l[i] > last :
        cnt +=1
        last = l[i]
print(cnt)