class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        longest_lenght = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in s_set:
                s_set.remove(s[l])
                l += 1
                continue
            s_set.add(s[r])
            r += 1
            longest_lenght = max(longest_lenght, r-l)
            
        return longest_lenght
            