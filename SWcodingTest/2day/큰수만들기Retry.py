# 테스트케이스 12만 통과 X
def solution(number, k):
    answer = ""
    stack = []

    stack.append(number[0])
    for i in range(1, len(number)) :
        
        while stack and stack[-1] < number[i] :
            if k > 0 :
                stack.pop()
                k -= 1
            else :
                break
 
        stack.append(number[i])

    # print(stack)
    answer = ''.join(stack)
    return answer

number  = "1"
k = 1
solution(number, k)
# -------------------------------------------------------------------------

def solution(number, k):
    answer = ""
    stack = []

    stack.append(number[0])
    for i in range(1, len(number)) :
        
        while stack and stack[-1] < number[i] and k > 0:
                stack.pop()
                k -= 1

        stack.append(number[i])

    print(stack)
    answer = ''.join(stack)
    return answer

number  = "1"
k = 1
solution(number, k)
# 참고 :  https://train-validation-test.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level-2-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 210119 정답코드
def solution(number, k) :
    box = []
    for i in number :
        while box and box[-1] < i and k > 0 :
            k -= 1
            del box[-1]
        box.append(i)
    
    if k != 0 :
        box = box[:-k]

    print(box)
    return ''.join(box)

number  = "1"
k = 1
solution(number, k)



