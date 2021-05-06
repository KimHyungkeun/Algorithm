import sys

# array에 n개의 숫자를 입력
n = int(sys.stdin.readline())
array = list(map(int , sys.stdin.readline().split()))

# 배열 내에서 각 숫자들의 등장 횟수를 구한다
num_dict = {}
for arr in array :
    if arr not in num_dict :
        num_dict[arr] = 1
    else :
        num_dict[arr] += 1

# 그 중 등장횟수가 1개인것(짝이없는것)을 골라낸다.
for key,val in num_dict.items() :
    if val == 1 :
        print(key)
        break