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

        l = 0
        r = len(nums)-1
        #search right side
        if nums[pivot] <= target <= nums[r]:
            l = pivot
            r = len(nums)-1
        #search left side
        else:
            l = 0
            r = pivot-1
        return binary_search(l, r)
  