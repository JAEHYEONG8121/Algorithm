import sys

n = int(sys.stdin.readline())
d = {}

for _ in range(n) :
    s1, s2 = map(str, sys.stdin.readline().split())
    d[s1] = s2
d = dict(sorted(d.items(), reverse=True))

for i in d :
    if d[i] == 'enter' :
        print(i)