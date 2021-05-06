import math

r = int(input())
euclid_result = round(r * r * math.pi, 6) # 기존에 알고있는 원의 넓이 구하기
taxi_result = round(r * r * 2) # r*r*(1/2) * 4

print(euclid_result)
print(taxi_result)