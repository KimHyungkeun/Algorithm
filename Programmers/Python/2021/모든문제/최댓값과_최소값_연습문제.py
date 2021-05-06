def solution(s):
    answer = ''
    # 문자열을 공백기준으로 나눈다
    s = s.split(" ")

    arr = []
    # arr 배열에 문자타입의 숫자를, 정수타입의 숫자로 바꾸어 집어넣는다
    for n in s :
        arr.append(int(n))
    
    # 최댓값과 최소값을 공백을 기준으로 나누어서 answer에 담는다
    answer += str(min(arr)) + " " + str(max(arr))
    return answer