import sys

string = sys.stdin.readline().rstrip()
tmp_str = ""
arr = []

for w in string :
    if w != ' ' :
        tmp_str += w
    else :
        if len(tmp_str) == 0 :
            continue
        arr.append(tmp_str)
        tmp_str = ""


if len(tmp_str) >= 1 :
    arr.append(tmp_str)

# print(arr)
print(len(arr))
