import sys

doller, add, year = sys.stdin.readline().split()
doller = int(doller) # 원금
add = float(add) # 이자율
year = int(year) # 년도

real_add = doller * (add/100) # 초기 이자율

for i in range(year) :
    doller += real_add # 해마다 이자율 추가
    real_add = doller * (add/100) # 이자율은 복리로 증가함

print("%.2f" % doller)

# https://level.goorm.io/exam/43190/%EC%9D%80%ED%96%89-%EC%98%88%EA%B8%88-%EC%9D%B4%EC%9E%90-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1