import sys

# 두 수를 입력
a, b = map(int ,sys.stdin.readline().split())

def euclid (a, b) :
    if a < b : #만약 b가 a보다 크다면 두 수를 swap 한다
        a,b = b,a
    while b != 0 :
        r = a % b # b로 나누었을때 나머지를 구해서
        a = b # a자리에 b를
        b = r # b자리에 나머지 r을 대입

    return a

result = euclid(a,b)
print(result)

# https://level.goorm.io/exam/43091/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95/quiz/1