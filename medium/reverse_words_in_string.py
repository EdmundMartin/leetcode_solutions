"""
Given an input string, reverse the string word by word.

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


# Runtime: 36 ms, faster than 73.04% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 13.3 MB, less than 95.65% of Python3 online submissions for Reverse Words in a String.
class Solution:
    # Not using Python (too many) built ins
    def reverseWords(self, s: str) -> str:
        words = []
        current_word = ""
        for ch in s:
            if ch == " ":
                if len(current_word) > 0:
                    words.append(current_word)
                    current_word = ""
            else:
                current_word += ch
        if len(current_word) > 0:
            words.append(current_word)
        sentence = ""
        for w in words:
            sentence = w + "  " + sentence
        return sentence[:-1]


# Runtime: 28 ms, faster than 95.91% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Reverse Words in a String.
class SolutionPythonic:

    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = [w for w in words if w != ""]
        return ' '.join(words[::-1])


if __name__ == '__main__':
    s = SolutionPythonic()
    res = s.reverseWords("a good   example")
    print(res)