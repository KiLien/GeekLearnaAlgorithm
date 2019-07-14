# @Author:Kilien
# @lc app=leetcode id=309 lang=python3
# [309] Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        not_hold, hold, cooldown = 0, float('-inf'), float('-inf')
        for i in prices:
            hold = max(hold, not_hold - i)
            not_hold = max(not_hold, cooldown)
            cooldown = hold + i
        return max(not_hold, cooldown)


