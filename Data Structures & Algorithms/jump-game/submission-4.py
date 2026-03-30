class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = 0

        for i in range(len(nums)):
            if i > max_len:
                return False

            cur_len = i + nums[i]
            max_len = max(max_len, cur_len)
            if max_len >= len(nums) - 1:
                return True

        return False