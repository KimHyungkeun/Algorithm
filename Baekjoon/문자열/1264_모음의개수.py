import sys

vowel = ['a','e','i','o','u','A','E','I','O','U']

while True :
    string = sys.stdin.readline().rstrip()
    
    # #을 입력 받으면 종료
    if string == '#' :
        break
    
    cnt = 0
    # 철자를 검색하면서 모음일때마다 카운트를 증가시킨다. 
    for s in string :
        if s in vowel :
            cnt += 1
    
    print(cnt)
