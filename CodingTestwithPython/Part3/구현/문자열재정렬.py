import sys

string = list(sys.stdin.readline().rstrip()) # 문자열 입력
word = [] # 알파벳만을 담음
num = 0 # 숫자일 경우 그 값들을 누적시킴

for w in string :
    if 48 <= ord(w) <= 57 : # 숫자는 누적
        num += int(w)
    else : # 단어는 배열에 넣음
        word.append(w)

word.sort() # 오름차순 정렬

print(''.join(word) + str(num)) # 출력

