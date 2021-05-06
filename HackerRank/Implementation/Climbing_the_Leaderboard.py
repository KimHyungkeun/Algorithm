# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     answer = []
#     not_repeat_ranked = []
#     rank_dict = []
#     rank = 1

#     for r in ranked :
#         if r not in not_repeat_ranked :
#             not_repeat_ranked.append(r)
    
#     for p in enumerate(not_repeat_ranked) :
#         rank_dict.append(p)


#     print(rank_dict)
#     for p in player : 
#         # print(p)
#         for i in range(len(rank_dict)-1, -1 ,-1) :
#             if i == len(rank_dict)-1 :
#                 if rank_dict[i][1] > p :
#                     answer.append(rank_dict[i][0]+1)
#                     break
#             elif i == 0 :
#                 if rank_dict[i][1] < p :
#                     answer.append(1)
#                     break
#                 else :
#                     answer.append(rank_dict[i+1][0])
#                     break
#             else :
#                 if rank_dict[i][1] > p :
#                     answer.append(rank_dict[i+1][0])
#                     break
   
#     # print(answer)                
#     return answer

def climbingLeaderboard(ranked, player):
    scores = sorted(list(set(ranked)), reverse=True)
    player_ranks = []
    for score in player :
        # print(scores)
        while scores and score >= scores[-1] :
            scores.pop()
        player_ranks.append(len(scores)+1)
    return player_ranks

# 참고 : https://livecodestream.dev/challenge/climbing-the-leaderboard/

# 210307 풀이
def climbingLeaderboard(ranked, player):
    
    # 해당 점수를 순위별 구간으로 나눈다
    score = sorted(list(set(ranked)), reverse=True)
    score_with_rank = []

    # 각 점수가 몇위에 해당되는지 새 리스트를 구성한다
    for i in range(len(score)) :
        score_with_rank.append((i+1, score[i]))
    
    # print(score_with_rank)
    answer = []
    for p in player :
        # 점수 p가 현 점수판의 꼴찌보다도 높다면, 점수판의 끝자락은 제외시킨다
        while score_with_rank and score_with_rank[-1][1] <= p :
            score_with_rank.pop()
        # 만약 스코어판이 비어있다면, 현 점수가 가장 1위에 있단 뜻이다
        if not score_with_rank :
            answer.append(1)
        # 그런 경우가 아니라면, 현재 존재하는 마지막순위에 +1을 한것이 p의 순위이다
        else :
            answer.append(score_with_rank[-1][0]+1)
    
    return answer

ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
climbingLeaderboard(ranked, player)