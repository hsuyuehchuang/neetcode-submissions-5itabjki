class MinStack:
    
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            lastMin = self.stack[-1][1]
            currentMin = min(val, lastMin)
            self.stack.append((val, currentMin))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        
# tuple = (val, currentMin)
# currentMin = min(val, lastMin)