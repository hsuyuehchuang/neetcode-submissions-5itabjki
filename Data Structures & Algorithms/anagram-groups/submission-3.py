class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# 1. 宣告 Hash Map 來存儲所有符合特定組成的字串
        # Key = 26 個字母的出現頻率 Tuple
        # Value = 一個 List，包含符合該頻率的所有字串
        ans = defaultdict(list)
        
        for s in strs:
            # 2. 幫每一個字串重新計算字母頻率
            count = [0] * 26  # 初始化 26 個零，代表 a~z 的出現次數
            
            for char in s:
                # 把字元轉換為對應陣列的位置 (a->0, b->1... z->25)
                # 利用 ord() 將字母轉為 ASCII，再減掉 a 的 ASCII 值
                index = ord(char) - ord("a")
                count[index] += 1
                
            # 3. List 不能當作字典的 Key（因為它是可變的）
            # 所以必須轉換成不可變的 Tuple，當作這個字串專屬的「特徵值」
            ans[tuple(count)].append(s)
            
        # 4. 把字典裡所有的 Value 提取出來，變成題目的預期格式
        return list(ans.values())