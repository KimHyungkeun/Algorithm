def repeatedString(s, n):
    
    add_on = n // len(s) # 길이 n이 주어졌을때, 슬라이싱 없이 s문자열 그대로를 복제할수 있는 갯수
    remain = n % len(s) # add_on 갯수만큼 붙인 후, 길이 n을 채우기위한 s의 부분문자열 길이
   
    lists = list(s) # 해당 문자열을 리스트화 시킨다
    count_a = lists.count('a') # 해당 문자열에 들어있는 a의 갯수
    remain_a = lists[:remain].count('a') # 슬라이싱 후의 부분문자열에 들어있는 a의 갯수
    return count_a * add_on + remain_a # add_on 만큼의 a의 갯수를 센 후, 나머지 a의 갯수를 마저 센다