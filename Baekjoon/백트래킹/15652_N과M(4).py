import sys
# 1에서 n개 까지의 수에서, m개를 골라 그 리스트를 나열
n, m = map(int, sys.stdin.readline().split())
answer = [0]*m # 0으로 초기화된 answer 리스트

def recursive(index, start, n, m) :
    if index == m :
        # answer이 원하는 m만큼 채워졌을때 출력
        for i in range(m) :
            print(answer[i], end=' ')
        print()
        return
    
    for i in range(start, n+1) :
        answer[index] = i # 답란에 탐색한 값을 넣음
        recursive(index+1, i ,n, m) # 자식노드에 대해 추적시작, 중복조합은 본인도 포함하므로 i부터 추적

recursive(0, 1, n, m)
# ----------------------------------------------------------------------------------------
# from itertools import combinations_with_replacement # 중복조합을 구하기 위한 라이브러리

# n, m = map(int, input().split())
# array = []

# for i in range(1,n+1) :
#     array.append(i) # 1부터 n까지 오름차순 배열을 설정

# permute = list(combinations_with_replacement(array,m)) #  중복조합을 구함

# for i in range(len(permute)) :
#     for j in range(m):
#         print(permute[i][j], end=' ') # 조합 목록 출력
#     print()