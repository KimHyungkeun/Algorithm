def solution(distance, rocks, n) :
    rocks.sort()
    rocks.append(distance)
    left = 0
    right = distance
    # 바위 사이의 최소거리보다 거리가 작을 경우 둘 삭제
    # 거리가 클 경우, 이 값들 중 최솟값을 구해둔다
    answer = 0
    while left <= right :
        # 이전 돌
        prev = 0
        # 돌 거리 최소값
        mins = float('inf')
        # 제거한 돌 개수
        removed_rocks = 0 

        # 바위 사이의 최소 거리
        mid = (left + right) // 2
        # 각 돌을 돌면서 제거할 돌을 찾는다
        for i in range(len(rocks)) :
            if rocks[i] - prev < mid :
                removed_rocks += 1
            else :
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]
        
        # 제거한 돌 개수가 기준보다 많다 = 바위 제거를 줄여야 한다
        # 바위 사이 최소거리의 기준을 낮춰야 한다
        if removed_rocks > n :
            right = mid - 1
        
        # 제거한 돌 개수가 기준보다 적다 = 더 많은 바위를 제거해야 한다
        # 바위 사이 최소거리의 기준을 높여야 한다
        else :
            answer = mins
            left = mid + 1
    return answer

# https://m.post.naver.com/viewer/postView.nhn?volumeNo=27217004&memberNo=33264526
distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
solution(distance, rocks, n)