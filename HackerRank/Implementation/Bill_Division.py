# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    # 실제 내야할 금액
    actual = bill[k] 
    # 해당 금액을 청구서에서 제외
    bill.remove(actual)
    
    actual = sum(bill) // 2
    
    # 만약 b가 actual과 같다면 정상결제
    if b == actual :
        print("Bon Appetit")
    
    # 그렇지 않다면 남은 금액을 출력
    else :
        print(b-actual)