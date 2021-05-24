def deleteNode(llist, position):
    # Write your code here
    cnt = 0
    node = llist
    
    if position == 0 : # 첫번째면 그다음 리스트를 시작head로 둔다
        llist = llist.next
    else :
        while cnt < position-1 : # position번째 노드에 도착하면, 이전노드가 position 다음 노드를 가리키도록 한다
            node = node.next
            cnt += 1

        node.next = node.next.next
    return llist