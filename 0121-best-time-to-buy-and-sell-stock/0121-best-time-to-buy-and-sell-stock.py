class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        min_price = prices[0]  # 초기 최소 가격은 첫 번째 가격으로 설정
        max_profit = 0  # 최대 이익 초기값은 0으로 설정
        
        for price in prices[1:]:
            min_price = min(min_price, price)  # 현재 가격과 최소 가격 중 작은 값을 선택하여 업데이트
            max_profit = max(max_profit, price - min_price)  # 현재 가격에서 최소 가격을 뺀 값과 최대 이익 중 큰 값을 선택하여 업데이트
        
        return max_profit