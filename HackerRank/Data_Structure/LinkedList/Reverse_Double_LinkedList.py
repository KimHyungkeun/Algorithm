def reverse(llist):
    # Write your code here
    arr = [] # 링크드 리스트를 탐색하며 얻은 데이터를 모아놓는 배열

    node = llist # 기존 링크 탐색을 위해 llist의 헤드부분을 가리킴
    new_node = llist # 새로이 넣기 위해 llist의 헤드부분을 가리킴

    # 노드를 모두 돌아서 arr에 데이터들을 집어넣음
    while node != None :
        arr.append(node.data)
        node = node.next
    
    # arr에 담긴 배열을 역순으로 배치
    arr.reverse()
    
    # 기존 노드를 다시 순회하면서, arr에 담긴 새로운 데이터들을 넣는다
    for a in arr :
        new_node.data = a
        new_node = new_node.next
    
    return llist