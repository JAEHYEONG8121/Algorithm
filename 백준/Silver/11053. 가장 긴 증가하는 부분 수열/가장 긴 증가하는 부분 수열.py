import sys

input = sys.stdin.readline

test_case = int(input().rstrip())
list_ = list(map(int, input().rstrip().split()))
cnt = [1 for i in range(test_case)]

for i in range(test_case) :
    for j in range(i) :
        if list_[j] < list_[i] :
            cnt[i] = max(cnt[j]+1, cnt[i])
print(max(cnt))