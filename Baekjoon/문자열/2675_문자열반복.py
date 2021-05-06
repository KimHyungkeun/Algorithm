num = int(input())

for k in range(num) :
    value = input()
    n = int(value.split(" ")[0])
    s = value.split(" ")[1]

    if s == ' ' :
        continue

    for i in range(len(s)) :
        for _ in range(n) :
            print(s[i], end='')
    print()