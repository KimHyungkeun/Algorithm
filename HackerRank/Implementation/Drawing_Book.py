#
# Complete the pageCount function below.
#
def pageCount(n, p):
    up_turn = 0 # 처음페이지에서 한장씩 넘길때의 횟수
    down_turn = 0 # 마지막페이지에서 뒤로 한장씩 넘길때의 횟수
    
    # 처음페이지 순서
    for i in range(0,n+1,2) :
        page = [i, i+1] # 현재에서의 책페이지
        if p in page : # 만약 찾는 페이지가 존재한다면 루프문 탈출
            break
        
        # 찾지 못하면 페이지를 넘김
        else :
            up_turn += 1
    
    # 마지막페이지에서 역순서
    for i in range(n,-1,-2) :
        # 먄약 n이 짝수라면, i쪽, i+1쪽 순서
        if n % 2 == 0 :
            page = [i, i+1]
        # 만약 n이 홀수라면, i-1쪽, i쪽 순서
        else :
            page = [i-1, i]
        
        # 찾는 페이지가 존재한다면 루프문 탈출
        if p in page :
            break

        # 찾지 못하면 페이지를 넘김
        else :
            down_turn += 1
    
    # 정순, 역순 경우를 모두 따져 가장 적게 걸린 횟수를 답으로 정함
    return min(up_turn, down_turn)