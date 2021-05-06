def d(n) :
    val = n
    str_list = list(str(n)) # 자릿수별 조작을 위해 임의로 리스트로 만듦
    for i in  str_list: 
        val += int(i) # 각 자리수를 모두 더함
    
    return val

self_num = [] # 생성자가 아닌 것들만 모아놓음

for i in range(10001) :
    self_num.append(d(i)) 

# print(self_num)
for i in range(1, 10001) :
    if i not in self_num : # 생성넘버인 것들만 출력
        print(i)


