class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        nums_1 = nums[0:n-1]
        nums_2 = nums[1:n]

        def findmax(nums):
            exexrob = 0
            exrob = 0
            for n in nums:
                nowrob = max(exexrob + n, exrob)
                exexrob = exrob
                exrob = nowrob
            return exrob

        return max(findmax(nums_1), findmax(nums_2))
