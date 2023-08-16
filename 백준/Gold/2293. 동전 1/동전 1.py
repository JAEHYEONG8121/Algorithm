import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in coin:
    for i in range(k+1):
        if i - c >= 0:
            dp[i] += dp[i-c]

print(dp[k])