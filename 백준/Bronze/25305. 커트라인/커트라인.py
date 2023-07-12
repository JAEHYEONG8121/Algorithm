n , k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
print(l[k-1])
