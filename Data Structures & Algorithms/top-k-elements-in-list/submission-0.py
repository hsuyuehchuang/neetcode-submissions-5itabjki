class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_common = count.most_common(k) # most_common = [(1, 3), (2, 2)]
        ans = [num for num, freq in most_common]
        return ans