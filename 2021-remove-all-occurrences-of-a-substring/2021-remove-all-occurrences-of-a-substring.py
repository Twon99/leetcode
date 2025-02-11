class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        res = []
        for c in s:
            res.append(c)
            if len(res) >= len(part):
                last_n_elements = res[-len(part):]  # Get last n elements
                result = "".join(map(str, last_n_elements))  # Convert to string
                
                while result == part:
                    res = res[:len(res) - len(part)]
                    last_n_elements = res[-len(part):]  # Get last n elements
                    result = "".join(map(str, last_n_elements))  # Convert to string
        
        return "".join(map(str, res))

        