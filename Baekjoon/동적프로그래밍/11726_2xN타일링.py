import sys

n = int(sys.stdin.readline())

# 기존 case배열에 추가할 배열갯수를 지정
add = n-2
if add < 0 : # 만약 add가 0 미만이면, 굳이 추가할 필요가 없는것이다
    add = 0

cases = [1,2] + [0]*add
# i번째 경우의 수는, i-2번째 경우의 수와 i-1번째 경우의 수를 합한 값이다.
for i in range(2,n) :
    cases[i] = cases[i-2] + cases[i-1]

# 해당하는 수를 10007로 나눈 나머지값이 답이다
answer = cases[n-1] % 10007

print(answer)


