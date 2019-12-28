import string

ALL_CHRS = list(string.ascii_lowercase) + list(string.digits)


# Runtime: 80 ms, faster than 10.59% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 19.1 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ch.lower() in ALL_CHRS]
        return s == s[::-1]


class SolutionVariant:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s:
            if i.isalnum():
                clean += i
        left = 0
        right = len(s) - 1
        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome("A man, a plan, a canal: Panama")
    print(res)