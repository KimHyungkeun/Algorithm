# 의도 : a 배열에 대한 최소공배수의 배수 리스트와, b 배열의 최대공약수의 약수 리스트를 구해서 두 리스트의 공통요소를 발견   

# 210514 풀이
def gcd(a, b) :
    while b != 0 :
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b) :
    g = gcd(a, b)
    return g * (a//g) * (b//g)

def getTotalX(a, b):
    # Write your code here
    cnt = 0
    a.sort()
    b.sort()
    
    if a[-1] > b[0] :
        a,b = b,a
    
    q_a = deque(a)
    q_b = deque(b)
    
    while len(q_a) != 1 :
        x = q_a.popleft()
        y = q_a.popleft()
        ans = lcm(x, y)
        q_a.appendleft(ans)
    
    while len(q_b) != 1 :
        x = q_b.popleft()
        y = q_b.popleft()
        ans = gcd(x, y)
        q_b.appendleft(ans)
    
    l = q_a[0]
    g = q_b[0]
    
    if l > g :
        l, g = g, l
    
    for i in range(l, g+1) :
        flag = True
        for j in a :
            if i % j != 0 :
                flag = False
                break 
        
        if flag :
            for j in b :
                if j % i != 0 :
                    flag = False
                    break
        
        if flag :
            cnt += 1
    
    return cnt

# 210512 : 위에 서술한 의도보고 풀었기 때문에 완전히 이해했다고 할수 없음
# def gcd (a,b) :
#     while b != 0 :
#         r = a % b
#         a = b
#         b = r       
#     return a

# def lcm(a, b) :
#     g = gcd(a,b)
#     return int(g * (a/g) * (b/g))


# def getTotalX(a, b):
#     # Write your code here
#     sorted_a = sorted(a, reverse=True)
#     sorted_b = sorted(b, reverse=True)
#     if sorted_a[-1] > sorted_b[0] :
#         sorted_a, sorted_b = sorted_b, sorted_a
        
#     while len(sorted_a) != 1 :
#         tmp1 = sorted_a.pop()
#         tmp2 = sorted_a.pop()
#         g = lcm(tmp1, tmp2)
#         sorted_a.append(g)
    
#     while len(sorted_b) != 1 :
#         tmp1 = sorted_b.pop()
#         tmp2 = sorted_b.pop()
#         g = gcd(tmp1, tmp2)
#         sorted_b.append(g) 
    
#     a_gcd = sorted_a[0]
#     b_gcd = sorted_b[0]
#     print(a_gcd, b_gcd)
    
#     if a_gcd > b_gcd :
#         a_gcd, b_gcd = b_gcd, a_gcd
    
#     a.sort()
#     b.sort()
    
#     cnt = 0
#     for i in range(a_gcd, b_gcd+1) :
#         flag = True
#         for j in a :
#             if i % j != 0 : 
#                 flag = False
#                 break
        
#         for j in b :
#             if j % i != 0 :
#                 flag = False
#                 break
        
#         if flag :
#             cnt += 1
    
#     return cnt
        


# def GCD(a, b): 
#     while b != 0 : #b가 0이 아닌 동안 반복
#         a, b = b, a%b #a에 b를, b에 a와 b를 나눈 나머지를 교환하여 저장(스왑)
#     return a #반환되는 a가 두 수의 최대공약수

# def getTotalX(a, b):
#     # Write your code here
#     a.sort()
#     b.sort()
    
#     # a 배열에 존재하는 수들의 최소공배수를 구함
#     GCDarr = a[0] #arr 리스트의 첫 번째 항목(0번 방)을 GCDarr에 저장
#     LCMarr = a[0] #arr 리스트의 첫 번째 항목(0번 방)을 LCMarr에 저장
#     for i in range(len(a)): #i가 0부터 리스트 arr의 길이만큼 반복     
#         GCDarr = GCD(LCMarr, a[i]) # GCDarr에 LCMarr과 arr[i]의 최대공약수를 저장 
#         LCMarr = LCMarr * a[i] // GCDarr #LCMarr에 LCMarr과 arr[i]의 최소공배수를 저장
    
#     # b배열에 존재하는 수들의 최대공약수를 구함
#     B_arr = b[0]
#     for i in range(len(b)) :
#         B_arr = GCD(B_arr, b[i])
    
#     # b의 최대공약수의 약수를 구한다
#     B_CD = []
#     for i in range(1, B_arr+1) :
#         if B_arr % i == 0 :
#             B_CD.append(i)
    
#     # b의 최대공약수 범위 이내까지, a의 배수를 구한다
#     A_CM = []
#     i = 1
#     while LCMarr * i <= B_arr :
#         A_CM.append(LCMarr * i)
#         i += 1
    
#     # a와 b의 공통 요소들을 찾아낸다
#     intersect = list(set(B_CD) & set(A_CM))
#     # print(intersect)

#     # 공통 요소들의 갯수를 구한다
#     answer = len(intersect)
    
            
#     return answer