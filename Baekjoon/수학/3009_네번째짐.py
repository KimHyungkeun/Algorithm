vector = []

# x와 y의 빈도수를 각각 세어서, 빈도수가 1개밖에 나오지 않는 경우가 구해야할 좌표이다
for _ in range(3) :
    point = list(map(int, input().split())) # 나머지 3좌표의 좌표를 입력
    vector.append(point)

for i in range(2) : # x,y를 각각 횟수비교를 위해 2번 돌림
    count_dict = {}
    for j in range(3) : # 입력된 좌표가 3개이므로 3번 돌림
        if vector[j][i] in count_dict :
            count_dict[vector[j][i]] += 1 # 만약 이미 딕셔너리에 존재하면 1 증가
        else :
            count_dict[vector[j][i]] = 1 # 없다면 새로 추가
    
    for key,val in count_dict.items() :
        if val == 1 :
            print(key, end = ' ') # 출력
            break