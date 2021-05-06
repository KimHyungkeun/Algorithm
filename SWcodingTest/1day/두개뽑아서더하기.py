def solution(numbers):
    answer = []
    
    # 서로다른 인덱스끼리 뽑아서 덧셈을 실시한 후, 각기 다른 값들을 모두모아 오름차순 정렬
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) :
            if numbers[i] + numbers[j] not in answer :
                answer.append(numbers[i] + numbers[j])
    
    answer.sort()
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/68644