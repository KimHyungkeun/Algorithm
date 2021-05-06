import sys

n = int(sys.stdin.readline())

student = {}
for _ in range(n) :
    name, kor, eng, math = sys.stdin.readline().split()
    student[name] = (int(kor), int(eng), int(math))

# 4. 이름 사전순대로 정렬
name_sort = sorted(student.items(), key = lambda x : x[0])
# 3. 수학 점수를 높은점수부터 내림차순 정렬
math_sort = sorted(name_sort, key = lambda x : x[1][2], reverse=True)
# 2. 영어점수를 낮은점수부터 오름차순 정렬
eng_sort = sorted(math_sort, key = lambda x : x[1][1])
# 1. 국어점수를 내림차순 정렬
kor_sort = sorted(eng_sort, key = lambda x : x[1][0], reverse=True)

for n in kor_sort :
    print(n[0])