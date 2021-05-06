# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    brr_dict = {} # 해당 숫자의 빈도수를 저장하기위 한 dict
    result = [] # missing number를 저장하기 위한 리스트
    
    # brr 배열에 등장하는 숫자의 종류와 빈도수를 계산한다
    for n in brr :
        if n in brr_dict :
            brr_dict[n] += 1
        else :
            brr_dict[n] = 1
    
    # n이 brr 배열에도 등장한다면, brr배열에서 빈도수를 하나 감소시킨다
    for n in arr :
        if n in brr_dict :
            brr_dict[n] -= 1
    
    # 빈도수가 1이상 남아있는 경우가 존재한다면, 그 숫자가 missing number이다
    for key,val in brr_dict.items() :
        if val >= 1 :
            result.append(key)
    
    # 오름차순 정렬 후 리턴
    result.sort()
    return result