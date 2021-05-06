# Complete the findDigits function below.
def findDigits(n):

    int_n = n # 정수타입의 n을 저장하기위한 변수
    n = str(n) # n을 str 타입으로 만든 후, 철자 하나하나를 쪼개서 리스트에 담는다
    n = list(n)
    
    cnt = 0
    for num in n :
        # 0으로는 나눌수 없으므로 카운트에서 제외한다
        if int(num) == 0 :
            continue
        # num을 n으로 나누어서 나누어떨어졌을때 카운트를 증가시킨다
        elif int_n % int(num) == 0 :
            cnt += 1
        else :
            continue
    
    return cnt