import sys

asc_arr = [1,2,3,4,5,6,7,8]
dsc_arr = [8,7,6,5,4,3,2,1]

arr = list(map(int, sys.stdin.readline().split()))
if arr == asc_arr :
    print("ascending")

elif arr == dsc_arr :
    print("descending")

else :
    print("mixed")