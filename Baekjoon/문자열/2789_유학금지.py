import sys

# CAMBRIDGE 각각의 철자를 담은 배열을 선언(중복 없음)
arr = list(set(list("CAMBRIDGE")))

# 문자열 입력
string = list(sys.stdin.readline().rstrip())

# CAMBRIDGE내에 들어간 철자가 포함되지 않은 글자들만 result에 추가
result = ""
for s in string :
    if s not in arr :
        result += s

print(result)
