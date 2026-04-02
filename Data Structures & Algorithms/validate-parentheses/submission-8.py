class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        dict = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if not stack or dict[char] != stack.pop():
                    return False
                    
        return len(stack) == 0