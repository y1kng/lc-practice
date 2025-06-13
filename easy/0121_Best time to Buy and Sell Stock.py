class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        his_low = prices[0]
        big_money = 0
        hao = 0
        for wyk in range(len(prices) - 1):
            if prices[wyk+1] <= prices[wyk]:
                hao += 1
        if hao == len(prices) - 1:
            return 0
        else:
            for kn in prices:
                his_low = min(his_low, kn)
                big_money = max(big_money, kn - his_low)
            return big_money
        