# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    cnt = 0 # 카프리카 수를 확인할때마다 증가하는 카운트

    for i in range(p, q+1) :
        num = str(i**2) # 해당 수를 제곱
        result = [] # 제곱한 수를 두 부분으로 나누어서 더한값을 저장하는 리스트
        mid = len(num)//2 # 해당 수의 가운데 부분

        if len(num) == 1 : # 결과가 1~9 사이일때는, 해당 수만 넣음
            result.append(int(num))
        
        else :
            # 해당 결과 수의 길이가 홀수일때
            if len(num) % 2 == 1 :

                # 두 수를 배분하고, 두 수가 모두 양수일때 더한값을 result에 포함
                # 1) 길이가 n, n+1 형태
                a = int(num[:mid])
                b = int(num[mid:])
                if a > 0 and b > 0 :
                    result.append(a+b)
                
                # 2) 길이가 n+1, n 형태
                a = int(num[:mid+1])
                b = int(num[mid+1:])
                if a > 0 and b > 0 :
                    result.append(a+b)

            # 해당 결과 수의 길이가 짝수일때
            else :
                # 두 수를 배분하고, 두 수가 모두 양수일때 더한값을 result에 포함
                a = int(num[:mid])
                b = int(num[mid:])
                if a > 0 and b > 0 :
                    result.append(a+b)
        
        # 현재 i가 카프리카 수라면 cnt를 추가하고, i를 출력
        if i in result :
            cnt += 1
            print(i, end=" ")

    # 어떠한 카프리카수도 나오지 않으면 INVALID RANGE 출력
    if cnt == 0 :
        print("INVALID RANGE")
p = 400
q = 700 
kaprekarNumbers(p, q)