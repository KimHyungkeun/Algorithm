import sys
# 1에서 n개 까지의 수에서, m개를 골라 그 리스트를 나열
n, m = map(int, sys.stdin.readline().split())
answer = [0]*m # 0으로 초기화된 answer 리스트

def recursive(index, n, m) :
    if index == m :
        # answer이 원하는 m만큼 채워졌을때 출력
        for i in range(m) :
            print(answer[i], end=' ')
        print()
        return
    
    for i in range(1, n+1) :
        # 만약 탐색되지 않았다면 해당 부분을 찾음 
        answer[index] = i # 답란에 탐색한 값을 넣음
        recursive(index+1, n, m) # 자식노드에 대해 추적시작
     

recursive(0, n, m)

# ---------------------------------------------------------------------------------
# from itertools import product # 중복순열을 구한다

# n, m = map(int, input().split())
# array = [] # 1부터 n까지의 오름차순 배열

# for i in range(1,n+1) :
#     array.append(i)

# permute = []
# for i in product(array, repeat=m) : # 중복순열 리스트
#     permute.append(i)

# for i in range(len(permute)) :
#     for j in range(m):
#         print(permute[i][j], end=' ') # 순열 목록 출력
#     print()