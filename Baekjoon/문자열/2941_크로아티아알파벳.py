import sys

# 문자열 입력
string = sys.stdin.readline().rstrip()

# 크로아티아 알파벳 종류
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 입력 문자열에 해당하는 크로아티아 알파벳이 있다면, 임의로 '0'으로 치환한다
for w in croatia :
    string = string.replace(w,'0')

# 크로아티아 알파벳을 대체된 문자열의 길이를 구한다
print(len(string))