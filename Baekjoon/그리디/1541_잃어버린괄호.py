# 수식 입력
s = input()
form = s.split("-") # 뺄셈을 기준으로 수식을 구분한다
# print(form)

result = 0
for i in range(len(form)) :
    # 각 수식별로 덧셈을 진행한다
    tmp = form[i].split("+")
    tmp_result = 0
    for j in range(len(tmp)) :
        tmp_result += int(tmp[j])
    
    # 맨 첫번째 결과를 중심으로 뺄셈을 하나하나씩 진행해나갈 예정이다
    if i == 0 :
        result = tmp_result
        continue
    
    # 두번째 순서부터는 덧셈을 진행했던 결과들을 하나하나씩 뺄셈해나간다.
    result -= tmp_result

print(result)




