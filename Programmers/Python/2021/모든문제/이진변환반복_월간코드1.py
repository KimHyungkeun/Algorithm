def binary(n) : # 해당 10진법 수를 이진수로 만들기 위한 함수
    result = []
    while n != 0 :
        result.append(str(n % 2))
        n //= 2
    result.reverse() # 나머지값을 모두 담고 나면, 그 배치를 역순으로 배치한다
    return ''.join(result)

def solution(s):
    answer = []
    
    cnt = 0 # 연산을 진행한 횟수
    delete = 0 # 지금까지 지워진 총 0의 갯수

    s = list(s) # 0의 갯수를 세기위해 리스트 형태로 변환
    c = len(s) # 해당 이진수의 길이

    while len(s) != 1 :
        
        zero = s.count('0') # 0의 갯수를 센다
        c -= zero # 총 길이 c에서 0의 갯수만큼을 뺀다
        delete += zero # 제거된 0의 갯수만큼을 delete 변수에 누적시킨다
        cnt += 1 # 연산 횟수를 올린다

        
        s = list(binary(c)) # 0의 갯수를 세기위해 리스트 형태로 변환
        c = len(s) # 해당 이진수의 길이
        
    answer = [cnt, delete] # 연산 횟수, 삭제된 총 0의 갯수를 각각 담는다
    return answer

# s = "110010101001"
s = "1111111"
solution(s)