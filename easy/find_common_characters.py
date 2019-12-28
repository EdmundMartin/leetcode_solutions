"""
Find Common Characters
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""
from typing import List


# Runtime: 52 ms, faster than 81.11% of Python3 online submissions for Find Common Characters.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Find Common Characters.
class Solution:

    def shortest_word(self, A: List[str]):
        shortest = A[0]
        for w in range(1, len(A)):
            if len(A[w]) < len(shortest):
                shortest = A[w]
        return shortest

    def counter_dict(self, word):
        map = {}
        for ch in word:
            if ch not in map:
                map[ch] = 1
            else:
                map[ch] += 1
        return map

    def commonChars(self, A: List[str]) -> List[str]:
        shortest = self.shortest_word(A)
        counts = self.counter_dict(shortest)
        common = {k: 0 for k in counts.keys()}
        for word in A:
            update_counts = self.counter_dict(word)
            for k in update_counts.keys():
                if k in counts:
                    counts[k] = min(update_counts[k], counts[k])
                if k in common:
                    common[k] += 1
        ret_value = []
        for key, value in common.items():
            if value == len(A):
                key_count = counts[key]
                for i in range(key_count):
                    ret_value.append(key)
        return ret_value




if __name__ == '__main__':
    s = Solution()
    rsult = s.commonChars(["bella","label","roller"])
    print(["e","l","l"])
    print(rsult)

