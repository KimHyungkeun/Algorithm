def solution(phone_book):
    answer = []

    # 전화번호를 문자열 길이순대로 먼저 오름차순 정렬한다
    phone_book.sort(key = lambda x : len(x))
    # print(phone_book)

    # 접두어가 될 번호를 고른다
    head = phone_book[0]

    for i in range(1, len(phone_book)) :
            # print(head[:])
            # print(phone_book)
            # 만약 해당 번호의 시작이 head로 시작하면 False이다
            if head[:] == phone_book[i][:len(head)] :
                answer.append(False)  
            else :
                answer.append(True)
    
    # print(answer)

    # 하나라도 접두어로 시작하는게 있다면 False
    if False in answer :
        ans = False
    else : # 없다면 True를 반환
        ans = True

    print(ans)
    return ans

# phone_book = ["119", "97674223", "1195524421"]
# solution(phone_book)





# ----------------------------------------------

# 210121 정답코드

# def solution(phone_book):
    
#     box = []
#     for i in range(1, len(phone_book)) :
#         if phone_book[0] == phone_book[i][:len(phone_book[0])] :
#             box.append("false")
#         else :
#             box.append("true")
    
#     if "false" in box :
#         print("false")
#         answer = "false"
#     else :
#         print("true")
#         answer = "true"

#     return answer

phone_book = ["123", "5678", "5678924"]
solution(phone_book)