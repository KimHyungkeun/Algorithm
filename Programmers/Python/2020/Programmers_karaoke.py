def solution(genres, plays):
    answer = []
    my_dict={ }
    for i in range (len(genres)) :
        if genres[i] not in my_dict :
            my_dict[genres[i]] = plays[i]
        else :
            my_dict[genres[i]] += plays[i]
    
    song_list = sorted(my_dict.items(), key = lambda x : x[1], reverse = True)
    # print(song_list)
    num_list = []
    for i in range (len(song_list)) :
        tmp_dict = {}
        for j in range (len(genres)) :
            if song_list[i][0] == genres[j] :
                tmp_dict[j] = plays[j]
        sort_tmp = sorted(tmp_dict.items(), key = lambda x : x[1], reverse = True)
        num_list.append(sort_tmp)
    # print(num_list)
    
    for i in range(len(num_list)) :
        count = 0
        for j in range(len(num_list[i])) :
            if count == 2 :
                break 
            answer.append(num_list[i][j][0])            
            count += 1
            
    return answer