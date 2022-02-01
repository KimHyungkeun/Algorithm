def solution(numbers):
    answer = []
    
    for num in numbers :
        bin_num = list('0' + bin(num)[2:])
        idx = ''.join(bin_num).rfind('0')
        bin_num[idx] = '1'
        
        if num % 2 == 1 :
            bin_num[idx+1] = '0'
        
        answer.append(int(''.join(bin_num), 2))
    return answer

# https://velog.io/@kerri/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Lv2-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8