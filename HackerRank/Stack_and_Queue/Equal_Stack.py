def equalStacks(h1, h2, h3):
    # Write your code here
    
    # h1,h2,h3의 점차적인 높이 변화 리스트
    res_1 = [] 
    res_2 = [] 
    res_3 = []
    
    # 하나라도 스택높이가 0이면 무조건 최대높이는 0이되어버린다
    if not h1 or not h2 or not h3 :
        return 0

    
    else :
        # h1이 빌때까지, h1의 top부터 시작하여 하나씩 높이의 변화상태를 리스트에 저장한다
        while h1 :
            if not res_1 :
                res_1.append(h1.pop())
            else :
                res_1.append(h1.pop() + res_1[-1])
        
        # h2이 빌때까지, h2의 top부터 시작하여 하나씩 높이의 변화상태를 리스트에 저장한다
        while h2 :
            if not res_2 :
                res_2.append(h2.pop())
            else :
                res_2.append(h2.pop() + res_2[-1])
        
        # h3이 빌때까지, h3의 top부터 시작하여 하나씩 높이의 변화상태를 리스트에 저장한다
        while h3 :
            if not res_3 :
                res_3.append(h3.pop())
            else :
                res_3.append(h3.pop() + res_3[-1])
        
        # 세 스택의 높이가 동일해지는 순간을 저장한다
        result = list(set(res_1) & set(res_2) & set(res_3))
        # result.sort()
        # print(res_1, res_2, res_3)

        # 단 1개도 없다면 0을 리턴하고, 하나 이상 있다면 그 중 최대높이를 리턴한다
        if not result :
            return 0
        else :
            result.sort()
            return result[-1]