# Algorithm

## 1. sort - 회의실 배정

문제 : https://www.acmicpc.net/problem/1931

**내 풀이**
```python
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
```
- 한 개의 회의실에서 이를 사용하고자하는 N개의 회의에 대하여 최대로 사용할 수 있는 회의의 개수를 출력해야 한다.
- 회의의 시작시간과 끝나는 시간이 입력으로 주어지는데, 이를 for문을 통해서 2차원 리스트의 형태로 받아주었다.
- 결국 어떤 회의가 끝나는 시간과 다음 회의가 시작되는 시간이 중요하다.
    - 최대한 많은 회의를 하려면 우선적으로 빨리 끝나는 회의 순으로 정렬을 해주어야 한다.
    - l이라는 리스트 안에 특정 회의의 시작시간과 끝나는 시간이 리스트 형태로 담겨져 있는데, 이를 람다함수를 통해 인자를 지정해주었다.
    - sort()함수의 key값을 통해 정렬하는데, 이를 튜플형태로 지정하여 회의가 끝나는 시간을 기준으로 정렬을 구현했다.
- 정렬을 한 후에는 for문을 통해 리스트를 순회하면서 끝나는 시간을 계속 갱신해주면서 하나의 회의실에서 진행할 수 있는 최대 회의의 수를 cnt값에 저장했다.

**Review**

- 이 문제는 그리디 알고리즘과 정렬의 개념이 합쳐진 문제였다. 최대값을 구하기 위해 리스트안에 있는 회의시간을 어떤기준으로 어떻게 정렬할 것인지가 핵심이라고 생각한다.
- 추가적으로, sort() 함수의 key값을 람다함수를 통해 정렬할 수 있다는 것을 다시 한 번 상기하게 되었다.

***

## 2. sort - 신입사원

문제 : https://www.acmicpc.net/problem/1946

**내 풀이**
```python
import sys

input = sys.stdin.readline

for _ in range(int(input())) :
    l = []
    cnt, top = 1, 0
    for _ in range(int(input())) :
        a = tuple(map(int, input().split()))
        l.append(a)
    l.sort(key=lambda x: (x[0], x[1]))
    for i in range(1, len(l)) :
        if l[i][1] < l[top][1] :
            top = i
            cnt += 1 
    print(cnt)
```
- 회사에서 신입사원을 고용하는데, 고용 기준은 서류심사 성적과 면접심사 성적 둘 중에 적어도 하나가 다른 지원자보다 낮지 않은 경우만 선발하는 것이다.
- 즉, 서류와 면접성적 둘 다 어떠한 경쟁자보다 우위에 있지 않다면 그사람은 불합격인 것이다.
- 우선적으로 '(서류 성적, 면접 성적)'와 같은 형태의 튜플로 입력받아 l이라는 리스트에 저장했고, 이를 튜플의 서류 성적을 기준으로 정렬했다.
- 1 4 o
  2 5 x
  3 6 x
  4 2 o
  5 7 x
  6 1 o
  7 3 x













