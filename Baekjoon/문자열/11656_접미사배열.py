import sys

# 단어 입력
word = sys.stdin.readline().rstrip()

# 해당 단어에 대한 접미사를 모두 구한다
types = []
for i in range(len(word)) :
    types.append(word[i:])

# 오름차순 정렬(알파벳순 정렬)
types.sort()

# 정렬한 결과 출력
for _ in types :
    print(_)