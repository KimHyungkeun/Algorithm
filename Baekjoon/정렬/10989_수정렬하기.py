import sys
n = int(sys.stdin.readline()) # 횟수 입력

array = [0] * 10001 # 수의 배열
for i in range(n) :
    a = int(sys.stdin.readline()) # 수를 입력
    array[a] = array[a] + 1

for i in range(len(array)) :
    if array[i] != 0 :
        for j in range(array[i]) : # 숫자 출력
            print(i)

# 참고 : https://kminito.github.io/baekjoon/2018/05/07/baekjoon_10989/