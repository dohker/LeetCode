class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        current_price = prices[0]  # 현재까지의 최소 가격을 저장할 변수
        max_profit = 0  # 최대 이익 초기값은 0으로 설정
        
        for price in prices[1:]:
            if price > current_price:
                # 현재 가격이 최소 가격보다 큰 경우
                max_profit = max(max_profit, price - current_price)  # 최대 이익 업데이트
            else:
                # 현재 가격이 최소 가격보다 작은 경우
                current_price = price  # 최소 가격 업데이트
        
        return max_profit