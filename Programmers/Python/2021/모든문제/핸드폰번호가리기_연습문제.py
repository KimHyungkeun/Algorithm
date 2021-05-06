def solution(phone_number):

    # 들어온 문자열 phone_number를 리스트로 바꿈
    arr = list(phone_number)
    arr.reverse() # 배열을 역순으로 정렬. 즉, 0102345678 -> 876543210이 된다

    # 5번째 숫자부터 모두 '*' 표시로 바꾼다
    for i in range(4, len(arr)) :
        arr[i] = '*'

    # 다시 역순 정렬
    arr.reverse()
    
    # 리스트에 담긴 내용을 문자열로 표기
    answer = ''.join(arr)
    return answer