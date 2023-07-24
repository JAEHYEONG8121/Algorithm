import sys

n = int(sys.stdin.readline().strip())
stack = []

for _ in range(n) :
    a = sys.stdin.readline().strip()
    
    if a[0] == '1' :
        stack.append(int(a[2:]))
    elif a == '2' :
        if stack :
            print(stack.pop())
        else :
            print(-1)
    elif a == '3' :
        print(len(stack))
    elif a == '4' :
        if not stack :
            print(1)
        else :
            print(0)
    elif a == '5' :
        if stack :
            print(stack[-1])
        else :
            print(-1)   
