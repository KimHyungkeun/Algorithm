# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0

    # 만약 due date내로 책을 반납하면 추가요금은 0이다
    if (y2 >= y1 and m2 >= m1 and d2 >= d1) or (m2 > m1 and y2 >= y1) or (y2 > y1):
        return 0
    
    # 만약 년,월은 같으면서 due date보다 며칠 초과하면, 초과한 일당 * 15 만큼의 추가요금이 든다
    elif (y2 >= y1 and m2 >= m1 and d2 < d1) :
        return abs(d1-d2) * 15
    
    # 만약 년은 같으면서 due date보다 몇달 초과하면, 초과한 월당 * 500 만큼의 추가요금이 든다
    elif (y2 >= y1 and m2 < m1) :
        return abs(m2-m1) * 500
    
    # 몇년 이상이 초과하면, 10000원의 고정 추가요금이 든다
    else :
        return 10000