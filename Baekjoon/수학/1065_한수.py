n = int(input()) 

def hansu(n) :
    count = 0
    for i in range(1,n+1) :
        str_num = str(i) # 입력한 수를 임시로 string으로 캐스팅
        flag = True # 한수인지 아닌지를 확인하기 위한 플래그
        
        if len(str_num) <= 1 :
                count += 1 # 만약 1자리 수면, 그 자체로 한수이므로 count를 증가
                continue
        else :
            diff = int(str_num[0]) - int(str_num[1]) # 각 자리수의 차를 구한다. (각 자리수마다의 차가 diff와 모두 같다면 등차수열임)
            for j in range(len(str_num)-1) :
                if int(str_num[j]) - int(str_num[j+1]) != diff : # 각 자리수의 차가 diff와 다르면 한수가 아닌 것이다
                    flag = False
                    break
        
        if not flag : # 한수가 아니면 다음 수를 검사
            continue 
        else :
            count += 1 # 한수가 맞다면 count 증가

    return count

result = hansu(n)
print(result)
