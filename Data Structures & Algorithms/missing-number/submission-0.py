class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] != 1:
                return int(nums[i+1]) - 1
        return 0
