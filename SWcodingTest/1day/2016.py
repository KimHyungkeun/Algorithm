import calendar

def solution(a, b):
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    
    # 2016년의 a월 b일의 요일을 구한다
    answer = calendar.weekday(2016, a, b)
    print(days[answer])
    return days[answer]

solution(1,18)