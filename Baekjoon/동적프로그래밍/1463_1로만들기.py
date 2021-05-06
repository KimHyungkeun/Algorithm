x = int(input())
lists = [x]
count = 0

def making_one (x) :
    tmp_list = []
    for i in x :
        tmp_list.append(i-1)

        if i % 3 == 0 :
            tmp_list.append(i/3)
        
        if i % 2 == 0 :
            tmp_list.append(i/2)
        
    return tmp_list

while True :
    if x == 1:
        print(count)
        break

    temp = lists
    lists = []
    lists = making_one(temp)
    count += 1
    if min(lists) == 1 :
        print(count) 
        break

# 참조 https://doorbw.tistory.com/57
