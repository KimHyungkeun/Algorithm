import sys

# 숫자 입력
num = input()
count = 0 #자릿수를 모두 더할때마다, 카운트를 증가시킴
result = "NO" # YES or NO를 표현


# 한 자리수가 될때 자릿수를 더하고, 3의배수 여부를 판단
while len(num) != 1 :
    
    summary = 0 
    count += 1

    for n in num :
        summary += int(n)
    num = str(summary)

# num이 한자리수까지 왔을 경우
if int(num) % 3 == 0 :
    result = "YES"

print(count)
print(result)


