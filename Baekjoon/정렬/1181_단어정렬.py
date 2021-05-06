n = int(input()) # n개 단어 입력

word_list = []

for _ in range(n) :
    word = input() # 각 단어들을 모두 입력
    word_list.append(word)

del_repeat = set(word_list) # 중복 요소를 제거
sort_by_len = sorted(del_repeat, key=lambda x : len(x)) # 단어길이를 기준으로 정렬


sort_dict = {} 

# 단어 길이별로 단어들을 모음
for i in range(len(sort_by_len)) :
    if len(sort_by_len[i]) not in sort_dict : 
        sort_dict[len(sort_by_len[i])] = [sort_by_len[i]] 
    
    else :
        sort_dict[len(sort_by_len[i])].append(sort_by_len[i])

# 각 단어 길이별로, 단어들을 사전순서대로 정렬 시킴
for key, val in sort_dict.items() :
        sort_dict[key].sort()

# 정렬 완료시킨 순서대로 단어들을 차례대로 배열시킴
answer = []
for key,val in sort_dict.items() :
    for i in range(len(sort_dict[key])) :
        answer.append(sort_dict[key][i])

# 답 출력
for i in range(len(answer)) :
    print(answer[i])
