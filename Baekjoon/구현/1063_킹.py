import sys

a, b, n = sys.stdin.readline().split()
n = int(n)

king = [ord(a[0]), int(a[1])]
stone = [ord(b[0]), int(b[1])]

# print(king, stone)
for _ in range(n) :
    cmd = sys.stdin.readline().rstrip()

    # 한 칸 오른쪽으로
    if cmd == 'R' :
        if king[0] + 1 <= 72 :
            king[0] += 1
            # king과 돌의 위치가 같을때, 돌도 똑같이 행동한다
            # 만약, 돌 또한 보드 밖으로 나가는 경우라면 이번 행동은 무효로 한다
            if king == stone :
                if stone[0] + 1 <= 72 :
                    stone[0] += 1
                
                else :
                    king[0] -= 1
            
    # 한 칸 왼쪽으로
    elif cmd == 'L' :
        if king[0] - 1 >= 65 :
            king[0] -= 1
            # king과 돌의 위치가 같을때, 돌도 똑같이 행동한다
            # 만약, 돌 또한 보드 밖으로 나가는 경우라면 이번 행동은 무효로 한다
            if king == stone :
                if stone[0] - 1 >= 65 :
                    stone[0] -= 1
            
                else :
                    king[0] += 1
    
    # 한 칸 아래로
    elif cmd == 'B' :
        if king[1] - 1 >= 1 :
            king[1] -= 1
            # king과 돌의 위치가 같을때, 돌도 똑같이 행동한다
            # 만약, 돌 또한 보드 밖으로 나가는 경우라면 이번 행동은 무효로 한다
            if king == stone :
                if stone[1] - 1 >= 1 :
                    stone[1] -= 1
                else :
                    king[1] += 1
    # 한 칸 위로
    elif cmd == 'T' :
        if king[1] + 1 <= 8 :
            king[1] += 1
            # king과 돌의 위치가 같을때, 돌도 똑같이 행동한다
            # 만약, 돌 또한 보드 밖으로 나가는 경우라면 이번 행동은 무효로 한다
            if king == stone :
                if stone[1] + 1 <= 8 :
                    stone[1] += 1
                else :
                    king[1] -= 1

    # 오른쪽 위 대각선
    elif cmd == 'RT' :
        if king[0] + 1 <= 72 and king[1] + 1 <= 8 :
            king[0] += 1
            king[1] += 1
            # king과 돌의 위치가 같을때, 돌도 똑같이 행동한다
            # 만약, 돌 또한 보드 밖으로 나가는 경우라면 이번 행동은 무효로 한다
            if king == stone :
                if stone[0] + 1 <= 72 and stone[1] + 1 <= 8 :
                    stone[0] += 1
                    stone[1] += 1
                else :
                    king[0] -= 1
                    king[1] -= 1
    # 왼쪽 위 대각선
    elif cmd == 'LT' :
        if king[0] - 1 >= 65 and king[1] + 1 <= 8 :
            king[0] -= 1
            king[1] += 1
            # king과 돌의 위치가 같을때, 돌도 똑같이 행동한다
            # 만약, 돌 또한 보드 밖으로 나가는 경우라면 이번 행동은 무효로 한다
            if king == stone :
                if stone[0] - 1 >= 65 and stone[1] + 1 <= 8 :
                    stone[0] -= 1
                    stone[1] += 1
                else :
                    king[0] += 1
                    king[1] -= 1

    # 오른쪽 아래 대각선
    elif cmd == 'RB' :
        if king[0] + 1 <= 72 and king[1] - 1 >= 1 :
            king[0] += 1
            king[1] -= 1
            # king과 돌의 위치가 같을때, 돌도 똑같이 행동한다
            # 만약, 돌 또한 보드 밖으로 나가는 경우라면 이번 행동은 무효로 한다
            if king == stone :
                if stone[0] + 1 <= 72 and stone[1] - 1 >= 1 :
                    stone[0] += 1
                    stone[1] -= 1
                else :
                    king[0] -= 1
                    king[1] += 1

    # 왼쪽 아래 대각선으로
    elif cmd == 'LB' :
        if king[0] - 1 >= 65 and king[1] - 1 >= 1 :
            king[0] -= 1
            king[1] -= 1
            # king과 돌의 위치가 같을때, 돌도 똑같이 행동한다
            # 만약, 돌 또한 보드 밖으로 나가는 경우라면 이번 행동은 무효로 한다
            if king == stone :
                if stone[0] - 1 >= 65 and stone[1] - 1 >= 1 :
                    stone[0] -= 1
                    stone[1] -= 1
                else :
                    king[0] += 1
                    king[1] += 1
    
    # print(king, stone)
    

print(chr(king[0]) + str(king[1]))
print(chr(stone[0]) + str(stone[1]))

        
            