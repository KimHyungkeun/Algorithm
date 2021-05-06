# n = []

# for i in range(9) :
#     number = int(input())
#     n.append(number)

# flag = False
# height = sum(n)
# n.sort()

# for i in range(9) :
#     for j in range(i+1, 9) :
#         if height - n[i] - n[j] == 100 :
#             tmp1 = n[i]
#             tmp2 = n[j]
#             n.remove(tmp1)
#             n.remove(tmp2)
#             flag = True
#             break
#     if flag :
#         break

# for i in range(7) :
#     print(n[i])

# -------------------------------------------------------

n = []
for _ in range(9) :
    n.append(int(input())) # 난쟁이 키 입력

n.sort() # 오름차순 출력을 대비하여, 오름차순 정렬
height_sum = sum(n) # 현재 입력된 모든 난쟁이들의 키
diff = height_sum - 100 # 진짜 난쟁이들의 키 합은 100이므로, diff는 남은 가짜 2명의 키 합이다. 

for i in range(len(n)) :
    for j in range(i+1, len(n)) :
        if n[i] + n[j] == diff : # 만약 두 난쟁이의 키가 diff와 같다면 반복문에서 탈출한다
            tmp1 = n[i]
            tmp2 = n[j]
            break

# 가짜 난쟁이는 삭제한다
n.remove(tmp1)  
n.remove(tmp2) 

for i in range(len(n)) :
    print(n[i])



