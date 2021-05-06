import sys

# 상품 고유번호
id_num = list(map(int, sys.stdin.readline().split()))
# print(id_num)

# 검증수
verified = 0
for n in id_num :
    # 각 고유번호 자릿수의 제곱한 값을 모두 더한다
    verified += n**2

# 10으로 나눈 나머지값이 진짜 검증수이다
verified %= 10

print(verified)