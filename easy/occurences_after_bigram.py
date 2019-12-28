"""
1078. Occurrences After Bigram
Given words first and second, consider occurrences in some text of the form "first second third",
where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Example 2:
Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]

Note:
1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
"""
from typing import List


# Runtime: 28 ms, faster than 88.12% of Python3 online submissions for Occurrences After Bigram.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Occurrences After Bigram.
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_array = text.split(' ')
        result = []
        for i in range(1, len(text_array)):
            current = text_array[i - 1]
            next = text_array[i]
            if current == first and next == second and i + 1 <= len(text_array) - 1:
                result.append(text_array[i + 1])
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.findOcurrences("alice is a good girl she is a good student", "a", "good")
    print(res)
    res = s.findOcurrences("we will we will rock you", "we", "will")
    print(res)