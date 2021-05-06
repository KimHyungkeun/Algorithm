import sys

# 숫자입력
num = list(input())
# 숫자별 등장횟수를 저장
num_dict = {}

for i in range(len(num)) :
    # 9나 6을 서로 뒤집어서 쓸 수 있으므로, 9가 나온다 해도 6으로 취급한다.
    if num[i] == '9' :
        num[i] = '6'
    
    # 숫자별 등장횟수를 저장
    if num[i] in num_dict :
        num_dict[num[i]] += 1
    
    else :
        num_dict[num[i]] = 1

# 등장한 6의 갯수를 센다
if '6' in num_dict :
    repute = num_dict['6'] 
    num_dict['6'] = (repute // 2) + (repute % 2)

# 등장한 숫자가 가장 많은것이 최소로 꾸려야할 세트의 수다. (6과 9를 제외한 나머지 수는 1개씩밖에 없으므로)
sort = sorted(num_dict.items(), key = lambda x : x[1], reverse=True)

# 등장횟수
answer = sort[0][1]
print(answer)