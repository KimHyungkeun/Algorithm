import sys

string = list(sys.stdin.readline().rstrip())

result = int(string[0]) # 맨 처음 숫자를 기준점으로 둔다
for i in range(1, len(string)) :
    num = int(string[i])
    if num <= 1 or result <= 1 : # 곱하려는 두 수 중에 아무거나 하나가 1이하이면 더하고
        result += num 
    else : # 그것이 아니라면 곱한다
        result *= num
print(result)
