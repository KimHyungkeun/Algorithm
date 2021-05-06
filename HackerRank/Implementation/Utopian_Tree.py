# Complete the utopianTree function below.
def utopianTree(n):
    height = 0 # 나무의 높이

    # 0부터 n까지의 성장 주기
    for i in range(n+1) : 
        if i == 0 : # 첫번째 시즌에서는 나무가 1만큼 자란다
            height += 1
        
        # 홀수 주기의 경우에는 나무가 2배로 자란다
        elif i % 2 == 1 :
            height *= 2
        
        # 짝수 주기의 경우에는 나무가 1만큼 자란다
        else :
            height += 1
    
    return height