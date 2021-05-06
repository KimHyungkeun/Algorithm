def sortString(s) :
    
    answer = ""
    list_s = list(s)
    
    # print(list_s)
    

    while True :
        # print(len(list_s))
        # min -> max
        if len(list_s) == 0 :
            break

        list_s.sort()
        min_word = min(list_s)
        while min_word != max(list_s) :
            answer += min_word
            list_s.remove(min_word)

            for word in list_s :
                if min_word < word <= max(list_s) :
                    min_word = word
                    break

        answer += min_word
        list_s.remove(min_word)

        # max -> min
        if len(list_s) == 0 :
            break

        list_s.sort(reverse=True)
        max_word = max(list_s)
        while max_word != min(list_s) :
            answer += max_word
            list_s.remove(max_word)

            for word in list_s :
                if max_word > word >= min(list_s) :
                    max_word = word
                    break

        answer += max_word
        list_s.remove(max_word)

    # print(answer)
    return answer

s = "rat"
sortString(s)