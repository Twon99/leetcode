class Solution:
    def isPalindrome(self, s: str) -> bool:
        re = ""
        se = ""
        
        for c in range(0, len(s), 1):
            if s[c].isalnum():
                se += s[c].lower()
            d = len(s)-c-1
            if s[d].isalnum():
                re += s[d].lower()
            
        print(se)
        print(re)
        if re != se:
            return False
        return True
        