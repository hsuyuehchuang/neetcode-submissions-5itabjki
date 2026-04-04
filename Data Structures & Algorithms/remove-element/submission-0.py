class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        for i in range(len(nums)):
            if val != nums[i]:
                res.append(nums[i])
        return len(res)

# create a empty list
# if the value is in nums: skip
# else, append nums[i] into res