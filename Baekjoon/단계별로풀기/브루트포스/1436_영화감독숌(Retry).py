import sys

n = int(sys.stdin.readline())
series = 666

# series 자릿수에 연속된 '666'이 있을 경우 n을 1씩 차감한다.
# 그리고 n이 0일될때까지는 series는 계속 증가한다
# 즉, series는 '666'이 포함되며, n번째로 작은 수가 되어야한다
while n :
    if '666' in str(series) :
        n -= 1
    series += 1

print(series-1)
