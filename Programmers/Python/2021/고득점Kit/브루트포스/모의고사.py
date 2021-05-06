def solution(answers):
    answer = []
    
    student_1 = [1,2,3,4,5] # 학생 1의 패턴 
    student_2 = [2,1,2,3,2,4,2,5] # 학생 2의 패턴
    student_3 = [3,3,1,1,2,2,4,4,5,5] # 학생 3의 패턴

    stu_grade = [0] * 4 # 0번을 제외하고 1번부터 3번학생까지의 점수
    stu1_idx = 0 # 학생1의 초기 패턴 위치
    stu2_idx = 0 # 학생2의 초기 패턴 위치
    stu3_idx = 0 # 학생3의 초기 패턴 위치

    for i in range (len(answers)) :
        # 학생1~3의 패턴 움직임
        stu1_idx = i % len(student_1) 
        stu2_idx = i % len(student_2)
        stu3_idx = i % len(student_3)

        # 각 학생별로 정답이면 1점을 부여한다
        if answers[i] == student_1[stu1_idx] :
            stu_grade[1] += 1
        if answers[i] == student_2[stu2_idx] :
            stu_grade[2] += 1
        if answers[i] == student_3[stu3_idx] :
            stu_grade[3] += 1
    
    # print(stu_grade)
    
    # 학생들 점수를 종합하여 가장 높은 점수를 골라낸다
    top = max(stu_grade[1:])
    for i in range(1, 4) : # 가장 top 점수를 받은 학생들을 추려낸다
        if stu_grade[i] == top :
            answer.append(i)

    # print(answer)  
    return answer

# answers = [1,2,3,4,5]
answers = [1,3,2,4,2]
solution(answers)