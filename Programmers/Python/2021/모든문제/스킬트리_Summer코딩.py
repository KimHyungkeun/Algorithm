from collections import deque

def solution(skill, skill_trees):
    # 올바른 스킬트리 갯수
    cnt = 0
    
    for i in range(len(skill_trees)) :
        # popleft()함수를 위해 덱으로 변환
        tmp = deque(skill)
        flag = True # 올바른 스킬트리인지를 확인하기 위한 플래그

        for j in range(len(skill_trees[i])) :
            # 해당 스킬트리가 스킬내에 있고, 올바른 순서로 온 경우
            if skill_trees[i][j] in tmp and skill_trees[i][j] == tmp[0] :
                tmp.popleft()
            # 해당 스킬트리가 스킬내에 있지만, 순서가 뒤바뀐 경우
            elif skill_trees[i][j] in tmp and skill_trees[i][j] != tmp[0] :
                flag = False
                break
            # 그 외의 경우는 패스한다
            else :
                continue
        
        # 올바른 스킬트리라면 cnt를 증가시킨다
        if flag :
            cnt += 1
    
    # 값 리턴
    return cnt

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]	
solution(skill, skill_trees)