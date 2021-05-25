def reversePrint(llist):
    # Write your code here
    arr = []

    # 노드를 순서대로 순회하여 얻은 data를 arr에 넣는다
    while llist != None :
        arr.append(llist.data)
        llist = llist.next
    
    # arr에 담긴 요소들을 역순으로 재배치한다
    arr.reverse()
    for a in arr :
        print(a)