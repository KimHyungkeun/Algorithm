import sys

n = int(sys.stdin.readline())

# 초기숫자 n을 설정한다
numbers = [n]

while True :
    # print(numbers)
    # 각 자릿수별에 대해 제곱을 해야하므로, 임의로 자릿수별 리스트를 만든다
    new = str(numbers[-1])
    tmp = list(new)
    # print(tmp)
    
    val = 0
    # 자릿수별 제곱을 한 값을 더한다
    for num in tmp :
        val += (int(num)**2)
    
    # 만약 1이 나오게 되면 행운의 숫자다
    if val == 1 :
        print(str(n) + " is Happy Number.")
        break
    
    # 연산 과정 중 4가 나오게되면 그 이후로는 반복되므로 행운의 숫자가 아니다
    elif val == 4 :
        print(str(n) + " is Unhappy Number.")
        break

    # 그 외의 숫자들은 계속 탐색을 시작한다
    else :
        numbers.append(val)
    # print(tmp)

# https://level.goorm.io/exam/43084/happy-number/quiz/1