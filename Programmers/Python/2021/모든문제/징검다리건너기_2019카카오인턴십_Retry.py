# 정확성 (3번째 케이스 예외 발생), 효율성(모두 시간초과)
# def solution(stones, k):
#     answer = 0
    
    
#     while sum(stones) != 0 :
#         for i in range(len(stones)) :
#             if stones[i] == 0 :
#                 continue
#             stones[i] -= 1
        
#         # print(stones)
#         answer += 1
        
#         flag = False
#         for i in range(len(stones)) :         
#             if stones[i] == 0 :
#                 if i+k < len(stones) and sum(stones[i:i+k]) == 0 :
#                     flag = True
#                     break

#         if flag :
#             break           
                   
#     return answer

# 20210425
def check(mid, stones, k) :
    ck = 0
    for i in stones :
        if i - mid <= 0 :
            ck += 1
        else :
            ck = 0
        if ck >= k :
            return True
    return False

def solution(stones, k):
    answer = 0
    left = 1
    right = 200000000
    while left < right-1 :
        mid = (left + right) // 2
        if check(mid, stones, k) :
            right = mid
        else :
            left = mid
        print(left, right)
            
    return right

# 참고 https://hazung.tistory.com/105

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
solution(stones, k)