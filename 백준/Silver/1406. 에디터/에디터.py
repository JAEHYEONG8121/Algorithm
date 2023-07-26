import sys

s1 = list(sys.stdin.readline().rstrip())
s2 = []
n = int(sys.stdin.readline())

for _ in range(n) :
    c = list(sys.stdin.readline().rstrip())
    
    if c[0] == 'L' :
        if s1 :
            s2.append(s1.pop())
            
    elif c[0] == 'D' :
        if s2 :
            s1.append(s2.pop())
        
    elif c[0] == 'B' :
        if s1 :
            s1.pop()
        
    elif c[0] == 'P' :
        s1.append(c[-1])
        
s = s1 + list(reversed(s2))
print("".join(s))