import sys

# 줄의 갯수 n
n = int(sys.stdin.readline())

# 각 줄이 종류를 담을 배열
rope = []
for _ in range(n) :
    # 각 줄이 최대 버틸 수 있는 무게를 입력
    num = int(sys.stdin.readline())
    rope.append(num)

# 가장 무거운 물체를 버틸수있는 순서대로 줄을 배열해놓음
rope.sort(reverse=True)

# n개의 줄이 주어졌을때, 1개 줄부터 n개의 줄까지 모두 사용하였을때
# 그 중 , 가장 무거웠던 무게를 찾아낸다. 
# ex) 15, 10 이 있을때, 1개 줄 일때는 15kg가 최대한계이나 
# 2개일 때는 15kg중의 10kg , 10kg중의 10kg를 동등 분산하여 총 20kg 무게가 가능
max_kg = 0
for i in range(0, n) :
    if rope[i] * (i+1) > max_kg :
        max_kg = rope[i] * (i+1)

print(max_kg)