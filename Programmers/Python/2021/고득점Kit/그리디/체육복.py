def solution(n, lost, reserve):
    student = []

    # 일단 먼저 모든 학생들이 체육복을 1벌씩 다 가져왔다고 가정
    for i in range(1, n+1) :
        student.append([i,1])
    
    # 여벌 가지고 있는 학생이 존재하며, 체육복을 도난 당한 학생도 있다. 여벌을 가져왔으나 그것이 도난당했을수도 있다
    for i in range(len(student)) :
        if student[i][0] in reserve :
            student[i][1] += 1
        if student[i][0] in lost :
            student[i][1] -= 1
    
    # print(student)

    for i in range(len(student)) :

        # 맨 처음의 학생의 경우, 여벌이 있는 바로 뒷사람에게 빌리는것이 가능하다
        if i == 0 :
            if student[i][1] == 0 and student[i+1][1] == 2 :
                student[i][1] += 1
                student[i+1][1] -= 1
        
        # 맨 끝의 학생일 경우, 여벌이 있는 바로 앞사람에게 빌리는것이 가능하다
        elif i == len(student)-1 : 
            if student[i][1] == 0 and student[i-1][1] == 2 :
                student[i][1] += 1
                student[i-1][1] -= 1
        
        else :

            # 만약 본인 앞뒤로 여벌가진사람이 모두 존재한다면, 아무한테나 한명 빌린다. 
            if student[i][1] == 0 and student[i-1][1] == 2 and student[i+1][1] == 2 :
                student[i][1] += 1
                student[i-1][1] -= 1
            
            # 만약 앞사람만 여벌을 가지고 있다면, 그 사람한테 빌린다
            elif student[i][1] == 0 and student[i-1][1] == 2 : 
                student[i][1] += 1
                student[i-1][1] -= 1
            
            # 만약 뒷사람만 여벌을 가지고 있다면, 그 사람한테 빌린다
            elif student[i][1] == 0 and student[i+1][1] == 2 : 
                student[i][1] += 1
                student[i+1][1] -= 1

    cnt = 0

    # 체육복을 1벌이상은 가지고 있는 사람만 수업 참여 가능
    for w in student :
        if w[1] >= 1 :
            cnt += 1
    # print(cnt)
    return cnt

n = 5
lost = [2,4]
reserve = [1,3,5]
solution(n, lost, reserve)