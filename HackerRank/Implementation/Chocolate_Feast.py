# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):

    # 현재 가진 n의 돈으로 c값 하는 초코바를 사먹는다. 그 후, 먹은 초코바만큼 포장지가 남는다
    bar = n // c
    wrap = bar
    
    # 포장지 m개를 초코바 하나로 바꿀수 있으므로, m개 미만의 포장지를 가질때까지 반복
    while wrap >= m :
        # 포장지 m개당 초코바를 추가로 사먹는다
        bar += (wrap // m)
        # 포장지 m개씩 하여 남은 포장지가 줄어들고, 새로 초코바를 사먹음으로써 그만큼의 포장지가 또 추가된다
        tmp = wrap - m * (wrap // m) + (wrap // m)
        wrap = tmp


    return bar

n = 10
c = 2
m = 5
chocolateFeast(n, c, m)