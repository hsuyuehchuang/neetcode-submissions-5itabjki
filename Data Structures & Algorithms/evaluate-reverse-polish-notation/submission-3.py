class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []

        for char in tokens:
            if char == "+" or char == "-" or char == "*" or char == "/":
                a2 = stack.pop()
                a1 = stack.pop()

                if char == "+":
                    stack.append(a1 + a2)
                elif char == "-":
                    stack.append(a1 - a2)
                elif char == "*":
                    stack.append(a1 * a2)
                elif char == "/":
                    stack.append(int(a1 / a2))

            else:
                stack.append(int(char))

        return stack[0]