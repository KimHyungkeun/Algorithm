# Complete the insertionSort1 function below.
def insertionSort1(n, arr):

    # 마지막 요소를 임시저장한다
    tmp = arr[-1]
    
    for i in range(n-2,-1,-1) :
        # print(i)

        # 끝에서 두번째 요소부터 시작해서, 임시저장된 요소와 크기를 비교한다

        # 만약, 해당 요소가 임시저장된 요소보다 크다면, 현재번째 요소와 다음번째 요소를 같게한다
        if arr[i] > tmp :
            arr[i+1] = arr[i]
            print(*arr)
        
        # 만약 그렇지 않으면 다음번째 요소에 임시저장돤 요소를 넣고 루프문을 종료한다
        else :
            arr[i+1] = tmp
            print(*arr)
            break
    
    # 모든 루프문이 다 돌았음에도 첫번째와 두번째 요소가 같다면, 첫번째 요소에 임시저장 요소 tmp를 넣는다
    if arr[0] == arr[1] :
        arr[0] = tmp
        print(*arr)