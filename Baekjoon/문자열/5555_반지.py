import sys

# 반지에 새겨진 글귀와, 비교할 반지의 갯수 n
target_ring = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
cnt = 0 # 일치한다면 카운트를 증가시킴 

for _ in range(n) :

    # 반지의 형태를 입력
    ring = sys.stdin.readline().rstrip()
    for i in range(len(ring)) :
        correct = 0
        for j in range(len(target_ring)) :
            # 만약 새겨진 반지의 철자가, target_ring의 철자와 일치하는지 확인
            if target_ring[j] == ring[(i+j)%len(ring)] :
                correct += 1

        # 만약, 문자열 길이부터 내용까지 target_ring과 일치한다면 반지 카운트를 1올린다
        if correct == len(target_ring) :
            cnt += 1
            break

# 내용 출력
print(cnt)