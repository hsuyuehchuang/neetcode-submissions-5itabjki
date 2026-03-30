class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        left = 0
        right = len(numbers)-1
        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum > target:
                right-=1
            elif currentSum < target:
                left+=1
            else:
                res.append(left+1)
                res.append(right+1)
                return res
        return res
            



# 12345
# ^   ^
# i.  j 
# target = target
# currentSum = numbers[i] + numbers[j]
# res=[]