import sys


string = sys.stdin.readline().rstrip()

# 해당 수식의 최솟값을 만들기위해서는 "+"를 먼저 처리하고, "-"를 후반에 계산한다

# 맨 먼저 "-" 를 기준으로 나눈다. ("+" 계산을 먼저 하기 위함)
first_split = string.split("-")
final_result = []

# "+" 계산을 먼저 진행한다
for f in first_split :
    result = f.split("+")
    total = 0
    for r in result :
        total += int(r)
    final_result.append(total)

# 만약, 계산에 필요한 수가 하나밖에 없다면 그 수가 최종 값이다
if len(final_result) == 1 :
    print(final_result[0])

# 남은 수에 대해서 전체적으로 뺄셈을 진행하고, 그 결과가 나온다면 그 값이 최종 값이다
else :
    total = final_result[0]
    for i in range(1, len(final_result)) :
        total -= final_result[i]
    print(total)
