# 순차 탐색 함수
def sequential_search(n, target, array) :
    for i in range(n) :
        # 현재의 원소가 찾고하자 하는 원소와 동일한 경우
        if array[i] == target :
            return i + 1 # 현재의 위치 반환(인덱스 0부터 시작하므로, +1)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열 입력")
input_data = input().split()
n = int(input_data[0]) # 원소 개수
target = input_data[1] # 찾을 문자열
 
print("앞서 적은 원소개수만큼 문자열을 입력. 구분은 띄어쓰기 한 칸")
array = input().split() 

# 순차 탐색
print(sequential_search(n,target,array))

# 순차탐색의 최악의 시간복잡도는 O(N)