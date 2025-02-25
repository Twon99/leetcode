class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged = []
        M = len(nums1)
        N = len(nums2)
        ptr1 = 0
        ptr2 = 0

        while(ptr1<M and ptr2<N):
            if nums1[ptr1]<=nums2[ptr2]:
                merged.append(nums1[ptr1])
                ptr1+=1
            else:
                merged.append(nums2[ptr2])
                ptr2+=1
        
        while(ptr1<M):
            merged.append(nums1[ptr1])
            ptr1+=1
        while(ptr2<N):
            merged.append(nums2[ptr2])
            ptr2+=1
        L = len(merged)
        if L%2==0:
            # even
            mid = L//2
            return ((merged[mid-1]+merged[mid])/2)
        else:
            mid = L//2
            return merged[mid]
        
