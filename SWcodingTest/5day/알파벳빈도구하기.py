import sys

alphabet_dict = {
    'a' : 0,
    'b' : 0,
    'c' : 0,
    'd' : 0,
    'e' : 0,
    'f' : 0,
    'g' : 0,
    'h' : 0,
    'i' : 0,
    'j' : 0,
    'k' : 0,
    'l' : 0,
    'm' : 0,
    'n' : 0,
    'o' : 0,
    'p' : 0,
    'q' : 0,
    'r' : 0,
    's' : 0,
    't' : 0,
    'u' : 0,
    'v' : 0,
    'w' : 0,
    'x' : 0,
    'y' : 0,
    'z' : 0
}

# 문자열 입력
string = sys.stdin.readline().rstrip()

for w in string :
    if w == ' ' : # 공백은 패스함
        continue
    else :
        if 65 <= ord(w) <= 90 : # 만약 대문자이면
             w = ord(w) + 32 # 소문자와 같은것으로 취급하고 횟수증가
             w = chr(w)
        alphabet_dict[w] += 1 # 해당 알파벳 빈도수 증가

for key,val in alphabet_dict.items() :
    print(str(key) + " : " + str(val))