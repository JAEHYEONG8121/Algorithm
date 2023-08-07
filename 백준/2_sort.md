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
- 1 4 o<br>
  2 5 x<br>
  3 6 x<br>
  4 2 o<br>
  5 7 x<br>
  6 1 o<br>
  7 3 x<br>

- 위의 예시를 보자. 내가 생각한 방법은 서류 성적을 기준으로 정렬된 상태에서 면접 점수를 비교하는 것인데, 어차피 서류 성적이 1등인 사람은 무조건 합격할 자격이 주어지는 것이므로 cnt = 1로 두고 더해가기로 했다.
- 처음에는 for문의 range를 1부터 시작해서, 서류 성적이 1등인 사람의 면접 성적보다 더 높은 순위를 얻은 사람인 경우 합격처리를 하는 코드인 if l[i][1] < l[0][1] : 이렇게 작성하면 된다고 생갂했다.
- 하지만, 면접 성적의 경우 계속 갱신을 해줘야한다는 것을 뒤늦게 깨달았다.
- top이라는 변수를 만들어서 현상태에서 면접성적이 가장 좋은 사람의 인덱스를 top에 저장해두고, for문을 순회하면서 if l[i][1] < l[top][1] : 이렇게 비교하여 이 조건이 만족할 시 cnt를 1씩 증가시켜주었다.

   
**Review**
- 솔직히 그리 어려운 문제는 아니다.. 서류 성적을 기준으로 정렬한 후에 면접 성적을 비교하는 것이 포인트인데, 비교할 때 계속 최고 성적을 갱신해줘야한다는 생각을 일찍하지 못해서 5번이나 틀렸다,,

***

## 3. sort - 두 용액

문제 : https://www.acmicpc.net/problem/2740

**내 풀이**
```python
n = int(input())
l = list(map(int, input().split()))
l.sort()

left = 0
right = n-1

answer = abs(l[left] + l[right])
result = [l[left], l[right]]


while left < right:
    left_val = l[left]
    right_val = l[right]

    sum = left_val + right_val
  
    if abs(sum) < answer:
        answer = abs(sum)
        result = [left_val, right_val]
        if answer == 0:
          break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])

```

- 두 수를 합쳐서 0에 가장 가까운 경우를 출력해야 한다.
- 음수, 양수가 섞여있으므로 두 수의 합의 절댓값이 0에 가까운 수가 나올 수 있도록 우선적으로 리스트를 정렬했다.
- 정렬이 되었다면, 가장 왼쪽과 가장 오른쪽에서 각각 인덱스를 left, right로 지정해주고 그 때 두 수의 합을 answer에 저장해둔다.
- 이제 두 인덱스가 만나지 않을 때까지 반복하여 answer값이 현재 answer값보다 작다면 계속 갱신하고 그 때의 절댓값이 아닌 실제 계산값의 부호를 통해서 만약 음수라면 left를 한 칸 오른쪽으로, 양수라면 right를 한 칸 왼쪽으로 당겨가면서 최대한 0에 가까운 수가 나올 수 있도록 하였다.

**Review**
- 처음에는 양수 부분 음수 부분을 나누어서 하려고 했으나 불필요한 짓이었다.
- 정렬를 한 상태에서 왼쪽 끝과 오른쪽 끝에서부터 각각 시작하여 두 수의 합의 절댓값이 계속 0에 가까워질 수 있게 만들어주면 되는 것이었다.












