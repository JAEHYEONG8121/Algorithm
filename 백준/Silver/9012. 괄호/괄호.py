import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    s1 = []
    s = input()
    for i in range(len(s)) :
        if s[i] == '(' :
            s1.append(s[i])
        elif s[i] == ')' :
            if len(s1) != 0 :
                s1.pop()
            else :
                print("NO")
                break
        elif i == len(s)-1 :
            if len(s1) == 0 :
                print("YES")
            else :
                print("NO")
        