def solution(s):

    p = 0
    y = 0
    
    # 문자열 내에서 p와 y의 갯수를 구해서, 갯수가 같으면 True를 아니면 False를 출력
    for w in s :
        if w == 'p' or w == 'P':
            p += 1
        elif w == 'y' or w == 'Y':
            y += 1
    
    if p == y :
        return True
    else :
        return False

# https://programmers.co.kr/learn/courses/30/lessons/12916