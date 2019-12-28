"""
884. Uncommon Words from Two Sentences
We are given two sentences A and B.  (A sentence is a string of space separated words.
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words.
You may return the list in any order.



Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:
0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""
from typing import List


# Runtime: 32 ms, faster than 82.53% of Python3 online submissions for Uncommon Words from Two Sentences.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Uncommon Words from Two Sentences.
class Solution:

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        counts = {}
        for sent in [A, B]:
            for word in sent.split():
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
        return [k for k, v in counts.items() if v == 1]


if __name__ == '__main__':
    s = Solution()
    res = s.uncommonFromSentences("this apple is sweet", "this apple is sour")
    print(res)