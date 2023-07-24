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
- 처음에는 입력받은 막대기를 리스트에 저장
- 리스트를 거꾸로 순회하면서 크기 비교 & 카운트
  - 1. 원소 입력 받고 리스트에 저장
    2. 리스트의 가장 오른쪽(마지막)원소를 last변수에 저장
    3. 리스트를 for문을 통해 거꾸로 순회하면서 크기 비교 -> cnt 1증가 & last변수 갱신
    

