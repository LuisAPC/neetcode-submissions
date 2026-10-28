class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_lenght = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest_lenght = max(longest_lenght, r-l+1)
            
        return longest_lenght
            