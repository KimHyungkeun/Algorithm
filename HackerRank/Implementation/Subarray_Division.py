# Complete the birthday function below.
def birthday(s, d, m):
    cnt = 0 

    # 배열 s에 대해서 차례대로 m개만큼의 하위배열의 합이 d와 같다면 카운트를 증가시킨다
    for i in range(len(s)) :
        if sum(s[i:i+m]) == d :
            cnt += 1
    return cnt