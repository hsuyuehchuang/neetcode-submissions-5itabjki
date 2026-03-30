class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # {key: value}

        for i, num in enumerate(nums):
            need_find = target - num

            if need_find in prev_map:
                return [prev_map[need_find], i]
            
            prev_map[num] = i