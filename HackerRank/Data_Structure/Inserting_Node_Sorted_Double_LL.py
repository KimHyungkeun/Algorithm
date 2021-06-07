def sortedInsert(llist, data):
    # Write your code here

    node = llist # 노드의 헤드부분 부터 탐색
    while node != None :

        # 노드의 가장 맨 처음(헤드)에 있을때
        if node.prev is None and node.next is not None :     
            if node.data <= data : # 넣으려는 data가 현재 노드 데이터보다도 크거나 같다면
                node = node.next # 다음 노드로 이동
            else :
                # 현재 노드 이전에 새로운 노드를 만들어서 data를 삽입한다
                new_node = DoublyLinkedListNode(data)
                node.prev = new_node 
                node.prev.next = node           
                llist = node.prev # 새로 삽입한 부분이 새로운 헤드가 된다
                break
        
        # 노드의 가장 마지막에 있을때
        elif node.prev is not None and node.next is None :
            new_node = DoublyLinkedListNode(data)
            # # 넣으려는 data가 현재 노드 데이터보다도 크거나 같다면
            if node.data <= data :
                node.next = new_node # 현재 노드 다음에 새로운 노드를 생성한다
                break
            else :
                # 그렇지 않다면 중간에 새로 끼워 넣는다
                node.prev.next = new_node
                new_node.next = node
                break
        
        # 노드와 노드 사이 일때
        else :

            # 넣으려는 data가 이전 노드의 데이터보단 크고 현재 노드의 데이터보단 작다면 그 사이에 넣는다
            if node.prev.data <= data <= node.data :
                new_node = DoublyLinkedListNode(data)
                node.prev.next = new_node
                new_node.next = node
                break
            
            # if 조건을 만족하지 않으면 다음 노드로 이동한다
            else :
                node = node.next
    
    return llist