class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_except_self = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            product_except_self[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            product_except_self[i] *= postfix
            postfix *= nums[i]

        return product_except_self