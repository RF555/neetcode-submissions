class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0
        max_diff = 0
        for r in range(1, len(prices)):
            curr_diff = prices[r] - prices[l]
            max_diff = max(max_diff, curr_diff)

            if prices[l] > prices[r]:
                l = r
        return max(max_diff, 0)