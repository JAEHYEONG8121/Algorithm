import sys

n = int(sys.stdin.readline())
cards = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in cards :
    if i in cnt :
        cnt[i] += 1
    else :
        cnt[i] = 1

for i in checks :
    if i in cnt :
        print(cnt[i], end=' ')
    else :
        print(0, end= ' ')