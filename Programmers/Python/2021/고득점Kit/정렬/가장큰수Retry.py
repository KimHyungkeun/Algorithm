def solution(numbers):
    array = list(map(str, numbers)) # 각 숫자를 문자로 표현
    # 해당 숫자를 3번씩 반복한 문자열 생성(아스키코드 순서에 의해 정렬됨), number의 원소 최댓값이 1000이므로 3자리수 이하로 맞추겠단 뜻
    array.sort(key = lambda x : x*3, reverse=True) 
    # print(array)

    answer = ''.join(array) # 숫자입력
    # print(answer)
    if int(answer) == 0 : # 만약 해당 숫자가 모두 0이면 '000' 이런식이 아닌 0 하나로 끝나야 함
        answer = '0'
    return answer

# numbers = [6,10,2]
numbers = [3, 30, 34, 5, 9]
solution(numbers)

# https://wooaoe.tistory.com/82