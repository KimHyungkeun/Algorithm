n, m = map(int, input().split())
array = list(map(int, input().split())) 
count = 0

def binary_search(array, target, start, end) :
    
    mid = (start + end) // 2 # 중간지점 설정
    i = 0

    while i <= mid : # 루프문은 mid까지 돈다
        if array[start] != target : # 원하는 수를 찾을때까지 start에서 증가
            start += 1
                   
        if array[end] != target : # 원하는 수를 찾을때까지 end에서 감소
            end -= 1

        if array[start] == array[end] == target : # 원하는 수를 찾음
            break 

        i += 1

    if array[start] != array[end] : # 만약 원하는 수를 못찾으면 -1 리턴
        return -1

    else :   
        return end - start + 1  # 찾았으면 그 갯수를 리턴

result = binary_search(array, m, 0, len(array)-1 )
print(result)