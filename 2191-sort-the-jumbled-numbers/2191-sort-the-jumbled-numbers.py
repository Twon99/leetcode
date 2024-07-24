class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        hashmap = {index: value for index, value in enumerate(mapping)}

        #print(hashmap)

        res = {}

        for numbers in nums:
            temp = ''
            for digit in str(numbers):
                temp += str(hashmap[int(digit)])
            if not numbers in res:
                res[numbers] = [int(temp) , 1]
            else:
                count = res[numbers][-1]
                res[numbers] = [int(temp) , count + 1]
        print(res)
        
        ans = dict(sorted(res.items(), key=lambda item: item[1]))
        final_res = []
        for key, (value, count) in ans.items():
            final_res.extend([key] * count)
        return final_res

        