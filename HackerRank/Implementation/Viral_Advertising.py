# Complete the viralAdvertising function below.
def viralAdvertising(n):
    day = 0 # n이 될때까지 day가 지난다
    shared = 5 # 첫 공유횟수는 5로 시작
    cumul = 0 # 누적되는 좋아요 갯수
    while day != n :

        liked = shared // 2 # 공유횟수의 절반이 좋아요 갯수이다
        cumul += liked # 좋아요 갯수를 누적한다
        shared = liked * 3 # 새 공유횟수는 지금의 좋아요 갯수의 3배
        day += 1 # 하루가 지난다
    
    return cumul