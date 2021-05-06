def solution(A):
    # write your code in Python 3.6

    # dict 자료형으로 만든다면, 중복되는 key가 발생되지 않으므로 각각의 고유한 수를 저장할 수 있다
    answer = {}
    for a in A :
        answer[a] = 1
    
    return len(answer)