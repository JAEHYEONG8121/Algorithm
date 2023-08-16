import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    l = [0, 1, 1, 1]
    for i in range(4, int(input())+1) :
        l.append(l[i-3] + l[i-2])
    print(l[-1])