import sys

string = list(sys.stdin.readline().rstrip()) # 세부적인 탐색을 위해 리스트로 설정
mid = len(string) // 2 # 해당 문자열의 가운데지점으로 나눔

left = 0 # 중간지점 이전
right = 0 # 중간지점 이후

for i in range(mid) :
    left += int(string[i]) #중간 이전까지를 모두 더함
 
for i in range(mid,len(string)) : # 중간부터 끝까지 모두 더함
    right += int(string[i])

# 럭키스트레이트 여부 판단
if left == right : 
    print("LUCKY")

else :
    print("READY")