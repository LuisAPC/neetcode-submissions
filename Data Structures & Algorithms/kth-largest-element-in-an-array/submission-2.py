class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. Sorting O(nlogn)
        nums.sort()
        return nums[-k]



        # 2. min heap of k size O(nlogk)
        # 3. quick select average O(n)
