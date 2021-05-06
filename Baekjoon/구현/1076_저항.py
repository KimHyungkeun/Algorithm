import sys

# 각 색에 맞는 값을 매핑시킨다
resistance = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}

# 첫째 색, 둘째 색, 곱셈연산을 위한 색을 설정한다
first_col = sys.stdin.readline().rstrip()
sec_col = sys.stdin.readline().rstrip()
product = sys.stdin.readline().rstrip()

answer = int(str(resistance[first_col]) + str(resistance[sec_col])) * (10**resistance[product])
print(answer)    