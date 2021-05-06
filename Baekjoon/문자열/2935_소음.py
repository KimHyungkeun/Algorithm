import sys

# 두 수 a, b를 입력하고 연산자 calc를 결정한다
a = list(sys.stdin.readline().rstrip())
calc = sys.stdin.readline().rstrip()
b = list(sys.stdin.readline().rstrip())

# print(a,b)

# 만약 곱하기일 경우
if calc == '*' :
    # a와 b에서 0의 갯수를 각각 구하고
    zero_cnt = a.count('0') + b.count('0')
    # print(zero_cnt)
    
    # 1 뒷쪽에 zero_cnt만큼의 0을 추가로 덧붙인다 
    arr = ['1'] + ['0']*zero_cnt
    print(''.join(arr))

else :
    # 만약 두 수가 같은 경우면, 그대로 덧셈을 실시한다
    if ''.join(a) == ''.join(b) :
        tmp = a
        tmp[0] = '2'
        print(''.join(tmp))
    else :
        # b의 길이가 더 작은 경우, a의 역순을 기준으로 'b의길이' 순서째의 숫자에 1을 넣는다 
        if len(a) > len(b) :
            a[-len(b)] = b[0]
            print(''.join(a))
        # a의 길이가 더 작은 경우, b의 역순을 기준으로 'a의길이' 순서째의 숫자에 1을 넣는다
        else :
            b[-len(a)] = a[0]
            print(''.join(b))