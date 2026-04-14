class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for n in range(numCourses):
            preMap[n] = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        def dfs(crs):
            if crs in visit: 
                return False
            if preMap[crs] == []: # save course
                return True
            visit.add(crs)
            # check all pre
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses): # check all course in case these are subsets
            if dfs(crs) == False:
                return False
        return True