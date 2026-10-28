class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {} # val : idx

        for j, n in enumerate(nums):
            diff = target - n
            if diff in nums_dict:
                i = nums_dict[diff]
                return [i, j]

            nums_dict[n] = j
