"""
49. Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""
from typing import List


# Runtime: 100 ms, faster than 92.81% of Python3 online submissions for Group Anagrams.
# Memory Usage: 15.6 MB, less than 96.23% of Python3 online submissions for Group Anagrams.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = {}
        for gram in strs:
            sorted_gram = ''.join(sorted(gram))
            if sorted_gram in mappings:
                mappings[sorted_gram].append(gram)
            else:
                mappings[sorted_gram] = [gram]
        return [v for v in mappings.values()]

