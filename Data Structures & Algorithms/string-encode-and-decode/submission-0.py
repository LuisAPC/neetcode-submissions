class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for word in strs:
            n = len(word)
            encode_str += str(n) + "!" + word
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        word_len = ""
        while i < len(s):
            #Get word length
            j=i
            while s[j] != "!":
                j += 1
            #Save word
            word_len = int(s[i:j])
            decode_list.append(s[j+1 : j+1+word_len])
            i = j + 1 + word_len
        return decode_list
