import sys
n = int(sys.stdin.readline()) # 갯수 입력

array = []
for i in range(n) :
    array.append(int(sys.stdin.readline())) 

array.sort() # 오름차순 정렬

count_dict = {} # 각 숫자별 빈도수를 저장하기위해, 딕셔너리 리스트 설정
for num in array :
    if num in count_dict :
        count_dict[num] += 1
    else :
        count_dict[num] = 1
new_dict = sorted(count_dict.items(), key=lambda x : x[1], reverse=True)

# 1. 산술평균
avg = sum(array) / n 
print(round(avg))

# 2. 중앙값 : n개의 수들을 오름차순으로 나열할 경우, 그 중간 값
mid = len(array) // 2
print(array[mid])

# 3. 최빈값 : n개의 수들 중 빈도수가 가장 많은 것
if n >= 2 : # 2개이상 수의 경우
    if new_dict[0][1] == new_dict[1][1] : #만약 빈도수가 같을 경우, 두번째로 작은값 출력
        print(new_dict[1][0])
    else :
        print(new_dict[0][0])

else : # 그렇지 않으면, 가장 빈도수 많은것으로 출력
    print(new_dict[0][0])

print(array[-1] - array[0]) # 4. n개의 수들 중 최대값과 최소값 차이 

