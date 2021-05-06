from itertools import permutations
import sys


l, c = map(int, sys.stdin.readline().split())
word = list(sys.stdin.readline().split())

all_cases = list(permutations(word, l))
vowls = ['a','e','i','o','u']

sorted_set = []
size = len(all_cases)

# 1. 암호의 패턴을 알파벳 순서대로 정렬
for i in range(size) :
    newlist = list(all_cases[i])
    newlist.sort()
    password = ''.join(newlist)
    if password not in sorted_set :
        sorted_set.append(password)

# 2. 모음이 최소 1개 이상이고, 자음이 2개이상 이어야 함
i = 0
while i < len(sorted_set) :
    count_vowl = 0
    count_consonant = 0
    # 자음과 모음 갯수를 센다
    for j in range(len(sorted_set[i])) :
        if sorted_set[i][j] in vowls :
            count_vowl += 1
        else :
            count_consonant += 1
    # 조건에 충족하지 않을경우, 해당 암호를 제외
    if count_vowl < 1 or count_consonant < 2 :
        del sorted_set[i]
        i -= 1
    
    else :
        i += 1    
    
    

# 3. 조건에 맞지 않는 암호는 지우고, 남은 암호들은 알파벳 순서대로 정렬
sorted_set.sort()
for i in range(len(sorted_set)) :
    print(sorted_set[i])

