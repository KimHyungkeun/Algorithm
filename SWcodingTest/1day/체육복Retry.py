def solution(n, lost, reserve):
    answer = 0
    student = []
    rent = []

    # 모두 체육복이 있다고 가정한다
    for i in range(n) :
        student.append(1)

    # 여벌옷을 가진사람은 +1을 하고, 도난당한 사람은 -1을 한다. 여벌을 가져왔으나 도난당했을 가능성도 있다
    for i in range(n) :        
        if i+1 in reserve :
            student[i] += 1
        if i+1 in lost :
            student[i] -= 1
    # print(student)

    for i in range(len(student)) :
        # 여벌옷을 가지고 있거나, 그냥 가지고 있는 사람은 인원을 1증가시킨다.
        if student[i] == 1 or student[i] == 2 :
            answer += 1

        # 아무것도 가지고 있지 않을때
        else :
            # 만약 본인이 첫번째 일때
            if i == 0 :
                if student[i+1] == 2 and (i+1 not in rent): # 뒷사람에겐 이미 빌렸으므로, 대여 항목에 넣는다
                    rent.append(i+1)
                    answer += 1
            # 만약 본인이 마지막 순서일때
            elif i == len(student)-1 :
                if student[i-1] == 2 and (i-1 not in rent): # 앞사람에겐 이미 빌렸으므로, 대여 항목에 넣는다
                    rent.append(i-1)
                    answer += 1

            # 앞뒤로 여벌옷을 가진사람이 1명 이상 있을때
            else :
                # 모두다 가지고 있을 경우

                if student[i-1] == 2 and student[i+1] == 2 :
                    # 앞사람에게 빌린다
                    if i-1 not in rent :
                        answer += 1
                    # 뒷사람에게 빌린다
                    elif i+1 not in rent :
                        answer += 1
                    # 앞,뒤 모두에게 빌리는 경우 2가지이므로, 앞뒤사람 항목을 대여리스트에 넣는다
                    rent.append(i-1)
                    rent.append(i+1)
                  
                # 앞사람만 가지고 있다면, 앞사람을 넣고 인원을 1 증가 시킨다.
                elif student[i-1] == 2 and (i-1 not in rent) :
                    rent.append(i-1)
                    answer += 1
                # 뒷사람만 가지고 있다면, 뒷사람을 넣고 인원을 1 증가 시킨다.
                elif student[i+1] == 2 and (i+1 not in rent) :
                    rent.append(i+1)
                    answer += 1
    print(answer)
    return answer

n = 3
lost = [1,2]
reserve = [2,3]
solution(n, lost, reserve)

# --------------------------------------------------------

# 210119 정답코드
def solution(n, lost, reserve) :

    a = set(lost) & set(reserve)
    lost = list(set(lost) - a)
    reserve = list(set(reserve) - a)

    for i in reserve :
        if i-1 in lost :
            lost.remove(i-1)
        elif i+1 in lost :
            lost.remove(i+1)
    
    return n - lost(lost)