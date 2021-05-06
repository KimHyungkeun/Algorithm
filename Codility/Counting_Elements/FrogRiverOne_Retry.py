def solution(X, A):
    # write your code in Python 3.6

    # 1부터 X까지의 순서 체크
    num_check = [0] * X
    # 1~X까지의 총 등장횟수 누적
    total = 0
    for i in range(len(A)) :
        # 등장한 횟수는 1로 처리한다
        if num_check[A[i]-1] == 0 :
            num_check[A[i]-1] = 1
            total += 1
            # 만약 총 등장횟수가 X와 같다면 해당 인덱스 i를 반환한다
            if total == X :
                return i
    
    # 아예 건너갈수 없는 경우라면 -1을 반환한다
    return -1