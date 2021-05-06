import sys

# 진짜 약수의 갯수 n을 입력
n = int(sys.stdin.readline())
# 진짜 약수들을 입력
multiple = list(map(int, sys.stdin.readline().split()))
multiple.sort() # 오름차순 정렬

# 배열 중앙지점을 찾기위함 
mid = len(multiple) // 2

# 배열 길이가 짝수인 경우
if n % 2 == 0 :
    # 중앙부근과 그 이전 요소를 서로 곱하면, 어떤 수의 약수인지 알수 있다
    result = multiple[mid] * multiple[mid-1] 

# 배열 길이가 홀수인 경우
else :
    # 제곱을 하여 해당 수가 나타나는 경우이다.
    result = multiple[mid] ** 2

print(result)
