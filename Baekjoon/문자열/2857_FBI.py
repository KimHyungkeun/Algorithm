import sys

# FBI 요원을 기록할 리스트
answer = []
for i in range(5) :
    # 해당 요원코드네임에서 "FBI"란 글자가 있다면 FBI 요원이다
    agent = sys.stdin.readline().rstrip()
    if "FBI" in agent :
        answer.append(i+1)

# FBI 요원을 한명도 찾지못하면 아래와같은 문구 출력
if not answer :
    print("HE GOT AWAY!")
# 있다면, 공백으로 나누어서 출력
else :
    for a in answer :
        print(a, end=' ')

