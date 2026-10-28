class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for n in nums:
            nums_set.add(n)

        longest_seq = 0
        for n in nums_set:
            if n-1 in nums_set:
                continue
            
            i=n
            curr_seq = 0
            while i in nums_set:
                curr_seq += 1
                i += 1

            longest_seq = max(longest_seq, curr_seq)
        return longest_seq