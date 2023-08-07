import sys
input = sys.stdin.readline

n = int(input().rstrip())
cranes = list(map(int, input().rstrip().split()))
box = int(input().rstrip())
boxes = list(map(int, input().rstrip().split()))
result = 0

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0] :
    print(-1)
else :
    while boxes :
        result += 1
        for i in range(len(cranes)) :
            for j in range(len(boxes)) :
                if cranes[i] >= boxes[j] :
                    boxes.pop(j)
                    break
    print(result)