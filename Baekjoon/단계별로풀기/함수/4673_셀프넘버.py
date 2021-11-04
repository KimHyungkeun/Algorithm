def d(n) :
    val = n
    list_num = list(str(val))

    for i in list_num :
        val += int(i)
    
    return val


generate_num = []   
for i in range(1, 10001) :
    generate_num.append(d(i))

for i in range(1, 10001) :
    if i not in generate_num :
        print(i)