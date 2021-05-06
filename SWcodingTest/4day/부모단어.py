import sys

# 부모단어와 문자열을 입력한다
parent, child = sys.stdin.readline().split()
parent = list(parent) # 부모단어의 스펠링 하나하나를 리스트로 만든다
flag = True

# 만약 부모단어에 포함되어있지않은 철자가 나오면, child의 부모가 아닌것이다
for w in child :
    if w not in parent :
        flag = False
        break

if flag :
    print("YES")
else :
    print("NO")

# https://level.goorm.io/exam/43244/%EB%B6%80%EB%AA%A8-%EB%8B%A8%EC%96%B4/quiz/1