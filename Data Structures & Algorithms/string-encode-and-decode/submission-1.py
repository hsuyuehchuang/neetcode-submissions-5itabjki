class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        final_string = "".join(res)
        return final_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # 負責走訪編碼字串的指標
        
        while i < len(s):
            # 1. 尋找長度數字的結束點 (即分隔符 '#')
            j = i
            while s[j] != "#":
                j += 1
                
            # 2. 擷取長度 (i 到 j 之間的字串就是數字，轉換為整數)
            length = int(s[i:j])
            
            # 3. 根據長度，精準擷取原始字串內容
            # 字串起點在 j+1，終點在 j+1+length
            res.append(s[j + 1 : j + 1 + length])
            
            # 4. 將指標移動到下一個資料區塊的開頭
            i = j + 1 + length
            
        return res