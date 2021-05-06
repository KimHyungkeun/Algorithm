import sys

# 문자열 입력
s = list(sys.stdin.readline().rstrip())

for i in range(len(s)) :
    # 해당 문자의 아스키코드를 저장
    tmp = ord(s[i])

    # 대소문자는 아스키코드상으로 32 차이가 난다
    # 소문자이면 대문자로 바꿈
    if 'a' <= s[i] <= 'z' : 
        tmp -= 32
    
    # 대문자이면 소문자로 바꿈
    else :
        tmp += 32
    
    # 변경된 아스키코드에 해당되는 문자열로 새로 치환
    s[i] = chr(tmp)

print(''.join(s))

