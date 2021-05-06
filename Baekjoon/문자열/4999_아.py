import sys

# 재환이와 의사가 각각 할 수있는 aaah를 입력한다
jaehwan = sys.stdin.readline().rstrip()
doctor = sys.stdin.readline().rstrip()

# 만약 의사가 원하는 길이보다 적다면 가선 안되고, 원하는 길이 이상이 된다면 가도 된다
if len(jaehwan) < len(doctor) :
    print("no")

else :
    print("go")