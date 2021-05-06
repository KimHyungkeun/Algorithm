# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):

    # (사탕개수 + 시작번호 - 1) 한것을 총 죄수의 인원으로 나누었을때의 나머지값을 구한다
    ans = (m+s-1) % n

    # 만약 나누어떨어지면, 현 죄수인원 중 마지막번호의 인원이 먹는다
    if ans == 0 :
        return n
    # 그렇지 않으면, 나누어서 나머지값이 나왔을때 그 값과 똑같은 번호의 죄수가 사탕을 먹는다
    else :
        return ans