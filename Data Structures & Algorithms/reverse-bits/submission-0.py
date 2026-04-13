class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1 # take the last bit
            res = (res << 1) | bit # left shift and add bit
            n = (n >> 1) # right shift and process next bit
        return res