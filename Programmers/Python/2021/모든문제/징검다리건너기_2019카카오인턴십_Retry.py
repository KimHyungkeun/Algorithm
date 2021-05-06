def solution(stones, k):
    left = 1 # 가장 낮은 높이의 돌
    right = max(stones) # 가장 높은 높이의 돌
    answer = 1  # 최대 건널 수 있는 인원수

    while left <= right :
        mid = (left + right) // 2 # 가장 낮은 돌과 높은 돌의 중간값을 구한다
        blank = 0 # 연속으로 공백이 발생되는 횟수
        flag = False # 공백 발생여부가 k개인지 확인하기 위한 플래그
        for stone in stones :
            if stone < mid : # 만약 해당 돌의 높이가 mid보다도 작다면 공백으로 카운트
                blank += 1
            else : # 그렇지 않으면 연속된 공백횟수가 다시 0개로 초기화
                blank = 0
            
            if blank == k : # 연속된 공백 갯수가 0이라면 탐색 종료
                flag = True
                break
        
        if flag : # 연속된 공백갯수가 k개라면 right의 최고높이를 mid높이-1 로 지정
            right = mid-1
        else : # 그렇지 않다면, 건널수 있는 현재 최대 인원수와 mid높이를 비교해서 큰값을 최대 인원수로 설정한다
            answer = max(answer, mid)
            left = mid+1 # 가장 낮은 높이의 돌을 mid+1로 지정한다
            
        print(mid)
    # print(answer)
    return answer
# https://jjangsungwon.tistory.com/109


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
# def check(mid, stones, k) :
#     ck = 0
#     for i in stones :
#         if i - mid <= 0 :
#             ck += 1
#         else :
#             ck = 0
#         if ck >= k :
#             return True
#     return False

# def solution(stones, k):

#     left = 1
#     right = 200000000
#     while left < right-1 :
#         mid = (left + right) // 2
#         if check(mid, stones, k) :
#             right = mid
#         else :
#             left = mid
#         print(left, right)
            
#     return right

# # 참고 https://hazung.tistory.com/105

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
solution(stones, k)