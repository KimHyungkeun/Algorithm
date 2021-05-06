a, b = map(int, input().strip().split(' '))

# 각 줄당 a만큼의 별을 찍는다. 반복횟수는 b번이다
for i in range(b) :
    print('*'*a)