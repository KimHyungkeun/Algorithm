import sys

# 문자열 입력
string = sys.stdin.readline().rstrip()
# 모음 종류
vowel = ['a','e','i','o','u']

cnt = 0
# 철자 중에서 모음이 있다면 카운트 증가
for w in string :
    if w in vowel :
        cnt += 1

print(cnt)