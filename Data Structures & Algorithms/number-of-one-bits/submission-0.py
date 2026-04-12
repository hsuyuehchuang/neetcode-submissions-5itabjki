class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (1 << i) & n: # 1 << i means shift how many bits
                res += 1 # if true means the ith bit is "1"
        return res