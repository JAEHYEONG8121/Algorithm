n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]
l.sort(reverse=True)
cnt = 0

for i in l :
    if k % i == k :
        pass
    else :
        cnt += k // i
        k %= i
print(cnt)