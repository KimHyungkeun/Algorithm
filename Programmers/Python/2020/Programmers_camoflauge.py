def solution(clothes):
    answer = 0
    my_dict = {}
    for i in range(len(clothes)) :
        if clothes[i][1] not in my_dict :
            my_dict[clothes[i][1]] = 1
        else :
            my_dict[clothes[i][1]] += 1
    
    print(my_dict)
    
    case_mul = 1
    for value in my_dict.values() :
        case_mul *= (value+1)
    
    answer = case_mul - 1 # -1을 하는 이유는 아무것도 안입는 경우는 없기 때문
    return answer