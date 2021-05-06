import sys

string = sys.stdin.readline().rstrip()
replace_string = string.replace("pi","00").replace("ka","00").replace("chu","000")
array = list(replace_string)

if array.count('0') == len(string) :
    print("YES")
else :
    print("NO")