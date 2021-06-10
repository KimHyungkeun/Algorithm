def insertNodeAtHead(llist, data):
    # Write your code here
    
    # 현재 리스트가 아무것도 없는 것이라면, 새 노드를 할당한다
    if llist is None :
        llist = SinglyLinkedListNode(data)
        return llist
    
    # 이미 존재하는 노드가 있다면, 한 노드를 생성한 후 이미 존재하는 노드의 맨 앞을 가리킨다.
    node = SinglyLinkedListNode(data)
    node.next = llist

    return node