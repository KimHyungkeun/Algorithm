# Complete the angryProfessor function below.
def angryProfessor(k, a):
    
    cnt = 0 # 정시 내에 출석한 학생수
    for stu in range(len(a)) :
        if a[stu] <= 0 : # 정시 내에 출석했다면, 학생수를 카운트한다
            cnt += 1
    
    # k명 이상 출석하면, 수업 취소가 아니므로 "NO". 그 미만 출석하면 수업 취소가 되어 "YES"
    if cnt >= k :
        return "NO"
    
    else :
        return "YES"