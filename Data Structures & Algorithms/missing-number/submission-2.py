class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for n in range(len(nums)):
            if n != nums[n]:
                return n
        return len(nums)
