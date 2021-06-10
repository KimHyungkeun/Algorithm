def removeDuplicates(llist):
    # Write your code here
    arr = []
    node = llist

    # 노드를 하나씩 순회하여 중복되는 값 없이 새로운 값들만을 arr에 모아놓는다.
    while node != None :
        if node.data not in arr :
            arr.append(node.data)
        node = node.next
    
    # arr를 차례대로 순회하여, 그에 따른 새로운 리스트노드들을 만들어 연결한다
    new_node = SinglyLinkedListNode(arr[0])
    head = new_node
    for i in range(1, len(arr)) :
        new_node.next = SinglyLinkedListNode(arr[i])
        new_node = new_node.next
    
    return head
