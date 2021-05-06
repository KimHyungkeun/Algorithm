import sys

# 2007년의 1월 ~ 12월까지의 일수
month = [31,28,31,30,31,30,31,31,30,31,30,31]
# 월 ~ 일요일
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int, sys.stdin.readline().split())

# 지나간 일수
elapse_day = 0
# 인덱싱을 위해, 입력된 값에서 각각 1씩 감소한 값으로 계산한다
for i in range(x-1) :
    elapse_day += month[i]
elapse_day += (y-1)

# 지나간 일수를 일주일 단위로 나누었을때, 해당 요일을 구할 수 있다.
result = elapse_day % 7
print(day[result])