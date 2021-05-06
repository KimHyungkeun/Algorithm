def solution(s, n):
    answer = ''
    # 문자열 s를 리스트 타입의 arr로 변형
    arr = list(s)
    
    for i in range(len(arr)) :
        # 해당 문자가 대문자라면
        if 'A' <= arr[i] <= 'Z' :
            # 알파벳을 n만큼 밀었을때 대문자 범위를 벗어난 경우, 65와 초과 크기인 exceed를 더함. ('A'의 아스키코드는 65)
            if ord(arr[i]) + n > ord('Z') :
                exceed = ord(arr[i]) + n - ord('Z') - 1
                arr[i] = chr(65 + exceed)
            
            # 그 외는 일반 덧셈 시작
            else :
                arr[i] = chr(ord(arr[i]) + n)
        
        # 해당 문자가 소문자라면
        elif 'a' <= arr[i] <= 'z' :
            # 알파벳을 n만큼 밀었을때 대문자 범위를 벗어난 경우, 97과 초과 크기인 exceed를 더함. ('a'의 아스키코드는 97)
            if ord(arr[i]) + n > ord('z') :
                exceed = ord(arr[i]) + n - ord('z') - 1
                arr[i] = chr(97 + exceed)
            
            # 그 외는 일반 덧셈 시작
            else :
                arr[i] = chr(ord(arr[i]) + n)
        
        # 공백은 건너뜀
        else :
            continue
    
    answer = ''.join(arr)
    return answer