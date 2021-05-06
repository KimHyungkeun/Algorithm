import sys

r1, s = map(int, sys.stdin.readline().split())

# (r1+r2) / 2 = s 이므로,   r2 = 2s - r1이다.
r2 = 2*s - r1
print(r2)