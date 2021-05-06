def solution(s):
    answer = ''

    # 해당 문자열을 공백을 기준으로 나눈다
    array = s.split(" ")
    # print(array)

    # 문자열에 들어있던 숫자들을 int형으로 바꾸어서 다시 리스트에 재배치한다
    num_array = []
    for n in array :
        num_array.append(int(n))
    # print(num_array)

    # 해당 리스트에서의 최댓값, 최소값을 구한다
    maximum = max(num_array)
    minimum = min(num_array)
    
    # 최솟값, 최대값을 공백을 기준으로 나누어서 문자열로 처리한다
    answer = str(minimum) + " " + str(maximum)
    return answer