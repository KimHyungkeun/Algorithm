import sys

# 숫자 n과 반복될 횟수 m을 입력
n, m = map(int, sys.stdin.readline().split())

# 숫자 n을 n번 반복
string = ""
for _ in range(n) :
    string += str(n)

# 길이가 너무 길어지면 앞 m길이 까지만 출력
print(string[:m])