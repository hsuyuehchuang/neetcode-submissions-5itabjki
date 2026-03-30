class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# 我們手動定義前 26 個質數
        primes = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 
            'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 
            'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 
            's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 
            'y': 97, 'z': 101
        }
        
        ans = defaultdict(list)
        
        for s in strs:
            key = 1
            for char in s:
                # 把字串裡的每個字母對應的質數乘起來
                key *= primes[char]
                
            # 這個相乘後的數字 key，就成了專屬的特徵值
            ans[key].append(s)
            
        return list(ans.values())