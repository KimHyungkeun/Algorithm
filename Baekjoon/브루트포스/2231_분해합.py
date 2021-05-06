num = int(input())

for i in range(1, num+1) :
    flag = False
    summary = i # 분해합을 담을 요소
    str_i = str(i) # 자리수끼리의 셈을 위해 임의로 string 형태로 캐스팅

    for j in range(0, len(str_i)) :
        # print(str_i[j], end='')
        summary += int(str_i[j]) # 자릿수끼리 모두 더한다
    

    if summary == num : # summary가 num의 분해합이면 루프문에서 빠져나간다
        flag = True     
        break

if flag :
    print(i) # 분해합이 존재하는 경우

else :
    print(0) # 분해합이 존재하지 않으면 0 출력