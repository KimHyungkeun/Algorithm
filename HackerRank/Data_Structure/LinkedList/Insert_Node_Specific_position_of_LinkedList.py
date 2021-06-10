def insertNodeAtPosition(llist, data, position):
    # Write your code here
    cnt = 1
    node = llist 
    while cnt != position : # 원하는 포지션에 도착할때까지 움직임
        cnt += 1
        node = node.next 
    
    new_node = SinglyLinkedListNode(data) # 새로운 노드를 생성
    new_node.next = node.next # 새로 생성한 노드의 다음 노드는, 현재 위치에서의 노드의 다음 노드를 가리킴
    node.next = new_node # 현재 위치의 다음 노드는 방금 생성한 새로운 노드로 설정

    return llist