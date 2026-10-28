class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            m = (l+r) // 2
            cur_h = 0
            for b in piles:
                cur_h += b//m + 1 if b%m else b//m
            
            if cur_h <= h:
                k = min(k, m)
                r = m-1
            elif cur_h > h:
                l = m+1

        return k