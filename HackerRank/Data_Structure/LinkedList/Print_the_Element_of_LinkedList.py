# data : 실제 값이 담기는 곳
# next : 다음 노드의 주소값을 담기 위한 곳

def printLinkedList(head):
    while head != None :
        print(head.data)
        head = head.next