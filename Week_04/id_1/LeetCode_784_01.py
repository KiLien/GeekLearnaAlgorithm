# @Author:Kilien
# @lc app=leetcode id=784 lang=python3
# [784] Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/description/
'''
小写字母和大写字母ASICII码相差32:
异或：不等则为1，即 0 ^ 1 =1
1 << 5：1左移5位，即 00..000001 -> 00..10000
'''
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                res.extend([s[:i] + chr(ord(s[i]) ^ (1<<5)) + s[i+1:] for s in res])
        return res       

