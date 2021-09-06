import sys

n = int(sys.stdin.readline()) # 배열 갯수 입력
arr = list(map(int, sys.stdin.readline().split())) # 배열 내의 원소 입력
ans = list(set(arr)) # 중복을 제거한 원소들만을 남김(집합 이용)
ans.sort() # 오름차순 정렬
print(*ans) # 정답 출력