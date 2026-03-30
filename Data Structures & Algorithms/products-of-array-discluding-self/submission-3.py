class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            res = [0] * len(nums)

        else:
            total_prod = 1
            for n in nums:
                if n != 0:
                    total_prod *= n
            
            res = []
            for n in nums:
                if zero_count == 1:
                    res.append(total_prod if n == 0 else 0)
                else:
                    res.append(total_prod // n)
        
        return res