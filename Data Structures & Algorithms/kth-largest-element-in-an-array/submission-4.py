class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. Sorting O(nlogn)
        # nums.sort()
        # return nums[-k]



        # 2. min heap of k size O(nlogk)
        # import heapq
        # return heapq.nlargest(k, nums)[-1]

        # Coding heap
        import heapq
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                heapq.heappushpop(heap, n)

        return heap[0]

        # 3. quick select average O(n)
