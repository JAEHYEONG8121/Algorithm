import sys

a, b = map(int, sys.stdin.readline().split())
s1 = set(map(int, sys.stdin.readline().split()))
s2 = set(map(int, sys.stdin.readline().split()))

print(len(s1^s2))