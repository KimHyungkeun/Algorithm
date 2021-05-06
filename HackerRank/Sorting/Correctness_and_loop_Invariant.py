def insertion_sort(arr):

    # 삽입정렬을 이용한 문제 해결

    for i in range(1, len(arr)) :
        # 현재의 처음위치를 저장한다
        pos = i
        for j in range(i-1, -1, -1) :

            # 만약 이전위치의 요소가 현위치의 요소보다 크다면 서로 스와핑한다
            if arr[j] > arr[pos] :
                arr[j], arr[pos] = arr[pos], arr[j]
                pos, j = j, pos
            
            # 그렇지 않다면, 현재의 루프문을 벗어나고 다음 요소를 살핀다
            else :
                break