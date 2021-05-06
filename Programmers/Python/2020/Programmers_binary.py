def solution(n):
    answer = 0
    
    count = 0
    list_s = []
    
    tmp = n
    while True :
        # print(n)
        if n == 1 :
            list_s.append(1)
            break
        
        remain = n % 2
        if remain == 1 :
            count += 1
        list_s.append(remain)
        n = int(n / 2)
    

    # print(list_s)

    i = 1
    while True :    
        answer = tmp + i
        real_tmp = answer
        next_count = 0
        next_list = []

        # print(tmp)
        while True :
            if answer == 1 :
                list_s.append(1)
                break

            remain = answer % 2
            if remain == 1 :
                next_count += 1

            next_list.append(remain)
            answer = int(answer / 2)
        
        if count == next_count :
            answer = real_tmp
            break

        i += 1

    # print(answer)
    return answer

solution(15)