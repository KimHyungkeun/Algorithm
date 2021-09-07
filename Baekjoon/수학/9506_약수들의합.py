import sys

# n의 약수를 구하는 함수(n 본인은 제외)
def save_measure(n) :
    arr = []
    for i in range(1,n) :
        if n % i == 0 :
            arr.append(i)
    return arr 

while True :
    n = int(sys.stdin.readline())

    # -1을 입력하면 종료
    if n == -1 :
        break
    
    # n의 약수 구하기
    arr = save_measure(n)

    # n의 약수들의 합(n 본인은 제외) == n 이면 그 과정을 출력
    if sum(arr) == n :
        string = ""
        for i in range(len(arr)) :
            if i != len(arr)-1 :
                string += (str(arr[i]) + " + ")
            else :
                string += str(arr[i])
        print(n, "=", string)

    # 그렇지 않다면, is NOT perfect를 출력
    else :
        print(n, "is NOT perfect.")