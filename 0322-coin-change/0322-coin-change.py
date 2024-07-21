class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def help(ind, target , dp):
            if ind == 0:
                if target % coins[ind] == 0:
                    return int(target // coins[ind])
                else:
                    return 1e9
            if dp[ind][target] != -1:
                return dp[ind][target]
            
            not_take = 0 + help( ind - 1, target, dp)

            take = 1e9
            if coins[ind] <= target:
                take = 1 + help(ind, target - coins[ind], dp)
            dp[ind][target] = min(take , not_take)
            return dp[ind][target]
        if amount == 0:
            return 0
        dp = [[-1 for j in range(amount + 1)] for i in range(len(coins))]
        ans = help(len(coins) - 1, amount, dp)

        if ans >= int(1e9):
            return -1
        else:
            return ans
        