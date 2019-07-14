# @Author:Kilien
# @lc app=leetcode id=51 lang=python3
# [51] N-Queens
# https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def _dfs(cols, pie, na):
            row = len(cols)
            if row == n:
                result.append(cols)
                return None
            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    _dfs(cols + [col], pie + [row + col], na + [row - col])

        result = []
        _dfs([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in row] for row in result]        
       

