def mergeLists(head1, head2):
    arr = []
    node1 = head1 # 노드1의 헤드
    node2 = head2 # 노드2의 헤드
    
    # 각 노드별 data들만 따로 모아서 arr에 저장한다
    while node1 != None :
        arr.append(node1.data)
        node1 = node1.next
    while node2 != None :
        arr.append(node2.data)
        node2 = node2.next
    
    # print(arr)

    # 저장된 arr내의 요소들을 오름차순으로 배열한다
    arr.sort()
    
    # 새로운 링크드리스트 노드를 생성한다
    new_node = SinglyLinkedListNode(arr[0])
    new_node_head = new_node # 새로 생성한 노드의 헤드부분을 기억한다

    # 순차적으로 노드를 만들어서 연결짓는다
    for i in range(1, len(arr)) :
            new_node.next = SinglyLinkedListNode(arr[i])
            new_node = new_node.next
    
    return new_node_head