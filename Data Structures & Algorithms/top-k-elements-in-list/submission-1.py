class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        nums_dict = Counter(nums)
        res = nums_dict.most_common(k)
        res1 = []
        for r in res:
            res1.append(r[0])
        return res1