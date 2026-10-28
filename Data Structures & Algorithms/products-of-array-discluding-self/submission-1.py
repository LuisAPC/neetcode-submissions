class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        for i in range(len(res)):
            res[i] = pre
            pre *= nums[i]

        pos = 1
        for i in range(len(res)-1, -1, -1):
            res[i] *= pos
            pos *= nums[i]

        return res
