s = input()

lists = s.split(" ") # 공백 기준으로 나눔

i = 0
while i < len(lists) :
    if lists[i] == '' : # 불필요한 공백을 발견할 경우 제거
        del lists[i]
        i = 0
    
    else :
        i += 1

print(len(lists))