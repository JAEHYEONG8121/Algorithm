## 1. stack - 단어순서 뒤집

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
- for문 안에서 s = input().split()형태로 입력받으면, 띄어쓰기를 기준으로 단어들이 구분되어 리스트에 저장됨
- 리스트를 거꾸로 순회하면서, 간격은 띄어쓰기 한 칸으로 설정하여 출력하면 된다.
***

**다른 풀이**
```python
for i in range(int(input())):
    print("Case #%d:"%(i+1), " ".join(list(reversed(input().split(" ")))))
```

- 육안으로 봐도 훨씬 간단해보인다.
- 하나의 for문과 format형식의 문법으로 한 번에 print한 것이다.
- list(reversed(input().split())) -> 이를 통해서 내가 단어가 저장되어 있는 리스트를 거꾸로 순회하는 것을 한 번에 실현했다.
- 마지막으로 리스트를 문자열로 일정한 규칙으로 합쳐주는 join메서드를 사용하여 띄어쓰기를 간격으로 문장에 있는 단어들을 거꾸로 출력하였다.
    
