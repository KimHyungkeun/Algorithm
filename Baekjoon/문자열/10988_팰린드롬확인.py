import sys

# 단어 입력
word = sys.stdin.readline().rstrip()

# 시작점, 끝지점, 중간지점, 팰린드롬 판단여부를 설정
start = 0
end = len(word)-1
mid = len(word) // 2
flag = True

while start < end :
    # 만약 시작 지점과 끝지점이 같은 단어라면 그다음 철자를 비교
    if word[start] == word[end] :
        start += 1
        end -= 1
    
    # 만약 서로 다른 글자가 나오게되면 팰린드롬이 아님
    else :
        flag = False
        break

# flag가 참이면 팰린드롬이고, 거짓이면 팰린드롬이 아니다
if flag :
    print(1)
else :
    print(0)
