class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 문자열을 모두 소문자로 바꿈
        paragraph = paragraph.lower()
        word_dict = {} # 단어별 등장 빈도수를 저장하기 위한 딕셔너리
        
        
        tmp = ""
        for p in paragraph :
            # 알파벳만 담기위한 tmp 임시변수 설정
            if 'a' <= p <= 'z' :
                tmp += p
            else :
                # 만약 해당 단어가 금지어거나 빈칸이면 탐색 취소
                if tmp in banned or not tmp :
                    tmp = ""
                    continue
                
                # 해당 단어가 딕셔너리에 존재하면 갯수 증가
                if tmp in word_dict :
                    word_dict[tmp] += 1
                # 그렇지 않다면 딕셔너리에 새로 추가
                else :
                    word_dict[tmp] = 1
                
                # 임시변수 초기화
                tmp = ""
        
        # 혹시 모를 단어누락을 위해 한번 더 탐색
        if tmp in word_dict :
            word_dict[tmp] += 1
        else :
            word_dict[tmp] = 1
        
        # 단어별 등장 빈도수를 기준으로 내림차순 정렬
        print(word_dict)
        result = sorted(word_dict.items(), key = lambda x : x[1], reverse=True)
        
        return result[0][0]