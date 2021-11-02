import sys

word = sys.stdin.readline().rstrip()
word = word.upper()
word_cnt = {}

for w in word :
    if w in word_cnt :
        word_cnt[w] += 1
    else :
        word_cnt[w] = 1

max_val = max(word_cnt.values())

cnt = 0
for val in word_cnt.values() :
    if val == max_val :
        cnt += 1
    
    if cnt >= 2 :
        break

if cnt >= 2 :
    print("?")

else :
    for key,val in word_cnt.items() :
        if val == max_val :
            print(key)
            break
