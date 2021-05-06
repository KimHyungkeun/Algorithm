import sys

number = list(sys.stdin.readline().rstrip())
mid = len(number) // 2

left = 0
for i in range(mid) :
    left += int(number[i])

right = 0
for i in range(mid, len(number)) :
    right += int(number[i])

if left == right :
    print("LUCKY")

else :
    print("READY")

# print(number)