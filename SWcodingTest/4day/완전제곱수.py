import sys

n, m = map(int ,sys.stdin.readline().split())
start = 1
result = []

# 1부터 시작하여 해당 숫자의 제곱수를 비교
while start :
    # 만약 m을 넘어선 제곱수이면 루프문 탈출
    if start**2 > m :
        break
    
    # n이상 m이하의 제곱수이면 리스트에 추가
    if n <= start**2 <= m :
        result.append(start**2)
    
    start += 1

# 제곱수 리스트 중 최소값과, 총 제곱수들의 합을 구함
print(result[0], sum(result))

# https://level.goorm.io/exam/43116/%EC%99%84%EC%A0%84-%EC%A0%9C%EA%B3%B1%EC%88%98/quiz/1