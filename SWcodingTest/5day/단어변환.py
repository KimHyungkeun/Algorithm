from collections import deque
def solution(begin, target, words):
    
    if target not in words : # 해당 단어가 words에 존재하지 않을때
        # print(0)
        return 0
    
    else :
        word_dict = {}
        for w in words : # 단어별로 탐색여부를 확인한다
            word_dict[w] = 0
        queue = deque()
        queue.append((begin,0)) # 맨 첫번째를 확인

        cal_cnt = 0 # 현재 depth에서의 총 비교가능횟수
        cnt = 1 # 현재 depth에서 큐를 하나씩 제거할때마다 감소함
        depth = 1 # 탐색 깊이

        
        while queue :

            search, idx = queue.popleft() # 비교해야할 노드를 넣는다
            cnt -= 1 # 현재 depth에서 남은 비교 노드

            for i in range(len(words)) :
                diff = 0
                # 서로 다른 단어일 경우
                if search != words[i] :
                    for j in range(len(words[i])) :              
                            if search[j] != words[i][j] :
                                diff += 1

                    # print(words[i], diff)
                    
                    # 철자가 1개만 다른 경우, 해당 단어에 대한 검색 시작  
                    if diff == 1 :
                        if word_dict[words[i]] == 0 : 
                            queue.append((words[i], i))
                            word_dict[words[i]] = 1
                            cal_cnt += 1

            # print(queue)
            # print(word_dict)

            # 만약 해당 단어를 이번 depth에서 검색한 경우 루프 종료
            if word_dict[target] == 1 :
                break

            if cnt == 0 : # 현 depth의 탐색을 모두 마친 경우
                cnt = cal_cnt # 다음 depth에 대해 탐색할 모든 경우의 수를 업데이트
                cal_cnt = 0
                depth += 1 # depth도 1 추가
    
        # print(word_dict)
        

        if word_dict[target] == 0 : # words에는 있으나 변환이 불가능한 경우도 0이다
            depth = 0

        print(depth)
        return depth

begin = "hit"
target = "cog"
# words = ["hhh", "hht"]
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin, target, words)	