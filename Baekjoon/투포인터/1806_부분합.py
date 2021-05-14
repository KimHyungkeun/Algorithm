import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

pos = [0, n-1]

# 포인터 두개를 처음 시작지점으로 설정
start = 0
end = 0

# 현재 위치에서의 총 부분합
total = arr[0]

flag = False # s이상의 부분합을 만들수 있는지 여부
while start < n and end < n :
    
    # 해당 영역이 s 미만의 부분합을 가지면
    if total < s :
        end += 1 # end를 하나 더 올린다.
        if end == n : # 만약 탐색 범위를 벗어나면 루프문을 탈출한다
            break
        total += arr[end] # 확장된 영역까지의 부분합으로 갱신한다
        
    else :   
        flag = True # 한번 이상이라도 s이상의 부분합을 만들수 있다면 flag를 참값으로 설정
        if end - start < pos[1] - pos[0] : # 현재 범위보다 더 좁은 범위내에서 s이상의 부분합을 만들 수 있다면, 해당 좌표로 갱신
            pos = [start, end]

        total -= arr[start] # start가 한칸 땡겨지므로, 그 범위를 벗어난 값에대해서는 차감을 한다
        start += 1 # start를 한칸 땡김
    
    
if not flag : # 아예 s 이상의 부분합을 만들지 못하면 0을 리턴
    answer = 0
else : # 그 외에는 해당 영역의 값을 구함
    answer = pos[1] - pos[0] + 1
print(answer)  