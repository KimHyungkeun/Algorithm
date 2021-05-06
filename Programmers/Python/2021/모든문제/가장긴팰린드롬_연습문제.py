# 210428
def is_palin(word) : # 팰린드롬인지 여부 확인   
    return word == word[::-1]
    

def solution(s):
    maximum = 0
    for i in range(len(s)) :
        for j in range(i, len(s)+1) :
            # i부터 j번째까지의 부분문자열에 대해서, 팰린드롬인지 확인
            word = s[i:j]
            if is_palin(word) :
                # 만약 해당 부분문자열의 길이가 maximum보다도 크면, 새로 갱신한다
                if maximum < len(word) :
                    maximum = len(word)
    return maximum

# 210427
# def check_palin(string):

#     return string == string[::-1]

# def solution(s):
#     answer = 0
#     length = len(s)
#     max_v = -1
#     for i in range(length):
#         for j in range(i,length+1):
#             if check_palin(s[i:j]):
#                 if max_v < len(s[i:j]):
#                     max_v = len(s[i:j])
#     return max_v


# 틀린 답
# def is_palin(word) :
#     is_palindrome = True  # 회문 판별값을 저장할 변수, 초깃값은 True
#     for i in range(len(word) // 2): # 0부터 문자열 길이의 절반만큼 반복
#         if word[i] != word[-1 - i]:# 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
#             is_palindrome = False # 회문이 아님
#             break
    
#     return is_palindrome

# def solution(s):
#     maximum = 0
    
#     length = len(s)
#     left = 0
#     right = 1
    
#     while left < length and right <= length :
#         word = s[left:right+1]
#         # print(word)
        
#         is_palindrome = is_palin(word)
        
#         if is_palindrome :
#             while right <= length :
#                 right += 1
#                 word = s[left:right+1]
#                 if not is_palin(word) :
#                     right -= 1
#                     word = s[left:right+1]
#                     break
                
#             left += 1
#             if maximum < len(word) :
#                 maximum = len(word)
#         else :
#             right += 1
        
    

#     return maximum