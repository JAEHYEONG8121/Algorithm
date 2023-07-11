l = [list(map(str, input().split())) for _ in range(5)]
max = 0

for i in range(5) :
    if len(l[i][0]) > max :
        max = len(l[i][0])

for i in range(max) :
    for j in range(5) :
        if i >= len(l[j][0]) :
             continue
        else :
            print(l[j][0][i], end='')
