class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1
        maxArea = 0

        while left < right:
            currentArea = (right - left) * min(height[left], height[right])
            if currentArea > maxArea:
                maxArea = currentArea
                
            if height[left] < height[right]:
                left+=1
            else: 
                right-=1
            


        return maxArea