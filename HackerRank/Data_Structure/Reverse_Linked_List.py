def reverse(llist):
    # Write your code here
    arr = []
    node = llist
    
    # 노드의 처음부터 끝까지 모든 data들을 탐색한다
    while node != None :
        arr.append(node.data)
        node = node.next
    
    # 담아놓은 데이터 배열의 순서를 역순으로 정렬한다
    arr.reverse()
    
    node = llist
    cnt = 0
    # 다시 노드의 처음부터 끝까지 수순을 밟으며, 새로 정렬된 arr에 담긴 순서대로 데이터를 업데이트한다
    while node != None :
        node.data = arr[cnt]
        node = node.next
        cnt += 1
    
    # 새로 변경된 리스트를 리턴
    return llist