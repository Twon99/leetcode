class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        n = len(prices)
        max_prof = 0
        while(i < n and j < n):
            if ( prices[i] > prices[j]):

                i = j
                j = i + 1
            else:
                max_prof = max(max_prof, prices[j] - prices[i])
                #i = i + 1
                j = j + 1
        return max_prof
        