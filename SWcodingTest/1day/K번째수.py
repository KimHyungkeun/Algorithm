def solution(array, commands):
    answer = []
    
    # command 내에 있는 [i,j,k]는 i부터 j번째 까지의 배열을 구해서 오름차순 정렬 후, k번째 값을 구하는 것이다
    for i in range(len(commands)) :
        tmp = []
        for j in range(commands[i][0]-1, commands[i][1]) :
            tmp.append(array[j])
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
    
    
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/42748