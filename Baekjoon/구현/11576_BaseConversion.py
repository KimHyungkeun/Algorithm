import sys

a, b = map(int, sys.stdin.readline().split()) # 현재 a진수이며 b진수로 바꿔야 한다
m = int(sys.stdin.readline()) # 자릿수는 총 m개이다
arr = list(map(int ,sys.stdin.readline().split())) # 각 자릿수의 숫자를 공백을 기준으로 띄워서 쓴다
arr.reverse()

total = 0

for i in range(len(arr)) :
    total += (arr[i] * (a**i)) #현재 자릿수에 a^i 승을 곱한값을 누적하여, 임시로 10진수로 바꾼다

# print(total)
result = []

# 임시로 바꾼 10진수를 다시 8진수로 바꾸는 작업을 한다
while total != 0 :
    result.append(total % b)
    total //= b

# 연산 후, result에 나온 값들을 역순으로 재배치한다
result.reverse()
print(*result)
