import sys

# 일의자리 숫자(n)와 자동차번호가 주어진다
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 10부제는 자동차번호의 일의자리 숫자가 n과 일치하면, 일의자리가 n인 날짜때는 운행 불가
print(arr.count(n))