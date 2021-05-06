import sys

# 문자열길이 n, 문자열 입력
n = int(sys.stdin.readline())
string = input()

result = 0
for i in range(n) :
    # 해당 글자가 대문자인경우, 아스키코드 룰에 의해 64를 빼서 1 ~ 26까지의 값으로 변환
    if 65 <= ord(string[i]) <= 90 :
        tmp = ord(string[i]) - 64
    
    # 해당 글자가 소문자인경우, 아스키코드 룰에 의해 96을 빼서 1 ~ 26까지의 값으로 변환
    elif 97 <= ord(string[i]) <= 122 :
        tmp = ord(string[i]) - 96
    
    # 문제에 주어진 해쉬 함수 적용
    result += ((tmp) * (31**i))

# 1234567891로 나누어 나머지를 구함
result %= 1234567891
print(result)
