# @Author:Kilien
# @lc app=leetcode id=78 lang=python3
# [78] Subsets
# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res            
