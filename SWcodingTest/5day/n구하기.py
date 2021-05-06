import sys

n = int(sys.stdin.readline())

i = 1 # 1부터 하나씩 증가하는 숫자들의 합을 구한다
total = 0 # 총합

while True :
    total += i # 결과값을 저장하고
    if total > n : # 결과값이 n을 넘어서면
        break # 그때의 i가 정답이 된다
    i += 1

print(i)