class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {} #key=num val=idx

        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in nums_dict:
                i = nums_dict[diff]
                return [i, j]

            nums_dict[nums[j]] = j 

        return False