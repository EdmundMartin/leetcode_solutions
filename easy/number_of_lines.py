from typing import List
import string


# Runtime: 32 ms, faster than 91.84% of Python3 online submissions for Number of Lines To Write String.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of Lines To Write String.
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines = 1
        current_line = 0
        for ch in S:
            size = widths[string.ascii_lowercase.index(ch)]
            if current_line + size > 100:
                lines += 1
                current_line = size
                continue
            if current_line + size == 100:
                lines += 1
                current_line = 0
                continue
            elif current_line + size < 100:
                current_line += size
        return [lines, current_line]


if __name__ == '__main__':
    s = Solution()
    res = s.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa")
    print(res)