import sys

# 문서와 찾을 단어를 입력, 문자열(str) 형태로 변환
doc = sys.stdin.readline().split()
word = sys.stdin.readline().split()
doc = ''.join(doc)
word = ''.join(word)

cnt = 0 # 찾은 횟수

# 문서를 하나하나 살펴, 해당 단어가 있는지 검색
i = 0
while i < len(doc) :
    flag = True
    
    # 찾을 단어의 앞자리가 문서상에 존재하면, 탐색을 시도한다.
    # 단, 찾을 단어의 철자를 하나하나 검색시에, 문서의 최대길이를 초과해서는 안된다. 
    if doc[i] == word[0] and i+len(word) < len(doc)+1:
        
        for j in range(len(word)) :
            # 만약 토시하나라도 틀리면, 다른 단어로 간주하고 검색 취소
            if word[j] != doc[i+j] :
                flag = False
                break
        
        # 단어를 찾으면 그다음 전체문서의 부분문자열을 검색
        if flag :
            i += (j+1)
            cnt += 1
        
        else :
            i += 1

    # 단서가 주어지지 않으면 다음 문서의 철자로 넘어간다
    else :
        i += 1

# 찾은 총 횟수
print(cnt)

