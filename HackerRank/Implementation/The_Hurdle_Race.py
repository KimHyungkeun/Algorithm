# Complete the hurdleRace function below.
def hurdleRace(k, height):
    maximum = max(height) # 주어진 허들 높이들 중, 가장 최고 높은 것을 고른다
    if maximum - k <= 0 : # 만약 k가 최대 허들높이보다도 높다면, 0을 리턴
        return 0
    else : # 그렇지 않다면, 그 차이를 리턴
        return maximum - k