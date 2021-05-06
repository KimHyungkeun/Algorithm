import sys

string = sys.stdin.readline().rstrip()

zero_case = 0 # 연속된 문자열이 0인 경우를 찾는다
for i in range(len(string)-1) :
    if string[i] == '0' and string[i+1] == '1' : 
        zero_case += 1 # 만약 0이 아닌 1이 나오게되면, 지금까지의 출현한 0을 하나의 출현 경우로 생각한다
    
    if i+1 == len(string)-1 :
        if string[i+1] == '0' : # 마지막 번째일때, 0으로 끝나면 출현회수를 한번 더 올린다
            zero_case += 1

one_case = 0 # 연속된 문자열이 1인 경우를 찾는다
for i in range(len(string)-1) :
    if string[i] == '1' and string[i+1] == '0' :
        one_case += 1 # 만약 1이 아닌 0이 나오게 되면, 지금까지의 출현한 1을 하나의 출현 경우로 생각한다
    
    if i+1 == len(string)-1 :
        if string[i+1] == '1' : # 마지막 번째일때, 1로 끝나면 출현횟수를 한번 더 올린다
            one_case += 1

# print(zero_case, one_case)

# 0일때의 경우와 1일때의 경우를 비교하여 가장 최소의 경우를 출력
if one_case >= zero_case :
    print(zero_case)

else :
    print(one_case)