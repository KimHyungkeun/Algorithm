import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, input().split(' ')))
count = 0


for num in numbers :
    flag = False 

    if num < 2 : # 1이면 소수로 count 하지말고 넘어간다
        continue
    
    else :
        i = 2
        while (i <= int(num/2)) : # 만약 num이 소수가 아니라면 (num / 2)로 나눴을때 나누어 떨어지게 될것이다 
            if num % i == 0 :
                flag = True # 만약 나누어떨어지는 수가 하나라도 있다면 소수가 아니므로 바로 루프문에서 나간다
                break
            else :
                i += 1

        if not flag :
            count += 1

print(count)