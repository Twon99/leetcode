class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        hashset = {}
        final_min = float('inf')
        for i, n in enumerate(cards):
            #print("\ni = ", i)
            #print("\nn = ", n)
            #print("\nhashset", hashset.values())
           
            if n in hashset:
                final_min = min(final_min, (i - hashset[n] + 1))
            
            hashset[n] = i

        return final_min if final_min != float('inf') else -1