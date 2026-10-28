class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nums_dict = Counter(nums)

        freq_list = [[] for _ in range(len(nums) + 1)] # idx = freq, val = num
        for n, freq in nums_dict.items():
            freq_list[freq].append(n)

        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if k == len(res):
                    return res
