class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        #find pivot
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        pivot = l

        #regular binary search on corresponding size
        def binary_search(l: int, r:int) -> int:
            while l <= r:
                m = (l+r) // 2
            
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return -1


        #search right side
        if nums[pivot] <= target <= nums[-1]:
            return binary_search(pivot, len(nums)-1)
        #search left side
        return binary_search(0, pivot-1)
  