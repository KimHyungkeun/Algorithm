n = int(input())

count = 0

i = 1
while True :
    
    if 5 ** i <= n : # 뒤에서 세어서 0이 아닌 수가 나오기까지는 인수분해를 하여 2^n X 5^n  = 10^n 형태만 찾아낸다. 그리고, 10^n에서 n의 갯수가 0이 나오는 갯수라 보면 된다.
        count += 1 # 특히, 소인수 분해를 하였을때 5의 갯수는 2보다 적게 나오기 때문에 5의 갯수를 세어서
        i += 1 # [N/5] + [N/5^2] + [N/5^3] + ... 순서대로 더하여 구하면 된다.
    
    else :
        break

answer = 0
for i in range(1, count+1) :
    answer += int( n / (5 ** i) )

print(answer)