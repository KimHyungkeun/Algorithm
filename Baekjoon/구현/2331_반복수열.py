import sys

# 숫자 a와 곱할 횟수 p를 설정
a, p = map(int, sys.stdin.readline().split())

# 배열 설정
array = [a]

while True :
    # array의 가장 최근 숫자를 자릿수별로 따로 나눈다
    num = str(array[-1])
    num = list(num)

    next_num = 0
    # 해당 자릿수를 각각 p번 곱한다음, 그 결과를 계속 누적시킨다
    for n in num :
        next_num += int(n)**p
    
    # 만약 해당 수가 이미 배열안에 있는 수라면 계산을 중단한다
    if next_num in array :
        break

    # 그렇지 않으면 배열에 계속 추가시킨다
    else :
        array.append(next_num)

# 반복되는 부분이 처음으로 등장했을때의 인덱스를 구하고, 그 인덱스 이전까지의 배열길이를 구한다 
idx = array.index(next_num)
print(len(array[:idx]))    
