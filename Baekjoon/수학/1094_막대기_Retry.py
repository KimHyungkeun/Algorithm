import sys

# 원하는 길이 x
x = int(sys.stdin.readline())
bar = [64] # 처음 가지고 있는 막대길이는 64


while True :
    
    # 원하는 길이가 64이면 그 자체이다
    if x == 64 :
        break
    
    # 제일 짧은 막대기를 제외한 나머지 길이들을 모두 더했을때, x값 이상이라면 현재의 막대리스트 중에 가장 짧은것을 제외한다
    if sum(bar[:-1]) >= x :
        bar.pop()
    else :
        # 가장 짧은 길이의 막대를 절반으로 자른다
        half = bar[-1] // 2
        bar.pop()
        bar.append(half)
        bar.append(half)
    
    # 만약 원하는 막대길이가 완성되었을 경우 루프문 종료
    if sum(bar[:-1]) == x :
        break


# 원하는 막대길이가 64이면 그 자체이므로 1개이고, 그 외에는 계산절차를 따른다
if x == 64 :
    print(1)
else :
    print(len(bar[:-1]))
