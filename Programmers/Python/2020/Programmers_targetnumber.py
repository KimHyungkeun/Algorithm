def solution(numbers, target) :
    answer_list=[0]
    for i in numbers :
        temporary_list = []
        for j in answer_list :
            temporary_list.append(j+1)
            temporary_list.append(j-1)
        answer_list=temporary_list
        print(answer_list)
    answer = answer_list.count(target)
    return answer 

numbers = [1,1,1,1,1]
target = 3
solution(numbers, target)