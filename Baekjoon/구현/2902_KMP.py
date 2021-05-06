# 문자열을 입력하고 "-"를 기준으로 문자열을 나눈다
string = input()
arr = string.split("-")

answer = ""
# "-"를 기준으로 나눈 substring 각각의 맨 첫번째 글자만 따온다
for i in range(len(arr)) :
    answer += arr[i][0]

print(answer)