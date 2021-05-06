n = int(input()) # 설탕무게 입력, 3x + 5y = n

x = 0
flag = False
maximum = int(n / 3) # n을 3으로 나누어서, x에 들어갈 입력 최대횟수를 구함.

while x <= maximum :
    if (3*x - n) % -5 == 0 : 
        y = int((3*x - n) / -5) # 0부터 차례대로 값을 대입하여 y값을 구한다.
        if y < 0 : # 해를 구했으나 음수인 경우 다음 값을 찾아본다
            continue

        else :
            flag = True # 해를 찾으면 루프문 탈출
            break

    else :
        x += 1 # 마땅한 해를 구하지 못하면 x값을 증가

if flag :
    print(x+y) # 최소갯수로 채울 수 있는 설탕

else :
    print(-1) # 적정값을 못 찾을시 -1 출력