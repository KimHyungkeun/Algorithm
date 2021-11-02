import sys

alphabet = {chr(w):-1 for w in range(97, 123)}
word = sys.stdin.readline().rstrip()
# print(alphabet)

for i in range(len(word)) :
    if alphabet[word[i]] == -1 :
        alphabet[word[i]] = i

for key in alphabet.keys() :
    print(alphabet[key], end=' ')