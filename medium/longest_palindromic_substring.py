"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
# Runtime: 7728 ms, faster than 5.01% of Python online submissions for Longest Palindromic Substring.
# Memory Usage: 11.8 MB, less than 73.97% of Python online submissions for Longest Palindromic Substring.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if len(substring) > len(longest) and self.is_palindrome(substring):
                    longest = substring
        return longest

    def is_palindrome(self, target):
        return target == target[::-1]