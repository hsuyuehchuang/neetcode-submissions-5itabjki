import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                sqrs_idx = (i//3, j//3)
                
                if (val in rows[i] or
                    val in cols[j] or
                    val in sqrs[sqrs_idx]):
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                sqrs[sqrs_idx].add(val)
        
        return True