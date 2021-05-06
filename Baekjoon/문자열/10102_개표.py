import sys

# 심사위원수 n, 투표현황 string
n = int(sys.stdin.readline())
string = list(sys.stdin.readline().rstrip())

# A의 갯수와 B의 갯수를 구함
a = string.count('A')
b = len(string) - a

# A가 더 많을 경우
if a > b :
    print("A")

# B가 더 많을 경우
elif a < b :
    print("B")

# 둘다 같을 경우
else :
    print("Tie")



