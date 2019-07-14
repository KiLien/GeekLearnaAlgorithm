# @Author:Kilien
# @lc app=leetcode id=70 lang=python3
# [70] Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        res = [0] * n
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]


