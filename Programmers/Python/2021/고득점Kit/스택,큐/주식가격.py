from collections import deque
def solution(prices):
    answer = []

    q = deque(prices) # price를 큐로 생성

    while q :
        num = q.popleft() # 맨 앞의 price부터 하나씩 비교
        cnt = 0
        for n in q :
            if num <= n : # 현 가격과 같거나 오른경우에는 cnt 추가
                cnt += 1
            else :
                cnt += 1 # 떨어진 경우는 cnt를 1 추가 후 루프문 탈출
                break

        answer.append(cnt)

    # print(answer)
    return answer

prices = [1, 2, 3, 2, 3]
solution(prices)