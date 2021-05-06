def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    
    for i in range(len(skill_trees)) :
        tmp = []
        flag = 0
        
        for j in range(len(skill_trees[i])) :
            if skill_trees[i][j] in skill_list :
                tmp.append(skill_trees[i][j])

        # print(tmp)
        for k in range(len(tmp)) :
            if tmp[k] != skill_list[k] :
                flag = 1
                break
                
        if flag ==  1 :
            continue
        
        else :
            
            answer += 1
        
    # print(answer)
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)