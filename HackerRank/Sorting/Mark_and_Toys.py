# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort() # 가격을 오름차순으로 정렬한다
    
    cnt = 0 # 살 수 있는 장난감의 갯수
    summary = 0 # 장난감의 총 가격
    for toy in prices :
        if summary + toy <= k : # 만약 k원 이내로 장난감 구입이 가능하다면
            summary += toy # 해당 장난감을 구입하고, 구입갯수를 증가시킨다
            cnt += 1
        else : # 더 이상 살 수 없다면 루프문을 종료한다
            break
    
    return cnt