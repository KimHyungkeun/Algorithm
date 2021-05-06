import sys

n = int(sys.stdin.readline())
plug = []

answer = 0
for _ in range(n) :
    answer += int(sys.stdin.readline())

print(answer - n + 1)