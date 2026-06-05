import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        box=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val=board[r][c]

                if (val=="."):
                    continue
                
                box_coord=(r//3,c//3)

                if(val in row[r] or val in col[c] or val in box[box_coord]):
                    return False
                
                row[r].add(val)
                col[c].add(val)
                box[box_coord].add(val)
        return True