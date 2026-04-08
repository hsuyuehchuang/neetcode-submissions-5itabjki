class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_count = {0 : 1}
        for num in nums:
            cur_sum += num
            target = cur_sum - k
            if target in prefix_count:
                res += prefix_count[target]
            prefix_count[cur_sum] = prefix_count.get(cur_sum, 0) + 1
        return res