class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane, one loop O(n), no sort because the order matters, use of max(counter, current)

        # # Brute force
        # profit = 0

        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         profit = max(profit, sell - buy)
        # return profit 

        # two pointers
        l, r = 0,1
        profit = 0

        while r <= len(prices) - 1:
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit