def findMergeNode(head1, head2):
    p1 = head1 # 리스트1의 검색 위치
    p2 = head2 # 리스트2의 검색 위치
    
    while True :
        if p1 == p2 : # 만약 두 리스트의 지점이 기리키는곳이 모두 같다면 루프문 종료
            break
        p1 = p1.next # 리스트1의 다음 리스트 확인
        p2 = p2.next # 리스트2의 다음 리스트 확인
        if p1 is None : # 리스트1이 모두 검색을 다하면 리스트2의 처음 지점으로 위치 선정
            p1 = head2
        if p2 is None : # 리스트2가 모두 검색을 다하면 리스트1의 처음 지점으로 위치 선정
            p2 = head1
    return p1.data

    # 참고 : https://www.youtube.com/watch?v=WcOdcUHOA1M&ab_channel=CodingCart
    
    # node1 = head1
    # node2 = head2
    
    # arr1 = []
    # arr2 = []
    # while node1 != None :
    #     arr1.append(node1.data)
    #     node1 = node1.next
    # # print("---------------------")
    # while node2 != None :
    #     arr2.append(node2.data)
    #     node2 = node2.next
    
    # intersect = set(arr1) & set(arr2)
    # intersect = list(intersect)
    
    # new_inter = []
    # for a in arr1 :
    #     if a in intersect :
    #         new_inter.append(a)
    
    # node1 = head1
    # node2 = head2
    # for i in new_inter :
    #     while node1.data != i :
    #         node1 = node1.next
    #     while node2.data != i :
    #         node2 = node2.next
        
    #     if node1 == node2 :
    #         return i
    #     else :
    #         node1 = head1
    #         node2 = head2