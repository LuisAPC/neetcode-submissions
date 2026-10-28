class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            s_sorted = tuple(sorted(s))
            res[s_sorted] = res.get(s_sorted, []) + [s]
        return list(res.values())
