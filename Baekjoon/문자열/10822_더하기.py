import sys

# 수식 입력
string = sys.stdin.readline().rstrip()
arr = string.split(",") # 콤마 단위로 숫자를 쪼갠다
arr_num = [] # 현재의 숫자들은 문자타입이므로, 숫자타입으로 바꾸기 위한 조치를 취한다

# 정수타입으로 바뀐 숫자를 배열에 넣는다
for a in arr :
    arr_num.append(int(a))

# 값 출력
print(sum(arr_num))