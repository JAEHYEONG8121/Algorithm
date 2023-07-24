n = int(input())

for i in range(1, n+1) :
    s = input().split()
    print('Case #{0}: '.format(i), end='')
    for j in reversed(range(len(s))) :
        print(s[j], end= ' ')
    print()
    