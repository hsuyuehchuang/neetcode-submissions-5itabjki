class Solution:
    def isValid(self, s:str) -> bool:
        dict = {'(':')', '[':']', '{':'}'}
        stack=[]
        for char in s:
            if char in dict:
                stack.append(char)
            else:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '0'
            
                if top_element == '0' or dict[top_element] != char:
                    return False

        return not stack