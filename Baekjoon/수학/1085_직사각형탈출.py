x, y, w, h = map(int, input().split())

diff_w = abs(w-x) # x좌표만을 기준으로 최대 경계선까지의 거리
diff_h = abs(h-y) # y좌표만을 기준으로 최대 경계선까지의 거리

array = [diff_w, diff_h, abs(x), abs(y)] # x,y 좌표를 기준으로 직사각형 경계선에 닿을수있는 모든 경우의 수

print(min(array)) 