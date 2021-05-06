# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_score = 0 # 최고 점수
    max_update = 0 # 최고점수가 갱신된 횟수
    
    min_score = 0 # 최저 점수
    min_update = 0 # 최저 점수가 갱신된 횟수
    
    for i in range(len(scores)) :
        if i == 0 : # 맨 첫번째 게임에서는 최초의 점수가 최고와 최저점수로 입력된다
            max_score = scores[i]
            min_score = scores[i]
        
        else :
            # 최대 점수를 갱신한 경우에, 갱신 횟수를 증가시킨다
            if scores[i] > max_score :
                max_score = scores[i]
                max_update += 1
            
            # 최저 점수를 갱신한 경우에, 갱신 횟수를 증가시킨다
            if scores[i] < min_score :
                min_score = scores[i]
                min_update += 1
        
           
    # 최대점수, 최저점수 순서대로 리스트에 값을 저장한다
    result = [max_update, min_update]
    return result