n = int(input())

num_list = []
for _ in range(n) :
    lists = list(input().split())
    num_list.append(lists[1:])

length = len(num_list)
for i in range(length) :
    for j in range(len(num_list[i])) :
        num_list[i][j] = int(num_list[i][j])

# print(num_list)

def gcd (a, b) : # 최대공약수 => b가 0이 될때까지 나머지연산과 나누기를 반복(유클리드 호제법)
    while (b != 0) :
        r = a % b
        a = b
        b = r
    return a

for i in range(length) :
    summary = 0
    for j in range(len(num_list[i])) :
        for k in range(j+1 , len(num_list[i])) :
            summary += gcd(num_list[i][j], num_list[i][k])
    print(summary)