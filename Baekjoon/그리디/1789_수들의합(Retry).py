import sys

# 숫자를 입력
n = int(sys.stdin.readline())

cnt = 0 # 최대 숫자 갯수
total = 0 # 누적 합

# 1부터 세어서 하나씩 더했을때, 만약 누적합이 n을 넘어서면 
# 지금까지 세었던 숫자갯수에서 하나를 제외하면 된다
i = 1
while total <= n :
    total += i
    i += 1
    cnt += 1

print(cnt-1)
# https://chanhuiseok.github.io/posts/baek-31/