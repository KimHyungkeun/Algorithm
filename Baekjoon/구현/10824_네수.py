import sys

a,b,c,d = sys.stdin.readline().split()

# a,b를 이어 붙인 수와 c,d를 이어 붙인 수의 합을 구한다
answer = int(a+b) + int(c+d)
print(answer)