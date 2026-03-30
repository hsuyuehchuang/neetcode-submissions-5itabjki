class Solution:
    def rob(self, nums: List[int]) -> int:
        # exexrob is ex, ex, rob result
        # exrob is ex-rob result

        exexrob = 0
        exrob = 0

        for n in nums:
            nowrob = max(exexrob + n, exrob)
            exexrob = exrob
            exrob = nowrob
        return exrob