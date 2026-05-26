class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = Counter(t)
        

        if not s or not t or len(s) < len(t):
            return ""
        
        min_len = float('inf')
        min_str = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j+1]
                sub_count = Counter(sub_str)

                isValid = True
                for char, count in target_count.items():
                    if sub_count[char] < count:
                        isValid = False
                        break
                
                if isValid:
                    if len(sub_str) < min_len:
                        min_len = len(sub_str)
                        min_str = sub_str

        return min_str