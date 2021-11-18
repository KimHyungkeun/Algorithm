class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        # 로그의 형태를 담아놓는 리스트
        log_list = []
        for l in logs :
            # 공백을 기준으로 키워드와 내용을 분류한다 (tuple로 만듦)
            keyword = l.split()
            log_list.append((keyword[0], " ".join(keyword[1:])))
        
        total_list = [] # 내용이 영어단어인 것에 대한 로그를 담음 (추후에, num_list와 결합 예정)
        num_list = [] # 내용이 숫자인 것에 대한 로그를 담음
        
        for l in log_list :
            # 내용이 숫자인 문자열은 num_list에 담음(내용이 숫자인 것은 입력된 순서대로 집어넣는다)
            if '0' <= l[1][0] <= '9' :
                num_list.append(l)
            # 내용이 영단어인 문자열은 total_list에 담음
            else :
                total_list.append(l)
        
        # 내용이 영단어인 문자열은 가장 첫번째 키워드를 중심으로 정렬한 후, 영단어 내용의 사전적 순서대로 정렬한다.
        # 그 후, 나머지 num_list에 대한 내용을 담는다 
        total_list.sort(key = lambda x : x[0])
        total_list.sort(key = lambda x : x[1])
        total_list += num_list
        
        # tuple로 담았던 내용을 다시 문자열을 수복시킨다
        result = []
        for t in total_list :
            result.append(t[0] + " " + t[1])
        
        print(result)
        return result