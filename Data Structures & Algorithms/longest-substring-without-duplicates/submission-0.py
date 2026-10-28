class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      
        max_sub = 0
        l = 0
        r = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_sub = max(max_sub, r-l+1)
            r += 1
                
        return max_sub