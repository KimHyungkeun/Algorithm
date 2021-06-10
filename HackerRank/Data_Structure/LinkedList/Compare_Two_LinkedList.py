def compare_lists(llist1, llist2):
    arr1 = [] # llist1의 data를 담을 배열
    arr2 = [] # llist2의 data를 담을 배열
    
    # arr1에 llist1의 데이터를 모두 담음
    while llist1 != None :
        arr1.append(llist1.data)
        llist1 = llist1.next
    
    # arr2에 llist2의 데이터를 모두 담음
    while llist2 != None :
        arr2.append(llist2.data)
        llist2 = llist2.next
    
    # arr1과 arr2 길이가 다르면 0을 리턴
    if len(arr1) != len(arr2) :
        return 0
    
    else :
        # 길이가 같으나 서로 다른 요소를 가지면 0을 리턴
        for i in range(len(arr1)) :
            if arr1[i] != arr2[i] :
                return 0
        
        # 그 외에는 llist1과 llist2가 같은 요소와 같은길이를 모두 가지므로 1 리턴
        return 1