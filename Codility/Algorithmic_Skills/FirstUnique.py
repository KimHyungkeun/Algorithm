def solution(A):
    # write your code in Python 3.6
    num_dict = {}
    for a in A :
        if a in num_dict :
            num_dict[a] += 1
        else :
            num_dict[a] = 1
    
    for key in num_dict.keys() :
        if num_dict[key] == 1 :
            return key
    
    return -1