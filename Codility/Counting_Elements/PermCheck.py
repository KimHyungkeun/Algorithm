def solution(A):
    # write your code in Python 3.6

    # 가장 큰 수 maximum를 골라내어, 1~maximum을 차례로 모아놓는다
    maximum = max(A)
    num_dict = {}

    # 각 숫자의 출현 횟수를 기록한다
    for i in range(len(A)) :
        num_dict[i+1] = 1
    
    # 만약 해당 숫자를 탐색했다면, 그 해당 숫자의 출현횟수는 0이 된다
    for n in A :
        num_dict[n] = 0
    
    # 출현횟수가 하나라도 남아있는 경우라면 완전한 permutation이 아니므로 0을 리턴한다
    for key,val in num_dict.items() :
        if num_dict[key] == 1 :
            return 0
    
    # 완전한 permutation이면 1을 리턴
    return 1
