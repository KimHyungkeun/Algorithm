# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    cnt = 0

    # 배열 ar내의 원소쌍의 합이 k의 배수이면 카운트를 증가시킨다
    for i in range(n) :
        for j in range(i+1, n) :
            if (ar[i] + ar[j]) % k == 0 :
                cnt += 1
    return cnt