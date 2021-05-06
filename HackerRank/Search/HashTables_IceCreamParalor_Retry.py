# Complete the whatFlavors function below.
def whatFlavors(cost, money):

    purchase = [] # 구입한 두종류의 아이스크림을 담을 리스트
    prices = {} # 각 아이스크림별 가격을 저장

    for i in range(len(cost)) :
        prices[cost[i]] = i
    
    for i in range(len(cost)-1) :
        unit = money - cost[i] # 현재 가진 돈에서 i번째 아이스크림을 고르고 난 후, 남은 돈으로 살수있는 아이스크림을 고른다
        # 이미 고른 아이스크림과 겹치지 않으면서 남은 돈과 맞아떨어지는 경우에 purchase 리스트에 추가한다
        if unit in prices and i != prices[unit]: 
            purchase = [i+1, prices[unit]+1]
            break  
    
    # 낮은 가격을 먼저 보여야하므로 오름차순 정렬
    purchase.sort()
    print(purchase[0], purchase[1])

    