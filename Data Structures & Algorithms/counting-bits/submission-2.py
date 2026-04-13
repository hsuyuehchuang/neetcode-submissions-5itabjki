
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
    
# every number can divide as: i = offset + (i - offset)
# offset is the largest power of 2 that is less than or equal to i
# the number of "1" in binary of i is 1 + the number of "1" in binary of (i - offset)
# so, bits(i) = 1 + bits(i - offset)
# so, bp(i) = 1 + bp(i - offset)
# time complexity: O(n)
# space complexity: O(n) 