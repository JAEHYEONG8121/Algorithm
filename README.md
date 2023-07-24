# Algorithm

## 1. stack - 막대기

문제 : https://www.acmicpc.net/problem/17608

**내풀이**
```python
import sys

n = int(sys.stdin.readline())
l = []
cnt = 1

for _ in range(n) :
    l.append(int(sys.stdin.readline()))
last = l[-1]

for i in reversed(range(len(l))) :
    if l[i] > last :
        cnt +=1
        last = l[i]
print(cnt)
```

- 오른쪽에서 봤을 때 보이는 막대기의 수를 구하는 문제
- 처음에는 

