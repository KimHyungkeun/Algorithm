# Down-Top 방식
class Solution:
    def fib(self, n: int) -> int:
        fibonacci = [0,1] + [0]*(n-1)
        
        for i in range(2, n+1) :
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        
        return fibonacci[n]

# Top-Down 방식 
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1 :
            return n
        else :
            return self.fib(n-1) + self.fib(n-2)

# 메모리 최적화
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 :
            return 0
        
        elif n == 1 :
            return 1
        
        else :
            fibonacci = [0,1]
            idx = 2
            
            while idx != n :
                tmp = fibonacci[1]
                fibonacci[1] = sum(fibonacci)
                fibonacci[0] = tmp
                idx += 1
            
            return sum(fibonacci)