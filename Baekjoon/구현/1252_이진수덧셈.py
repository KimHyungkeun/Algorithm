import sys

# 두 이진수를 입력 받음
num1, num2 = sys.stdin.readline().split()

# 두 이진수를 잠시 십진수로 변환
num1 = int(num1, 2)
num2 = int(num2, 2)

# 두 수의 합을 구하고, 그 결과값을 다시 이진수로 변환
result = num1 + num2
result = bin(result)

# bin로 변환시 앞 두글자에 "0b"가 나오므로, 그 부분을 제외한 다음 부분부터 읽어들임
str_result = str(result)[2:]
print(str_result)

