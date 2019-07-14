# @Author:Kilien
# @lc app=leetcode id=198 lang=python3
# [198] House Robber
# https://leetcode.com/problems/house-robber/description/
class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

