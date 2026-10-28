class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anag_dict = defaultdict(list)
        anag_dict = {}  # key=abc_count val=anag_list

        for word in strs:
            key = [0] * 26  # one for each letter in abc

            for char in word:
                key[ord(char) - ord("a")] += 1

            anag_dict[tuple(key)] = anag_dict.get(tuple(key), []) + [word]

        return anag_dict.values()