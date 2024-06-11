class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        i = 0
        n = len(s)
        j = 1
        dq = deque()
        dq.append(s[i])
        lon = 1
        while(i<n and j<n):
            if s[j] not in dq:
                dq.append(s[j])
                lon = max(lon, len(dq))
                j = j + 1
            else:
                while(s[j] in dq):
                    dq.popleft()
                dq.append(s[j])
                i = i + 1
                j = j + 1
        return lon
                    
        