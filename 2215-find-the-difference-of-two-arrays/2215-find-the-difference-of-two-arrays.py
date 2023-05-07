class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1Set = set(nums1)
        nums2Set = set(nums2)
        res1 = set()
        res2 = set()
        for i in nums1:
            if i not in nums2Set:
                res1.add(i)

        for i in nums2:
            if i not in nums1Set:
                res2.add(i)
        
        return[list(res1), list(res2)]
