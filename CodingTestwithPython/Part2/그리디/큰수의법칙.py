import sys

# 배열크기 n, 숫자더해지는 횟수 m, 반복허용횟수 k
n, m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 배열에서 가장 큰수와, 두번째로 큰 수만 골라낸다
sel1 = max(arr) 
arr.remove(max(arr))
sel2 = max(arr)
arr.remove(max(arr))

# print(sel1, sel2)

cnt = 0 # 반복허용횟수를 k까지 허용
summary = 0
flag = True

for _ in range(m) :
    if flag : # 기본적으로는 가장 큰수를 계속 더한다
        summary += sel1
        cnt += 1
    else : # 만약 반복허용횟수가 다 채워졌다면, 두번째로 큰 수를 한번 더한다
        summary += sel2
        cnt = 0
        flag = not flag
    
    if cnt == k : # 만약 k번까지 진행했다면, 그 수의 덧셈을 중지한다
        flag = not flag
        cnt = 0

print(summary)

# ----------------------------------------------------------------------------------------
# 답안

# # N, M, K를 공백을 기준으로 구분하여 입력 받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백을 기준으로 구분하여 입력 받기
# data = list(map(int, input().split()))

# data.sort() # 입력 받은 수들 정렬하기
# first = data[n - 1] # 가장 큰 수
# second = data[n - 2] # 두 번째로 큰 수

# # 가장 큰 수가 더해지는 횟수 계산
# count = int(m / (k + 1)) * k
# count += m % (k + 1)

# result = 0
# result += (count) * first # 가장 큰 수 더하기
# result += (m - count) * second # 두 번째로 큰 수 더하기

# print(result) # 최종 답안 출력