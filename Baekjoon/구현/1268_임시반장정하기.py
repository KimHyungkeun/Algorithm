# python3 시간초과, pypy3 가능
import sys

n = int(sys.stdin.readline())

# 학생 수 입력
student = {i:[] for i in range(1, n+1)}

# 각 학생의 1 ~ 5학년 까지의 배정 반
classes = []
for _ in range(n) :
    arr = list(map(int, sys.stdin.readline().split()))
    classes.append(arr)

# 각 학생별로 해당 학년에 한번이상이라도 같은반이었던 친구 찾아내기
for i in range(n) :
    for j in range(5) :
       for k in range(n) :
           if i == k :
                continue
           if classes[k][j] == classes[i][j] and k+1 not in student[i+1] :
               student[i+1].append(k+1)

# print(student) 

# 다양한 학생들 사이에서, 같은반을 많이 경험한 친구를 우선시 한다
result = []
for key,val in student.items() :
    result.append((key, val))
result.sort(key = lambda x : len(x[1]), reverse=True)

# print(result)

# 만약 여러 학우들과 같은반이 된 경우의수가 모두 같으면, 학생 번호가 작은것을 고른다
final_result = []
max_length = len(result[0][1])
for r in result :
    if len(r[1]) == max_length :
        final_result.append(r)
    else :
        break
# print(final_result)
final_result.sort(key = lambda x : x[0])
print(final_result[0][0])


