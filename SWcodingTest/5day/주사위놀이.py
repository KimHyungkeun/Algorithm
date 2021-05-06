import sys

n = int(sys.stdin.readline())

# 주사위 숫자는 1~6
dais = [1,2,3,4,5,6]

for i in range(1,7) :
    if n - i in dais : # 전체합 n에서 비교하려는 숫자 i를 뺐을때
        print(i, n-i)  # 그 결과값이 주사위 내 숫자이면 그 숫자를 표현

# https://level.goorm.io/exam/43157/%EC%A3%BC%EC%82%AC%EC%9C%84-%EB%86%80%EC%9D%B4/quiz/1