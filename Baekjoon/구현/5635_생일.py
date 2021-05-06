import sys

# 테스트 케이스 n 입력
n = int(sys.stdin.readline())

# (이름, 지나온 일수)
birthday = []
for _ in range(n) :
    # 이름, 일, 월, 년도로 입력받음
    name, day, month, year = sys.stdin.readline().split() 
    # 현재 날짜를 '일' 단위로 통합
    all_days = int(year) * 365 + int(month)*30 + int(day)
    # 배열에 추가
    birthday.append((name, all_days))

# 내림차순 정렬('일'단위가 크다면 날짜상으로는 가장 늦게 태어난것이다)
birthday.sort(key = lambda x : x[1], reverse=True)
print(birthday[0][0]) # 가장 늦게 태어난 사람
print(birthday[-1][0]) # 가장 일찍 태어난 사람