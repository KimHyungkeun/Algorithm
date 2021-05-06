# Complete the countSwaps function below.
def countSwaps(a):
    cnt = 0 # 스왑이 일어날때마다 그 횟수를 증가
    for i in range(len(a)) :
        for j in range(i+1, len(a)) :
            if a[i] > a[j] : # 만약 현재의 숫자가 다음 숫자보다 크다면, 그 둘을 서로 맞바꾼다
                a[i],a[j] = a[j], a[i]
                cnt += 1
    print("Array is sorted in " + str(cnt) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    
    return a