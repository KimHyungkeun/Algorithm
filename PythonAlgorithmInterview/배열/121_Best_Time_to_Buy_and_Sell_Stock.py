import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 이율
        profit = 0
        # 최소 가격
        min_price = sys.maxsize
        
        for price in prices :
            # 현재 가격과, 최소 가격을 비교하여 최소가격을 갱신
            min_price = min(min_price, price)
            # 현재 이득과 새로운 값에대한 이득중 최대값인 것을 갱신
            profit = max(profit, price - min_price)
        
        return profit