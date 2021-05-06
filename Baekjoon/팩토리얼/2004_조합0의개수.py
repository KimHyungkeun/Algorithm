n, m = input().split()
n = int(n)
m = int(m)

a = n
b = n - m
c = m

def count_2_and_5 (number) :
    count_2 = 0
    count_5 = 0

    i = 1
    while True :
        
        if 5 ** i <= number : # 뒤에서 세어서 0이 아닌 수가 나오기까지는 인수분해를 하여 2^n X 5^n  = 10^n 형태만 찾아내도록 한다. 
            count_5 += 1 # 그 중 5의 개수만 센다
            i += 1 
        
        else :
            break

    i = 1
    while True :
        
        if 2 ** i <= number : # 뒤에서 세어서 0이 아닌 수가 나오기까지는 인수분해를 하여 2^n X 5^n  = 10^n 형태만 찾아내도록 한다.
            count_2 += 1 # 그 중 2의 개수만 센다.
            i += 1 
        
        else :
            break

    answer_2 = 0
    answer_5 = 0

    for i in range(1, count_2+1) :
        answer_2 += int( number / (2 ** i) )

    for i in range(1, count_5+1) :
        answer_5 += int( number / (5 ** i) )
    
    return answer_2, answer_5


answer_a2, answer_a5 = count_2_and_5(a) # n!에서 2의 갯수와 5의 갯수를 구함
answer_b2, answer_b5 = count_2_and_5(b) # (n-m)!에서 2의 개수와 5의 갯수를 구함
answer_c2, answer_c5 = count_2_and_5(c) # m!에서 2의 개수와 5의 갯수륵 구함


answer_2 = answer_a2 - answer_b2 - answer_c2 # n!에서 2의 개수에서 (n-m)!m!의 2의 개수를 뺄셈
answer_5 = answer_a5 - answer_b5 - answer_c5 # n!에서 5의 개수에서 (n-m)!m!의 5의 개수를 뺄셈

if answer_2 <= 0 or answer_5 <= 0 : # 2와 5가 둘다 0개 이하이면 맨 끝부터 0으로 시작하는 경우가 없는 것이다
    print(0)

elif answer_2 <= answer_5 : # 2^x * 5^x 형태에서, 2의 개수가 적으면 2의 개수를 출력
    print(answer_2)

else : # 2^n * 5^n 형태에서, 5의 개수가 적으면 5의 개수를 출력
    print(answer_5) 

