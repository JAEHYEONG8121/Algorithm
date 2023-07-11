n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
min = 0
cost = 0

for i in range(len(l2)-1) :
    if i == 0 :
        min = l2[i]
        cost += min * l1[i]
    elif l2[i] < min :
        min = l2[i]
        cost += min * l1[i]
    else :
        cost += min * l1[i]

print(cost)