# 이진수로 만들기 위한 함수
def binary(n, cnt) :
    # 모든 이진수의 자릿수는 cnt 갯수만큼 지정한다
    if n == 0 :
        return '0'*cnt
    else :
        answer = []
        while n != 0 :
            answer.append(str(n%2))
            n //= 2
        
        if len(answer) < cnt :
            while len(answer) != cnt :
                answer.append('0')
        answer.reverse()
        return ''.join(answer)

def solution(n, arr1, arr2):
    answer = []
    new_arr1 = []
    new_arr2 = []
    
    # 십진수로 표현된 수들을 이진수로 변환하여 담을곳을 새로 지정한다
    for i in range(n) :
        new_arr1.append(binary(arr1[i],n))
        new_arr2.append(binary(arr2[i],n))
    
    for i in range(n) :
        tmp = ""
        # 두 arr1, arr2 배열에 대해 같은지점에 대해서 or 연산을 진행한다
        for j in range(n) :
            if new_arr1[i][j] == '0' and new_arr2[i][j] == '0' : 
                tmp += ' '
            else :
                tmp += '#'
        answer.append(tmp)
    
    return answer