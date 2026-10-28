class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        backet_pairs = {"}":"{", ")":"(", "]":"["} # close:open

        for c in s:
            if stack and c in backet_pairs:
                open_bracket = stack.pop()
                if backet_pairs[c] != open_bracket:
                    return False
                continue
            stack.append(c)

        return stack == []