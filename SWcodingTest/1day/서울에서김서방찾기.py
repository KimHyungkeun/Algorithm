def solution(seoul):

    # seoul 배열 내에 Kim이 있다면, 김서방은 i번째에 있다는 글을 출력하면 된다
    answer = ''
    for i in range(len(seoul)) :
        if seoul[i] == 'Kim' :
            answer = '김서방은 '+str(i)+"에 있다"
            break
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12919