class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = 0
        for i in range(len(s)):
            count += ord(s[i]) - ord(t[i])
        return count == 0
