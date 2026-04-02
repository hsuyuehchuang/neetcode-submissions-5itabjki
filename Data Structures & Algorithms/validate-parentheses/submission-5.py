class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        dict = {"(":")", "[":"]", "{":"}"}

        for char in s:
            # if char in dict:
            if char in dict.keys():
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if char == ")" and top != "(":
                    return False
                if char == "]" and top != "[":
                    return False
                if char == "}" and top != "{":
                    return False

        return len(stack) == 0