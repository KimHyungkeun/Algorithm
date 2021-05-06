import sys

# 최대공약수 함수
def gcd(a,b) :
    if b > a :
        a, b = b, a
    while True :
        if b == 0 :
            break
        q, r = divmod(a, b)
        a,b = b,r
    return a

# n:m 형태로 입력받고, :를 기준으로 문자들을 나눈다
string = sys.stdin.readline().rstrip()
string = string.split(":")

# 현재의 요소들은 string 형태이므로, num형태의 요소를 담을 리스트를 생성한다
number = []
for s in string :
    number.append(int(s))

# 두 수의 최대공약수로 약분해야, 기약분수를 만들수 있다
result = gcd(number[0], number[1])

# 약분
for i in range(len(number)) :
    number[i] //= result

print(str(number[0])+":"+str(number[1]))