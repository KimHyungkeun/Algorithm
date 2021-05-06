import sys

# o,x 결과를 넣는다
score = list(sys.stdin.readline().rstrip())

total = 0 # 총 점수
combo = 0 # 연속된 o가 나오면 combo수를 늘린다
for i in range (len(score)) :

    if score[i] == 'o' :
        combo += 1 # 연속으로 맞으면 combo수 증가
        total += combo # total에는 점수 누적
    
    else :
        combo = 0 # x가 나오면 콤보 초기화

print(total)








# https://level.goorm.io/exam/43280/%EC%B1%84%EC%A0%90%ED%95%98%EA%B8%B0/quiz/1