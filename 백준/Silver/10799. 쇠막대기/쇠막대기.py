s = list(input())
stack = []
result = 0

for i in range(len(s)) :
    if s[i] == '(' :
        stack.append(s[i])
    elif s[i] == ')' and s[i-1] == '(' :
        stack.pop()
        result += len(stack)
    else :
        stack.pop()
        result += 1

print(result)