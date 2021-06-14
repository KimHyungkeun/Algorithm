def rotateLeft(d, arr):
    # Write your code here

    # d번 만큼 arr의 앞부분을 맨 뒷부분으로 보내는 작업을 반복한다
    for _ in range(d) :
        arr.append(arr.pop(0))
    
    return arr