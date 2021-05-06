import sys

n, k = sys.stdin.readline().strip().split()

n = int(n)
k = int(k)

queue = []
answer = []
pos = 0

for i in range(1, n+1) :
    queue.append(i)

for i in range(n):
    move = k - 1
    
    pos += move

    if pos >= len(queue) :
        pos = pos % len(queue) 
    
    answer.append(str(queue.pop(pos)))

length = len(answer)
answer_str = "<"
for i in range(length) :
    answer_str += answer[i]
    if i == length - 1 :
        break
    answer_str += ", "
answer_str += ">"
print(answer_str)



