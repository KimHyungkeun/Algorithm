class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(idx, path) :
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits) :
                result.append(path)
                return
            
            # 입력값 자릿수 단위 반복
            for i in range(idx, len(digits)) :
                for j in numbers[digits[i]] :
                    dfs(i + 1, path + j)
        
        if not digits :
            return []
        
        numbers = {'2' : ['a','b','c'], '3' : ['d','e','f'], '4' : ['g','h','i'], '5' : ['j', 'k', 'l'],
                  '6' : ['m','n','o'], '7' : ['p','q','r','s'], '8' : ['t','u','v'], '9' : ['w','x','y','z']}
        
        result = []
        dfs(0, "")
        
        return result