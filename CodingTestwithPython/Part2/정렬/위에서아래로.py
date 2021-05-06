import sys

# 테스트케이스 갯수 n 입력
n = int(sys.stdin.readline())

array = []
# 배열 내에 들어갈 숫자 입력
for _ in range(n) :
    num = int(sys.stdin.readline().rstrip())
    array.append(num)

# 내림차순 정렬
array.sort(reverse=True)

# 공백을 기준으로 차례대로 숫자 출력
for num in array :
    print(num, end=' ')