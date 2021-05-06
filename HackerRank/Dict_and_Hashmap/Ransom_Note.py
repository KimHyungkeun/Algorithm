# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    word_dict = {} # 단어의 출현빈도수를 저장하기위한 dict
    
    # magazine 내에서 해당 단어의 등장 빈도수를 계산한다
    for w in magazine :
        if w in word_dict :
            word_dict[w] += 1
        else :
            word_dict[w] = 1
    
    # note에 담긴 단어들을 하나하나 비교한다
    while note :
        keyword = note[-1]
        # print(keyword)

        # 만약 해당 단어가 magazine내에 있을때
        if keyword in magazine :
            # magazine에서 발췌가능한 횟수를 모두 사용한 경우 루프문을 탈출한다 
            if word_dict[keyword] == 0 :
                break
            # 발췌할때마다, 해당 단어의 가능횟수를 1씩 줄인다
            else :
                word_dict[keyword] -= 1    
                note.pop() # 검색이 끝난 단어는 제외한다
        # 해당 단어가 magazine내에 존재하지 않으면 바로 루프문을 탈출한다
        else :
            break      
    
    # note가 비었다는 것은, 정상적으로 모든 단어를 magazine에서 발췌했다는 뜻이다.
    if not note :
        print("Yes")
    else :
        print("No")