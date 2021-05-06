n, s = input().split()
n = int(n)
s = int(s)

# print(n, s)
def gcd (a, b) :
    while b != 0 :
        r = a % b
        a = b 
        b = r
    return a

pos = list(map(int, input().split())) # 동생들이 숨어있는 위치이다
# print(pos)

for i in range (n) : 
    mov = s - pos[i] # 수빈이가 현재 존재하는 곳으로부터 얼마나 갔는지를 표현
    if mov < 0 :
        mov = mov * -1 # 얼마나 움직였는지 자체를 보기 위해, 절대값으로 표현
    pos[i] = mov # 수빈이가 각 동생에 대해 움직일 수 거리들을 리스트로 표현

result = pos[0]

for i in range (n) : # 움직인 거리들에 대해 최대공약수를 구한다.
    result = gcd(result, pos[i]) 
    

print(result)

