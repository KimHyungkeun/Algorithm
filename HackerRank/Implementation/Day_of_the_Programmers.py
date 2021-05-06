# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    # 개월당 일 수
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    # 만약 1919년 전 시기라면 율리우스 법에 따라 날짜 계산
    if year < 1919 :
        # 4로 나눌수 있다면, 해당 년은 윤년이다
        if year % 4 == 0 :
            month[1] = 29
        
        # 1918년은 1월 31일 다음이 2월 14일이다
        elif year == 1918 :
            month[1] -= 13
    
    # 그레고리 계산에 따라, 400으로 나눠지거나 4로 나눠지면서 100으로 나눠떨어지지 않는 년도가 윤년이다
    elif (((year%4==0) and (year%100!=0)) or year%400==0) :
        month[1] = 29

    # 프로그래머의 날은 그 해의 시작일로부터 256번째 날이다
    total = sum(month[:8])
    day = 256 - total
    
    # 날짜 출력
    print(day)
    return str(day)+"."+'09'+"."+str(year)