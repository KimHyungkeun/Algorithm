import sys

# 문자열을 입력 받음
arr = list(sys.stdin.readline().rstrip())
for i in range(len(arr)) :
    # 소문자일 경우, 해당 알파벳에서 13개의 철자를 밀려서 출력.
    if 'a' <= arr[i] <= 'z' :
        tmp = ord(arr[i]) + 13
        # 만약 알파벳 범위를 벗어났을 경우, 다시 순환할수 있도록 한다
        if tmp > ord('z') :
            tmp -= 26
        arr[i] = chr(tmp)
    
    # 대문자일 경우, 해당 알파벳에서 13개의 철자를 밀려서 출력.
    elif 'A' <= arr[i] <= 'Z' :
        tmp = ord(arr[i]) + 13
        # 만약 알파벳 범위를 벗어났을 경우, 다시 순환할수 있도록 한다
        if tmp > ord('Z') :
            tmp -= 26
        arr[i] = chr(tmp)
    
    # 그 외의 문자는 그대로 두어야 한다
    else :
        continue

print(''.join(arr))