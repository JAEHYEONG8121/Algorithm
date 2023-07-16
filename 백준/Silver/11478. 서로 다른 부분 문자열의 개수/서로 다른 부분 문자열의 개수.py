import sys

s1 = set()
s = sys.stdin.readline().strip()

for i in range(len(s)) :
    for j in range(i+1, len(s)+1) :
        s1.add(s[i:j])   

print(len(s1))