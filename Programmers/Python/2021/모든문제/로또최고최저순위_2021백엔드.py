def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 6개 당첨부터 0개 당첨까지 했을 경우의 랭크를 지정한다
    
    correct = set(lottos) & set(win_nums) # lottos와 당첨번호 중 겹치는 것들을 구한다
    min_val = len(correct) # 최소 당첨 갯수는 lottos와 win_nums에 둘다 들어있는 번호의 갯수이다.
    max_val = len(correct) + lottos.count(0) # 최대 당첨 갯수는 겹치는 번호 외의 다른 번호들 까지 win_nums에 있는 경우이다. 이때, 추가되는 번호갯수는 lottos의 0의갯수다
    
    
    answer = [rank[max_val], rank[min_val]] # 최대로 잘 나온 랭크와 최소로 잘 나온 랭크를 구한다
    
    
    return answer