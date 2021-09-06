import sys

# 카드 갯수 n개와 카드 종류를 담은 card_n 리스트
n = int(sys.stdin.readline())
card_n = list(map(int, sys.stdin.readline().split()))
card_n.sort()

# 카드 갯수 m개와 카드 종류를 담은 card_m 리스트
m = int(sys.stdin.readline()) 
card_m = list(map(int, sys.stdin.readline().split()))

# 존재여부를 판단해 주는 리스트
answer = [0 for _ in range(m)]

# 카드의 존재여부를 이분탐색으로 검색
def binary_search(val) :
    start = 0
    end = n-1
    
    while start <= end :
        mid = (start + end) // 2

        if val == card_n[mid] :
            return True
        
        elif val >= card_n[mid] :
            start = mid + 1
        
        elif val < card_n[mid] :
            end = mid - 1
        
        else :
            return False

# 카드가 존재하면 1이라고 표시
for i in range (m) :
    if binary_search(card_m[i]) :
        answer[i] = 1
    
# 정답 출력
print(*answer)