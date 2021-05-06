n1, n2 = input().split()

# 글자 하나하나씩을 다루기위해 리스트로 만든다
list1 = list(n1)  
list2 = list(n2) 

real_n1 = ""
real_n2 = ""

for i in range(len(list1)-1, -1, -1) :
    real_n1 += list1[i] # 입력받은 수를 거꾸로 만든다

for i in range(len(list2)-1, -1, -1) :
    real_n2 += list2[i] # 입력받은 수를 거꾸로 만든다

# 두 수의 실제 대소비교를 실시
if int(real_n1) > int(real_n2) : 
    print(int(real_n1))

else :
    print(int(real_n2))