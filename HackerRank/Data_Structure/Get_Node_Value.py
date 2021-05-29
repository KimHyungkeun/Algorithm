def getNode(llist, positionFromTail):
    # Write your code here
    arr = []
    node = llist 

    # 노드를 순회하여 Tail위치까지 간다.
    # 노드를 순회하는 도중 만나는 data들은 arr에 넣는다
    while node != None :
        arr.append(node.data)
        node = node.next
    
    # arr에 담긴 요소들의 순서를 역순정렬한다.
    arr.reverse()
    return arr[positionFromTail]