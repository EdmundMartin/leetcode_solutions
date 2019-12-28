
# Runtime: 28 ms, faster than 95.41% of Python3 online submissions for Hamming Distance.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Hamming Distance.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    s = Solution()
    diff = s.hammingDistance(4, 14)
    print(diff)