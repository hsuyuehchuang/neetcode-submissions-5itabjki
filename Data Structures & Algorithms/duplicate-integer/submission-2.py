class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []
        for n in nums:
            if n not in res:
                res.append(n)

        return not len(nums) == len(res)