class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        else:
            curr = 0
            end = 1
            maxProfit = 0
            while end < len(prices):
                currProfit = prices[end] - prices[curr]
                if prices[curr] < prices[end]:
                    maxProfit = max(currProfit, maxProfit)
                else:
                    curr = end

                end += 1

            return maxProfit

# New "buy" price would always do better than old one for any "better" sell price
