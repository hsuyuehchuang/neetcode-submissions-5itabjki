class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            count = 0
            for bit in range(32):
                if (1 << bit) & num:
                    count += 1
            res.append(count)
        return res