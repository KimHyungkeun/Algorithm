def insertNodeAtTail(head, data):
    node = head
    if node is None : # 현재 노드가 마지막 노드이면 새로운 노드를 생성한다.
        node = SinglyLinkedListNode(data) # 그 노드에 data를 넣는다
        return node
    
    while node.next != None : # 현재노드가 마지막이 아니면, 마지막 노드까지 이동한다
        node = node.next
    
    node.next = SinglyLinkedListNode(data) # 마지막노드에서 새로운 노드를 생성하고 data를 넣는다
    return head # head를 리턴