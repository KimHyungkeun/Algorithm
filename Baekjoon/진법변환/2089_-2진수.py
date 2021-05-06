n = int(input())

# print(int(n / -2))
# print(int(n % -2))

total = [] # 변환 완료된 진법이 들어갈 리스트
answer = "" # 문자열로 변환

while n != 0 :

    tmp = int(n % -2)
    tmp *= -1 # 나머지가 -1이므로, 이를 양수로 전환 시킨다.
    total.append(tmp)

    if n < 0 :
        if tmp == 0 :
            n = int(n / -2) # 음수이나 나누어 떨어지는 경우엔, 그대로 진행
        else :    
            n = int(n / -2) + 1 # 음수를 -2로 나눌 경우, 해당 몫에 +1을 시킨다. 
    
    else :
        n = int(n / -2)

total.reverse()
for i in range(len(total)) :
    answer += str(total[i])

if not total :
    answer = "0"
print(answer)
