#  알파벳별 등장 횟수
alphabet = {
    'a' : 0,'b' : 0,'c' : 0,'d' : 0,'e' : 0,'f' : 0,'g' : 0,'h' : 0,'i' : 0,'j' : 0,'k' : 0,'l' : 0,
    'm' : 0,'n' : 0,'o' : 0,'p' : 0,'q' : 0,'r' : 0,'s' : 0,'t' : 0,'u' : 0,'v' : 0,'w' : 0,'x' : 0,
    'y' : 0, 'z' : 0
}

# 문자열 입력
string = input()

# 알파벳별로 등장횟수를 카운팅한다
for w in string :
    alphabet[w] += 1

# 등장횟수 출력
for val in alphabet.values() :
    print(val, end=' ')