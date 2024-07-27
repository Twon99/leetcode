class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def lcs(string1, string2):
            dp = [[0] * (len(string2)+1) for _ in range(len(string1)+1)]

            for index1 in range(len(string1)):
                for index2 in range(len(string2)):
                    if string1[index1] == string2[index2]:
                        dp[index1+1][index2+1] = dp[index1][index2] + 1
                    else:
                        dp[index1+1][index2+1] = max(dp[index1][index2+1],dp[index1+1][index2])
            
            return dp[-1][-1]
        
        return lcs(s, s[::-1])