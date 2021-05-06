import sys

# 배열에 n개 숫자입력
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

mini_diff = 1000000 # 1부터 1000000까지의 수이므로 초기값은 1000000으로 설정
for i in range(len(array)-1) :
    if abs(array[i] - array[i+1]) < mini_diff :
        mini_diff = abs(array[i] - array[i+1]) # 더 작은 격차가 존재하면 그값이 최단거리가 된다

print(mini_diff)

# https://level.goorm.io/exam/43207/%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC/quiz/1