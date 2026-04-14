class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this problem is to check if ther is a cycle in the directed graph
        # we can maintain a preMap to store the prerequisites of each course
        
        # we can also maintain a visited set to store the courses that have been visited
        # once the current course is visited, we know there is a cycle, we can return false

        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []: # this course is save, is no prerequisites, we can take this course
                return True
            visited.add(crs)
            
            for pre in preMap[crs]: # check the prerequisites of all courses
                if not dfs(pre): return False 

            visited.remove(crs) # 這叫回溯。當 A 的所有先修課都檢查完沒問題，要把 A 從「危險路徑」中移除，因為它不再屬於當前正在探測的路徑。
            preMap[crs] = [] # 重要優化：標記為安全，下次直接回傳 True
            return True
        
        for crs in range(numCourses): # looping like this due to the seperate course like
            if not dfs(crs): return False
        return True 

# 為什麼 visited 要 add 又 remove？ 
# 想像一個「V 字型」的依賴關係：A -> C 和 B -> C
# 我們探測 A，路徑變成 A -> C，檢查完 C 沒問題，結束。 
# 接著探測 B，路徑變成 B -> C。
# 如果我們不 remove(A)，探測 B 的時候 visited 裡還留著 A，這不會出錯，但邏輯不對。 
# 更重要的是，如果沒有回溯，我們無法區分「以前看過的課」跟「現在這條路上的課」。