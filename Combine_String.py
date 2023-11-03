# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:33:29 2023

@author: punam.chaudhari
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ''
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            merged += word1[i] + word2[i]

        if len(word1) > len(word2):
            merged += word1[min_len:]
        else:
            merged += word2[min_len:]

        return merged

# Example usage
word1 = "abc"
word2 = "pqr"
solution = Solution()
output = solution.mergeAlternately(word1, word2)
print(output)
