s = input()
answer = 'z' * len(s)

for i in range(1, len(s)-1) :
    for j in range(i+1, len(s)) :
        result = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        answer = min(answer, result)
        
print(answer)