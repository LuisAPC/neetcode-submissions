class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            while l<r and not self.is_al_num(s[l]):
                l+=1
            while l<r and not self.is_al_num(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def is_al_num(self, char):
        if (ord("0") <= ord(char) <= ord("9") or
            ord("a") <= ord(char) <= ord("z") or
            ord("A") <= ord(char) <= ord("Z")):
            return True
        return False