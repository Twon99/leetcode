class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_map = defaultdict(int)

        for c in s:
            hash_map[c] +=1
        for c in t:
            hash_map[c] -=1
        for val in hash_map.values():
            if val != 0:
                return False
        return True