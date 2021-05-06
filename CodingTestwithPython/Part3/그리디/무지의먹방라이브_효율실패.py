# def find_not_zero(i, length, food_times) : # 다음 음식까지 세야함

#     while food_times[i % length] == 0 :
#         if sum(food_times) == 0 : # 만약 모든 음식을 다 먹었다면 종료
#             break
#         i += 1 # 다음 음식을 찾을때까지 돌림판을 돌림

#     if i >= length : # 해당 인덱스가 음식길이를 벗어나면 다시 1번째부터 돌아와야하므로, 나머지연산
#         i %= length

#     return i

# def solution(food_times, k):
#     answer = 0

#     length = len(food_times) # food_times 길이
#     pos = 0 # 음식 위치
#     sec = 0 # 걸린 시간

#     while sum(food_times) != 0 :
#         pos %= length # 위치
#         # print(food_times, sec)

#         if sec == k : # 네트워크가 끊겼다면 
#             pos = find_not_zero(pos, length, food_times)
#             answer = pos+1 # 다음 먹어야할 차례의 위치를 기억한다
#             break
        
#         pos = find_not_zero(pos, length, food_times) # 다음 먹어야할 음식위치까지 찾아냄
        
#         if sum(food_times) != 0 :
#             food_times[pos] -= 1 # 음식을 하나 먹은 후에는 초가 증가
#             sec += 1   
        
#         pos += 1
    
#     if sum(food_times) == 0 : # 만약 모두 먹었다면 -1 출력
#         answer = -1
    
#     print(answer)
#     return answer

# -----------------------------------------------------------------------------

# 정답 코드
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

# food_times = [3,1,2]
# k = 5

# food_times=[4,2,3,6,7,1,5,8] 
# k=16

# food_times=[4,2,3,6,7,1,5,8] 
# k=27

food_times=[1,1,1,1]
k=4

solution(food_times, k)