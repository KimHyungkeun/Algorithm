# 숫자 입력
n = list(input())
# 숫자의 길이
length = len(n)
# 자리수의 중간 지점
mid = length // 2

# 주어진 자릿수가 홀수자릿수이면 READY를 출력
if length % 2 != 0 :
    print("READY")

else :

    # 중간지점을 기준으로 왼편 자리수들의 합을 구함
    summary1 = 0
    for i in range(mid) :
        summary1 += int(n[i])
    
    # 중간지점을 기준으로 오른편 자리수들의 합을 구함
    summary2 = 0
    for i in range(mid, length) :
        summary2 += int(n[i])

    # 자릿수가 서로 같다면 LUCKY를 출력하고, 아니면 READY를 출력
    if summary1 == summary2 :
        print("LUCKY")

    else :
        print("READY")    
    







