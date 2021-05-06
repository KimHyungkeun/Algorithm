def solution(citations):
    n = len(citations) # 논문 n개
    citations.sort() # 인용수가 적은순서대로 오름차순

    h = 0
    for i in range(citations[-1]) : # 최대 인용횟수까지를 h-index의 후보로 본다
        done = 0 # i번 이상 인용했을때
        no_done = 0 # i번 이하 인용했을때
        for j in range(n) :
            if citations[j] >= i : 
                done += 1 # i번 이상 인용
            else :
                no_done += 1 # i번 이하 인용
        
        # 인용논문이 i번 이상이고, 나머지 논문이 i번 이하 인용될때
        if done >= i and no_done <= i :
            h = i

    print(h)
    return h

citations = [3,0,6,1,5]
# citations = [10,11,12,13]
solution(citations)