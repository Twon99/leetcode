class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 1
        if n ==0:
            return 0
        dq = deque()
        dq.append(s[i])
        ans = 1

        while j < n:
            if s[j] not in dq:
                dq.append(s[j])
                ans = max (ans , len(dq))
                j = j + 1
            else:
                while s[j] in dq:
                    dq.popleft()
                dq.append(s[j])
                i = j
                j = j + 1
        return ans
                
        