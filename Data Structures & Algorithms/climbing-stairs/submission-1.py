class Solution:
    def climbStairs(self, n: int) -> int:
        # O(n)
        step1 = 1
        step2 = 1

        for _ in range(n-1):
            tmp = step1 + step2
            step1 = step2
            step2 = tmp

        return step2
