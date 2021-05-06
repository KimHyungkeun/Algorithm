import sys

# 자연수 n 입력
n = int(sys.stdin.readline())
add = (n-1) # 인덱싱을 위해, 입력받은 숫자에서 -1을 제외

# 첫번째, 두번째는 이미 1,1이 있으므로 그 이후 인덱스부터 세어서 추가시킴
if add <= 0 : 
    add = 0
array = [1,1] + [0]*add

# 피보나치 수열
for i in range(2, n+1) :
    if array[i] != 0 :
        continue
    array[i] = (array[i-1] + array[i-2]) % 15746

# 츨력
print(array[n])