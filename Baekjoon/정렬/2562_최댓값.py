array = []
for _ in range(9) :
    array.append(int(input())) # 수 9개 입력 받음

maximum = max(array) # 최댓값 구함
print(maximum)

for i in range(9) :
    if array[i] == maximum : # 최댓값이 몇번째 있는지 구함
        print(i+1)
        break
