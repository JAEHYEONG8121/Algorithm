import sys

n, m = map(int, sys.stdin.readline().split())
s1, s2 = set(), set()
cnt = 0
s3 = set()
l = []

for _ in range(n) :
   s1.add(sys.stdin.readline().strip())
for _ in range(m) :
    s2.add(sys.stdin.readline().strip())

for i in s1 :
    if i in s2 :
        cnt += 1
        s3.add(i)
        
print(cnt)

for i in s3 :
    l.append(i)
l.sort()
for i in l :
    print(i)