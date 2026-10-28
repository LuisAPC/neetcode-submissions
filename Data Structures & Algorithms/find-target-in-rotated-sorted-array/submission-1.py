class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        res = -1
        while l <= r:
            m = (l+r) // 2
            num = nums[m]
            if num == target:
                res = m
                break
            #left part
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m+1
                else:
                    r = m-1
            #right part
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1
        return res

        #[3,4,[5],6,!1,2]