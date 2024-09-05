class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:



        sum_M = sum(rolls)

        sum_N = (mean) * (len(rolls) + n) - sum_M

        if n <= sum_N <= (6 * n):
            print(sum_N)
            array_val = sum_N // n
            res = [array_val] * n
            mod_N = sum_N % n
            for i in range(0, mod_N):
                res[i] += 1

            return res
             
        else:
            return []

        