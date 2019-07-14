# @Author:Kilien
# @lc app=leetcode id=53 lang=python3
# [53] Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/
'''
最大子序列之和：
    当前位置值 + 前面状态集合
    dp[i] = nums[i] + dp[i - 1]
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0], maxs = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
            maxs = max(maxs, dp[i])
        return maxs

