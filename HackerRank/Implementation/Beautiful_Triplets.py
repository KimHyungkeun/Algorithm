# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):

    # 중복 출현을 피하기위해 set로 임시변환 후, 다시 리스트로 변환
    arr = list(set(arr))
    arr.sort(reverse=True) # 내림차순 정렬
    cnt = 0 # (a,b,c)가 있을때 a-b == b-c == d 인 트리플렛이 형성되는 갯수
    
    for i in range(len(arr)) :      
        for j in range(i+1, len(arr)) :
            # 가장 최초로 나올 두 수의 차가 d인지 먼저 확인한다
            if arr[i] - arr[j] == d :
                triplet = [arr[i], arr[j]]
                
                # triplet의 마지막 숫자에서 d를 뺐을 때 결과값이 arr에 등장하는지 확인
                if triplet[-1] - d in arr :
                    triplet.append(triplet[-1] - d)
                
                # 트리플렛 출력
                print(triplet)
                
                # 만약 잘 형성되었다면 카운트를 올린다
                if len(triplet) == 3 :
                    cnt += 1
                    break
                         
    return cnt