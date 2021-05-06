n = int(input())

people_dict = {}

for i in range(n) :
    age, name = input().split() # 나이와 이름 입력
    age = int(age)

    # 각 나이대별에 속하는 이름들을 모음
    if age not in people_dict :
        people_dict[age] = [name] #
    
    else :
        people_dict[age].append(name)

sorted_dict = sorted(people_dict.items()) # 나이순대로 정렬
# print(sorted_dict)

# 나이와 이름을 순서대로 출력, 나이가 같은경우 먼저 가입한 순서대로 출력
for i in range(len(sorted_dict)) :
    for j in range(len(sorted_dict[i][1])) :
        print(sorted_dict[i][0], sorted_dict[i][1][j])

    
