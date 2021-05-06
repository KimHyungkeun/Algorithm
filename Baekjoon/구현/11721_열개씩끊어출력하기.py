import sys

s = sys.stdin.readline()
for i in range(len(s)) :
    # 10n째 글자인 경우에는 다음 줄에서 출력한다.
    if i >= 10 and i % 10 == 0 :
        print()
    print(s[i],end='')
    