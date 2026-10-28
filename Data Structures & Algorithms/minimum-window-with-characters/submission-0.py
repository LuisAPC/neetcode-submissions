class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur_s = {}
        t_dict = {}
        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)

        have = 0
        need = len(t_dict)
        res = [0,0]
        res_len = len(s)+1
        l = 0
        for r in range(len(s)):
            char = s[r]
            cur_s[char] = 1 + cur_s.get(char, 0)

            if char in t_dict and cur_s[char] == t_dict[char]:
                have += 1
            
            while have == need:
                if (r-l+1) < res_len:
                    res_len = r-l+1
                    res = [l, r]

                cur_s[s[l]] -= 1
                if s[l] in t_dict and cur_s[s[l]] < t_dict[s[l]]:
                    have -= 1

                l +=1
        l, r = res
        return s[l:r+1] if res_len < len(s)+1 else ""