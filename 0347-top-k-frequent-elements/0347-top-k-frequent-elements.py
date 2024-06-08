class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frq = [[] for _ in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        print(count)
        for n,c in count.items():
            frq[c].append(n)
        print(frq)
        res = []
        for i in range(len(frq)-1,0,-1):
            for c in frq[i]:
                res.append(c)
                if (len(res) == k):
                    return res
                