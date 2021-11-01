import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline().rstrip()

ans1 = a * int(b[2])
ans2 = a * int(b[1]) * 10
ans3 = a * int(b[0]) * 100 

print(ans1)
print(ans2 // 10)
print(ans3 // 100)
print(ans1 + ans2 + ans3)
