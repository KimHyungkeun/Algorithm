import sys

# 옷 종류 n을 입력
n = int(sys.stdin.readline())

# 각 옷종류별 갯수를 담을 dict

for _ in range(n) :
    wear_dict = {} 
    num = int(sys.stdin.readline()) # 옷 종류 숫자
    for i in range(num) :
        wear, wear_type = input().split()
        if wear_type in wear_dict : # 이미 존재하는 옷종류면 카운트를 한다
            wear_dict[wear_type] += 1
        else :
            wear_dict[wear_type] = 1 # 새로운 옷종류면 dict에 추가한다

    # 각 옷종류에 대해서, 아무것도 입지않은 경우까지 포함하여 각각 +1을 한후, 모두 곱한다
    cases = 1
    for key,val in wear_dict.items() :
        cases *= (val+1) 

    # 모든 경우의 수에대해서, 아무것도 입지않은 경우만 제외한다
    print(cases-1) 
