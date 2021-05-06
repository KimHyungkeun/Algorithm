num = int(input())

count = 0
for _ in range(num) :
    flag = False # 그룹 단어인지 여부를 판단하기위한 플래그
    alpha_dict = [] # 알파벳 종류들을 담는 리스트
    indexes = [] # 해당알파벳이 위치한 인덱스를 담는 리스트

    string = input() # 입력

    if flag : # 만약 그룹단어가 아니면 다음 단계로 넘어감
        continue

    for word in string :
        if word not in alpha_dict :
            alpha_dict.append(word) # 모든 알파벳 종류들을 모음
    
    for w in alpha_dict :
        for i in range(len(string)) : 
            if string[i] == w : # 해당 알파벳이 출현한 인덱스들을 모두 모음
                indexes.append(i)

    for i in range(len(indexes)-1) :
        if indexes[i] - indexes[i+1] != -1 : # 만약 하나라도 멀리 떨어진 인덱스 순서가 발견되면
            flag = True # 그 즉시 루프문 탈출
            break
    
    if not flag :
        count += 1 # 전부 그룹된 단어일 경우일때는 횟수 증가

print(count)



