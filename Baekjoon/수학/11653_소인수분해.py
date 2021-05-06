num = int(input())
n = num

i = 2
while i <= n :

    if num == 1 : # 1이라면 완전히 나누어 떨어진 경우이므로 루프문 탈출
        break

    if num % i == 0 : # i가 num을 나누어 떨어뜨릴수 있다면
        print(i) # i를 출력하고
        num = num // i # num을 다시 나눈다
    
    else :
        i += 1 # 만약 나누어 떨어뜨릴수 없다면, 다시 증가시킨다.
