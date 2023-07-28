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
***

## 2. stack - 단어순서 뒤집기

문제 : https://www.acmicpc.net/problem/12605

**내풀이**
```python
n = int(input())

for i in range(1, n+1) :
    s = input().split()
    print('Case #{0}: '.format(i), end='')
    for j in reversed(range(len(s))) :
        print(s[j], end= ' ')
    print()
```

- 문장을 입력받고, 입력 받은 문장의 단어들의 순서를 뒤집어서 case별로 출력하는 문제
- for문 안에서 s = input().split()형태로 입력받으면, 띄어쓰기를 기준으로 단어들이 구분되어 리스트에 저장됨.
- 리스트를 거꾸로 순회하면서, 간격은 띄어쓰기 한 칸으로 설정하여 출력하면 된다.

**다른 풀이**
```python
for i in range(int(input())):
    print("Case #%d:"%(i+1), " ".join(list(reversed(input().split(" ")))))
```

- 육안으로 봐도 훨씬 간단해보인다.
- 하나의 for문과 format형식의 문법으로 한 번에 print한 것이다.
- list(reversed(input().split())) -> 이를 통해서 내가 단어가 저장되어 있는 리스트를 거꾸로 순회하는 것을 한 번에 실현했다.
- 마지막으로 리스트를 문자열로 일정한 규칙으로 합쳐주는 join메서드를 사용하여 띄어쓰기를 간격으로 문장에 있는 단어들을 거꾸로 출력하였다.

**Review**
- 결국 스택 자료구조의 핵심은 LIFO(Last In First Out)이라고 생각이 들었다. 이를 통해서 리스트를 거꾸로 순회한다든가, pop()메서드를 통해 리스트에 존재하는 가장 오른쪽(마지막)원소에 대한 접근을 가능케 하는 것이 핵심이라고 생각한다.

***

## 3.stack - 요세푸스 문제 (23.08.01)

문제 : https://www.acmicpc.net/problem/1158

**내풀이**
```python
n, k = map(int, input().split())
l = [i for i in range(1, n+1)]
s = []
idx = 0

while(1) :
    if len(l) == 0 :
        break
    else :
        idx += (k-1)
        if idx >= len(l) :
            idx %= len(l)
        s.append(str(l.pop(idx)))
        
print("<", ", ".join(s), ">", sep="")
```

- 1번부터 n명의 사람이 원을 이루면서 앉아있는 상태에서 순서대로 k번째 사람을 제거한디.
- 예를 들어, n=7, k=3이라면
      - 1 2 3 4 5 6 7
      - 1 2 4 5 6 7
      - 1 2 4 5 7
      - 1 4 5 7
      - 1 4 5
      - 1 4
      - 4
- 위와 같은 순서로 모든 사람이 제거될 때까지 k번째 사람을 한 명씩 제거해가는 문제이다.
- 제거되는 순서를 바로 '요세푸스 순열'이라하고 그 순열을 출력하면 되는 것이다.
- 내 풀이의 핵심은 index로 접근한 것이다.
      - 우선 n을 입력받아 1부터 n까지의 숫자를 담은 리스트를 하나 만든다.
      - 인덱스를 계속 변경해가며 리스트에 담긴 숫자를 pop을 통해 제거하고, 만들어놓은 다른 리스트에 제거되는 순서대로 append해준다
- index를 갱신하는 법을 생각해보자. 사람들이 동그랗게 앉아있는 것을 고려해보자면
      - index를 (k-1)만큼 계속 더해간다면 리스트의 길이보다 인덱스가 커질 것이다.
      - 그러므로, index를 (k-1)만큼 계속 더하면서 리스트의 길이보다 같거나 길어진다면 현재 리스트의 길이로 나눈 나머지로 갱신해주는 방법으로 해결했다.
- s리스트에 append할 때 str형태로 넣어주어서 print시 join메서드를 활용하여 출력했다.

**다른 풀이**
```python
import sys
from collections import deque

# 입력 받기
n, k = map(int, input().split())

# 양방향 연결 리스트(deque) 생성
deq = deque([i for i in range(1, n+1)])

# 요세푸스 순열 생성
res = []
while len(deq) != 0:
    for _ in range(k-1):
        # k-1번째 노드까지 deq 맨 뒤로 이동
        deq.append(deq.popleft())
    # k번째 노드 삭제 후 결과 배열에 추가
    res.append(str(deq.popleft()))

# 결과 출력
print('<'+', '.join(res)+'>')
```

- 위의 다른 풀이를 살펴보면, '덱'을 사용한 풀이다.
- 덱에서 k-1번째까지 원소를 맨 뒤로 이동시키고, k번째 노드를 삭제하여 결과 배열에 추가하는 방식이다.
- 결국 k-1번째까지의 원소들을 pop하여 매번 큐를 회전시키는 방식인 것이다.

**Review**
- 내 풀이는 매번 k-1개씩 원소들을 뛰어넘고 pop()을 통해 결과 리스트에 추가하는 방식으로 시간복잡도가 <mark>O(n)</mark>이다.
- 하지만, 다른 풀이에서는 '덱'이라는 자료구조를 통해 k-1번쨰까지의 원소들을 지속적으로 pop()하기 때문에 시간복잡도가 <mark>O(nk)</mark>이다.
- 시간복잡도를 분석해보면서 내 풀이가 시간복잡도 측면에서 효율적임을 알 수 있었고, 상황에 따라 사용할 수 있는 다양한 자료구조를 알고 있는 것이 힘이 될 것이라는 생각을 하게 되었다.



