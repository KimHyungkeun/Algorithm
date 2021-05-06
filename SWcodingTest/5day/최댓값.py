import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

maximum = max(array) # 해당 배열의 최댓값
for i in range(len(array)) :
    if array[i] == maximum : # 해당 인덱스쪽이 최댓값 위치라면
        idx = i+1 # 해당 인덱스를 반환
        break

print(maximum, idx)

# https://level.goorm.io/exam/43245/%EC%B5%9C%EB%8C%93%EA%B0%92/quiz/1