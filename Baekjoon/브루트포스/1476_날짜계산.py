e,s,m = input().split()
e = int(e)
s = int(s)
m = int(m)

# print(e,s,m)

tmp_e = 0
tmp_s = 0
tmp_m = 0
year = 0

while True :
    tmp_e += 1
    tmp_s += 1
    tmp_m += 1
    year += 1

    if tmp_e > 15 :
        tmp_e = 1

    if tmp_s > 28 :
        tmp_s = 1

    if tmp_m > 19 :
        tmp_m = 1

    if tmp_e == e and tmp_s == s and tmp_m == m :
        break;    

print(year)