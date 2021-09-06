import sys

# 주사위 3개를 던진다
result = list(map(int, sys.stdin.readline().split()))

# 주사위 3개가 모두 같은 눈이면, 눈의 수 * 1000원에 10000원을 추가로 준다
if len(list(set(result))) == 1 :
    print(10000 + result[0] * 1000)

# 주사위 2개가 같은 눈이면, 눈의 수 * 100원에 1000원을 추가한다
elif len(list(set(result))) == 2 :
    tmp = list(set(result))
    if result.count(tmp[0]) == 2 :
        print(1000 + tmp[0] * 100)
    else :
        print(1000 + tmp[1] * 100)

# 모두 다 다른 눈이면, 그중 가장 큰 눈의 수 * 100원을 한다 
else :
    print(max(result) * 100)
