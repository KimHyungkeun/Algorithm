from collections import OrderedDict
def solution(money):
    # 털 집이 없으면 0원
    if not money :
        return 0
    # 털 집이 2개이하이면 가장 돈 많은 집
    if len(money) <= 2 :
        return max(money)
    
    # 순서정렬된 딕셔너리를 사용
    dp1 = OrderedDict()
    dp2 = OrderedDict()
    
    # 첫번째 집을 방문하고, 마지막 집은 방문하지 않는 경우
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money)-1) :
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    # 첫번째 집을 스킵하고, 마지막 집은 방문하는 경우
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)) :
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        
    return max(dp1.popitem()[1], dp2.popitem()[1])

# 참고 : https://velog.io/@imacoolgirlyo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%84%EB%91%91%EC%A7%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC