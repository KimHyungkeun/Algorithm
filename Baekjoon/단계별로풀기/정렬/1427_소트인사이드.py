import sys

num = list(sys.stdin.readline().rstrip())
num.sort(reverse=True)

print(''.join(num))