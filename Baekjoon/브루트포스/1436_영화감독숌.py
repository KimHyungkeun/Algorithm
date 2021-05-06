import sys

# n번째 시리즈
n = int(sys.stdin.readline())
series = 666 # 첫 시리즈는 666부터 시작

# 해당 시즌에 맞는 666 시리즈를 찾는다
while n != 0 :
    if '666' in str(series) : 
        n -= 1

    series += 1

print(series-1)
