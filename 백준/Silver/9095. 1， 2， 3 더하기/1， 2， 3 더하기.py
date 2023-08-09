import sys
input = sys.stdin.readline
l = [0] * 12
l[1] = 1
l[2] = 2
l[3] = 4

for i in range(4, 12) :
    l[i] = l[i-1] + l[i-2] + l[i-3]
    
for _ in range(int(input())) :
    n = int(input())
    print(l[n])