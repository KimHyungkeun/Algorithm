import sys

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

first = a1 * a2 # 맨 첫번째 항끼리 곱한다
middle = a1*b2 + a2*b1 # 서로 교차하며 곱한것을 더한다
end = - (b1 * b2) # 맨 뒷번째 항끼리 곱한다. i^2 = -1이 되므로 -1을 곱한다

if middle == 0 : # 허수가 존재하진 않으면 first와 end만을 더함
    print(first + end)

else :
    if middle < 0 : # middle 계수부분이 음수일때
        result = " - " + str(abs(middle)) + "i"
    elif middle > 0 : # middle 계수부분이 양수일때
        result = " + " + str(abs(middle)) + "i"

    print(str(first + end) + result)

# https://level.goorm.io/exam/43153/%EB%B3%B5%EC%86%8C%EC%88%98%EC%9D%98-%EA%B3%B1%EC%85%88/quiz/1