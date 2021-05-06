# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # 만약 y위치의 고양이가 z위치의 쥐와 가깝다면, y위치 고양이가 먼저잡게된다
    if abs(z-x) > abs(z-y) :
        return "Cat B"

    # 만약 x위치의 고양이가 z위치의 쥐와 가깝다면, x위치 고양이가 먼저잡게된다
    elif abs(z-x) < abs(z-y) :
        return "Cat A"
    
    # 두 고양이가 둘다 동시에 쥐룰 잡게되는 경우다
    else :
        return "Mouse C"