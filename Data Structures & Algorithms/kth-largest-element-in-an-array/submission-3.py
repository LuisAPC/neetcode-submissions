class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. Sorting O(nlogn)
        # nums.sort()
        # return nums[-k]



        # 2. min heap of k size O(nlogk)
        import heapq
        return heapq.nlargest(k, nums)[-1]
        # 3. quick select average O(n)
