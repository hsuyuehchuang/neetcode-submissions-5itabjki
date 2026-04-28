class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = max(nums)
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
            tmp = n * curMax
            curMax = max(tmp, n * curMin, n)
            curMin = min(n * curMax, n * curMin, n)
            res = max(res, curMax)
        return res