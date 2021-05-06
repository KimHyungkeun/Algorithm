import sys

# 책의 갯수 n
n = int(sys.stdin.readline())
book_dict = {}

# 팔린 책들을 입력
for _ in range(n) :
    book = input()
    if book in book_dict :
        book_dict[book] += 1
    else :
        book_dict[book] = 1

# 책들을 가장 많이 팔린 순으로 정렬
sort_by_quantity = sorted(book_dict.items(), key = lambda x : x[1], reverse=True)

sort_by_alphabet = []
maximum = sort_by_quantity[0][1]


# 만약 최고 판매수가 중복되는 경우에는 알파벳 순서대로 정렬한다
i = 0
while i < len(sort_by_quantity):
    if sort_by_quantity[i][1] == maximum :
        sort_by_alphabet.append(sort_by_quantity[i])
    else :
        break   
    i += 1

# 알파벳 순서대로 정렬

sort_book = sorted(sort_by_alphabet, key = lambda x : x[0])
print(sort_book[0][0])

