def swap_case(s):
    s = list(s)
    for i in range(len(s)) :
        if 'a' <= s[i] <= 'z' :
            word = s[i].upper()
            s[i] = word
        elif 'A' <= s[i] <= 'Z' :
            word = s[i].lower()
            s[i] = word
        else :
            continue
        
    return ''.join(s)  

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)