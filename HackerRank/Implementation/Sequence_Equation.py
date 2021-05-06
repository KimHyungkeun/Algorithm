# Complete the permutationEquation function below.
def permutationEquation(p):

    # 해당 인덱스위치를 저장하기위한 리스트
    idx = []
    # p를 1~N까지 오름차순정렬시킨 리스트
    sorted_p = sorted(p)

    # 정렬된 p에서의 i번째 위치가, 기본 p에서는 어느 위치에 있는지 확인한다
    for i in range(len(sorted_p)) :
        idx.append(p.index(sorted_p[i])+1)
    

    # 현재 저장된 인덱스+1 의 값이, p 리스트에서 어느 위치에 존재하는지를 answer 리스트에 저장한다
    answer = []
    for a in idx :
        answer.append(p.index(a)+1)
        

    return answer