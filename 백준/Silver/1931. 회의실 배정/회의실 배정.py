n = int(input())
l = []
last_idx = 0
cnt = 0
for i in range(n):
    l.append(list(map(int, input().split())))

l.sort(key=lambda x: (x[1], x[0])) 

for i in range(len(l)):
    if l[i][0] >= last_idx:
        last_idx = l[i][1]
        cnt += 1

print(cnt)