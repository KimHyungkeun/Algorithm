import sys

while True :
    cnt_big = 0 # 대문자 갯수
    cnt_small = 0 # 소문자 갯수
    cnt_space = 0 # 공백 갯수
    cnt_num = 0 # 숫자 갯수
    string = list(sys.stdin.readline()) # 문자열 입력
    if not string :
        break # 빈 문자열이면 루프문 탈출
    for s in string :
        # 각 조건에 맞게 갯수를 증가시킴
        if 'A' <= s <= 'Z' :
             cnt_big += 1
        elif 'a' <= s <= 'z' :
            cnt_small += 1
        elif '0' <= s <= '9' :
            cnt_num += 1
        elif s == ' ' :
            cnt_space += 1
        else :
            continue
    # 소문자, 대문자, 숫자, 공백 순서대로 갯수 출력
    print(cnt_small, cnt_big, cnt_num, cnt_space)
