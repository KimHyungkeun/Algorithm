import sys

# 이진수 입력
n = list(sys.stdin.readline().rstrip())
n.reverse() # 십진수로 만들기 위해 잠시 배열순서를 거꾸로 설정


# 십진수로 설정
cnt = 0
for i in range(len(n)) :
    if n[i] == '1' :
        cnt += (2**i)

# 십진수를 8진수로 만들고 값 출력(0o 이라는 접두어가 붙으므로 2번째 순서부터 문자열 출력)
cnt = str(oct(cnt))
print(cnt[2:])