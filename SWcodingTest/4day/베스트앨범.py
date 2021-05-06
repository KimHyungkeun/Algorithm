def solution(genres, plays):
    
    plays_num = [] # 고유번호를 같이 표기하기 위한 plays 배열
    play_dict = {} # 음반 재생목록을 담기 위한 dict
    total_play = {} # 총 재생수만을 담기 위한 dict
    
    # 수록곡과 고유번호를 같이 표기
    for i in range(len(plays)) :
        plays_num.append((plays[i], i))
    
    # 장르를 기준으로 plays를 분류함
    for i in range (len(genres)) :
        if genres[i] in play_dict :
            play_dict[genres[i]].append(plays_num[i])
        else :
            play_dict[genres[i]] = [plays_num[i]]
    
    # print(play_dict)
    # genre_num = 0

    # 가장 많이 플레이한 횟수를 먼저 수록하므로 내림차순 정렬
    for key,val in play_dict.items() :
        play_dict[key].sort(reverse=True)
        total_play[key] = 0 # 장르의 총 play수를 기준으로 key를 내림차순 정렬하기 위함
        # genre_num += 1
    
    # play_dict의 key를 내림차순정렬하기위해, 각 장르별 총 play수만을 모아 놓음
    for key,val in play_dict.items() :
        for i in range(len(play_dict[key])) :
            total_play[key] += play_dict[key][i][0]
    
    # print(total_play)
    sorted_total_play = sorted(total_play.items(), key = lambda x : x[1], reverse=True)
    # print(sorted_total_play)

    answer = []
    for w in sorted_total_play :
        # print(w)
        tmp = []
        i = 0
        while i != 2 : # 각 장르별로 2곡씩까지만 담음
            if play_dict[w[0]] :
                tmp.append(play_dict[w[0]][0])
                del play_dict[w[0]][0]
            else :
                break
            i += 1
        if len(tmp) == 2 : # 만약 재생수가 같은 음반이 2개있으면 오름차순 정렬
            if tmp[0][0] == tmp[1][0] :
                tmp.sort()
        # 장르에 있는 play가 하나밖에 없다면, 그 하나만 넣어도 된다
        answer.append(tmp)  
 
    
    # print(answer)

    tracks = []
    # 각 장르별 선택한 수록곡을 넣음
    for i in range(len(answer)) :
        for j in range(len(answer[i])) :
            tracks.append(answer[i][j][1])
    
    # print(tracks)
    return tracks

    

# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
genres = ["classic"]
plays = [500]
solution(genres, plays)