import sys

# 본래의 문자열과 폭발 문자열을 입력받고 bom_len에 폭발문자열 길이를 저장한다
string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
bom_len = len(bomb)

stack = []
for w in string :
    # 스택에 철자 하나하나를 저장한다
    stack.append(w)
    length = len(stack)
    
    # 만약 스택이 폭발문자열 길이 이상으로 쌓였을경우
    if len(stack) >= len(bomb) :
        # 스택의 top부터 거꾸로 세어서 일부 파트가 폭발문자열과 일치하는 경우에는 해당 부분을 스택에서 제거한다
        if ''.join(stack[length-bom_len:]) == bomb :
            for _ in range(bom_len) :
                stack.pop()

# 폭발 후, 남은 문자열이 없다면 "FRULA"를 출력하고, 그렇지 않으면 스택에 남은 철자들을 문자열로 만든다
if not stack :
    print("FRULA")
else :
    print(''.join(stack))