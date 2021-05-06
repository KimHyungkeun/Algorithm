# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    
    alpha_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 
    'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23,
    'x':24, 'y':25, 'z':26} 

    set_s = set(list(s))
    
    s_cnt = []
    weight = set([])
    answer = []
    for e in set_s :
        s_cnt.append((e, list(s).count(e)))
    print(s_cnt)
    for e in s_cnt :
        for i in range(1, e[1]+1) :
            weight.add(alpha_dict[e[0]]*i)
    
    # print(weight)
    # weight = list(weight)
    for i in range(len(queries)) :
        if queries[i] in weight :
            answer.append("Yes")
        else :
            answer.append("No")
    
    
    
    return answer