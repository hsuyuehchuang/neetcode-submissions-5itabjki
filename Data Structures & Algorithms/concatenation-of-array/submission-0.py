class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * 2 * length
        for i in range(len(nums)):
            res[i] = nums[i]
            res[i + length] = nums[i]
        return res