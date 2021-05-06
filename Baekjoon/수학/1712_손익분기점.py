a,b,c = map(int, input().split()) # a는 고정비용, b는 판매량에 따른 가변비용, c는 판매비용

if b >= c :
    print(-1) #만약 가변비용이 판매비용보다 높으면 -1 출력

else :
    n = int(a / (c - b))
    n += 1
    print(n)