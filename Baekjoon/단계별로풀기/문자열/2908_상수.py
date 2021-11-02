import sys

a, b = sys.stdin.readline().split()

a = reversed(list(a))
b = reversed(list(b))

num_a = int(''.join(a))
num_b = int(''.join(b))

print(max(num_a, num_b))