def solution(A):
    # write your code in Python 3.6
    num_dict = {}


    # A가 비어있는 배열이면 1을 추가
    if not A :
        return 1

    # 해당 배열 길이의 +1이, 본래 갖고있어야할 배열의 길이가 된다
    N = len(A)+1

    # 존재유무를 딕셔너리에 넣음
    for i in range(N) :
        num_dict[i+1] = 1
    
    # 확인이 완료되었으면 0으로 표기
    for a in A :
        num_dict[a] = 0
    
    # 아직도 남아있는 수가 있다면, 그 수가 넣어야할 수이다
    for key,val in num_dict.items() :
        if val == 1 :
            return key