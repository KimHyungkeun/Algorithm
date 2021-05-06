def solution(n, words):
    # 플레이어 1~n까지 각각 발언한 단어들을 담을 키-값 형태의 딕셔너리 생성
    player = {i:[] for i in range(1, n+1)}
    # 맨 첫번째 사람이 말한 단어를 전체스택에 담고, 플레이어1이 말한 단어를 플레이어1 딕셔너리에 포함
    stack = [words[0]]
    player[1].append(words[0])
    
    flag = True
    for i in range(1, len(words)) :
        # 해당 플레이어가 발언한 단어롤 딕셔너리에 추가
        player[i%n+1].append(words[i])
        
        # 마지막으로 말한 단어의 철자로 시작하는 새로운 단어를 말해야한다 
        if stack[-1][-1] == words[i][0]:
            # 만약, 발언한 단어가 이미 나온 단어라면 그 사람이 탈락한다
            if words[i] not in stack :
                stack.append(words[i])
            else :
                flag = False
                break
        
        # 이전 단어의 철자로 시작하는 단어가 아니게 되면, 그 사람은 탈락하게 되고 끝말잇기를 마친다
        else :
            flag = False
            break
        
    # 탈락자 없이 모두 성공했다면 [0,0] 리턴
    if flag :
        answer = [0,0]
    # 아니라면, 탈락한 플레이어 번호와 그 플레이어가 발언한 마지막번째 순서번호를 담는다
    else :
        answer = [i%n+1, len(player[i%n+1])]
            
    # 값 리턴
    return answer