while True :
    length = list(map(int, input().split())) # 세 변의 길이를 입력

    if sum(length) == 0 : # 세 변이 모두 0,0,0 이면 종료
        break

    max_length = max(length) # 최대값의 변의길이를 따로 저장
    length.remove(max_length) # length 리스트에서 제외

    if max_length**2 == length[0]**2 + length[1]**2 : # 피타고라스의 정리를 통해 직각삼각형 여부 판별
        print("right")
    else :
        print("wrong")
