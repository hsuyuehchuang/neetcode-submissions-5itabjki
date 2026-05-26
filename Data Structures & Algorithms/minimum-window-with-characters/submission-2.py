class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_target = Counter(t)
        required = len(dict_target)
        formed = 0
        window_counts = {}
        left, right = 0, 0
        ans = float("inf"), None, None

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_target and window_counts[char] == dict_target[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window_counts[char] -= 1

                if char in dict_target and window_counts[char] < dict_target[char]:
                    formed -= 1

                left += 1

            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
    