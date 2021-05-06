import sys

# 배열갯수 n 입력
n = int(sys.stdin.readline())
# result = []

# 쌍의 갯수
cnt = 0

# 배열 원소 입력, target이 될 수 입력, 그리고 배열을 오름차순
array = list(map(int, sys.stdin.readline().split()))
answer = int(sys.stdin.readline())
array.sort()

# 첫번째와 마지막번째에 포인터를 둔다
start = 0
end = len(array)-1


# 만약 배열 원소갯수가 하나뿐일때, target과 같다면 카운트를 올린다
if len(array) == 1 :
    if array[0] == answer :
        cnt += 1

else :
    # 항상 시작점이 끝지점보다 작아야한다
    while start < end :
        # 만약 원하는 수를 찾으면, 시작점은 한칸 올리고 끝지점은 한칸 내린다
        if array[start] + array[end] == answer :
                # result.append((array[start], array[end]))
                cnt += 1
                start += 1
                end -= 1

        # 만약 두 수의 합이 target보다도 작다면, start를 한칸 올린다
        elif array[start] + array[end] < answer :
            start += 1

        # 만약 두 수 의 합이 target보다 크면, end를 한칸 내린다
        else :
            end -= 1
    
        
# print(result)
# print(len(result))
print(cnt)