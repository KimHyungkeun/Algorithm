import sys

# 해쉬맵 사용

# 자연수 n개 만큼의 카드 갯수설정
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

# 자연수 m개의 카드 각각에 대해 갯수를 찾아야함 
m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))

n_dic = {}
# array에 들어있는 수들에 대한 갯수를 구한다
for i in range(n) :
    if array[i] in n_dic :
        n_dic[array[i]] += 1
    
    else :
        n_dic[array[i]] = 1

# print(n_dic)

# n_dic에, m_array에 있는 요소가 있는지 확인한다
for i in range(m) :
    if m_array[i] not in n_dic :
        print('0', end=' ')

    else :
        print(str(n_dic[m_array[i]]), end=' ') 

 
    
# 참고 : https://chancoding.tistory.com/45

    



    

