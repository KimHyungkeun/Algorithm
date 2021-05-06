while True :
    n, m = map(int, input().split())

    if n < m :
        if m % n == 0 :
            print("factor") # n이 m의 약수라면 factor 출력

        else : print("neither") # 아무것도 아니라면 neither 출력

    elif n > m :
        if n % m == 0 :
            print("multiple") # n이 m의 배수라면 multiple 출력

        else : print("neither") # 아무것도 아니라면 neither 출력
    
    elif n == 0 and m == 0 : # 둘다 0이면 종료
        break