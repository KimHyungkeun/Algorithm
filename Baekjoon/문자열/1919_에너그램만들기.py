import sys

# 입력받은 두 문자열의 철자 각각을 저장하기위해 리스트로 설정
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

# 두 문자열에서 공통되는 철자를 구한다
intersect = set(a) & set(b)
intersect = list(intersect)


# 출현하는 공통문자의 빈도수 중, 적은 빈도수를 기억하기 위함
final_count = []

# 공통된 문자가 a,b 문자열에서 출현했을때, 더 적은횟수로 출현한것을 넣는다
for i in intersect :
    if a.count(i) < b.count(i) :
        final_count.append((i, a.count(i)))
    else :
        final_count.append((i, b.count(i)))

# 두 문자열의 길이 구함
length_a = len(a)
length_b = len(b)

# 서로 공통되는 부분만을 제외하면, 애너그램을 만들기위해 없어져야할 문자들만 남게된다
for f in final_count :
    length_a -= f[1]
    length_b -= f[1]

print(length_a + length_b)