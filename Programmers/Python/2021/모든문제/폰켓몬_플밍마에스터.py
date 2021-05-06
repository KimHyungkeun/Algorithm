def solution(nums):
    answer = 0
    select = len(nums) // 2 # 뽑아야할 폰켓몬 최대 갯수는, nums 길이의 절반이다
    set_nums = set(nums) # 폰켓몬 종류 갯수는 set_nums 개이다
    
    if select < len(set_nums) : # 만약 뽑아야할 최대갯수가, set_nums보다 작다면 select가 최대갯수이다
        answer = select
    else : # 그렇지 않다면, 폰켓몬 종류 전체 갯수가 답이다
        answer = len(set_nums)
    
    return answer