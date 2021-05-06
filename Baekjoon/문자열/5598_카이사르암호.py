import sys

# 문자열 입력(카이사르 단어로 입력됨)
string = list(sys.stdin.readline().rstrip())

for i in range (len(string)) :
    # 해당 철자를 3번 앞당김
    tmp = ord(string[i]) - 3

    # 만약 해당 철자의 아스키코드가 65미만('A')이 되면, 90('Z')부터 역으로 센다 
    if tmp < 65 :
        string[i] = chr(90 - (65 - tmp) + 1)
    
    # 그렇지 않을경우에는 3번 앞당기기만 한다.
    else :
        string[i] = chr(tmp)

result = ''.join(string)
print(result)

