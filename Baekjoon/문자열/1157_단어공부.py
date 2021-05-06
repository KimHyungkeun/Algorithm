s = input()
lists = list(s) # 편의를 위해 문자열을 리스트형태로 만듦

for i in range(len(s)) :
    if ord(lists[i]) >= 97 : # 편의를 위해 모든 알파벳을 소문자로 만든다
        lower = ord(lists[i]) - 32
        lists[i] = chr(lower)

my_dict = {}

for i in range(len(s)) :
    if lists[i] in my_dict :
        my_dict[lists[i]] += 1 # 해당 알파벳이 존재하면 그 횟수를 늘려준다
    else :
        my_dict[lists[i]] = 1 


new_dict = sorted(my_dict.items(), key = lambda x : x[1], reverse=True) # 많이 나온 횟수를 우선 찾기위해, 내림차순 정렬
# print(new_dict)

if len(new_dict) >= 2 : # 알파벳 종류가 2개이상일 경우
    if new_dict[0][1] == new_dict[1][1] : # 최댓값이 중복되는경우가 생기면 "?"를 출력
        print("?")

    else :
        print(new_dict[0][0]) # 그렇지 않다면 최댓값을 가지는 알파벳 출력

else :
     print(new_dict[0][0]) # 단일상태일때는 그 알파벳만을 출력

