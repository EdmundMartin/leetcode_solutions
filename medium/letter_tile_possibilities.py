"""
1079. Letter Tile Possibilities
You have a set of tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make.

Example 1:
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: "AAABBC"
Output: 188

Note:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""


# Runtime: 72 ms, faster than 76.30% of Python3 online submissions for Letter Tile Possibilities.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Letter Tile Possibilities.
class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        tiles_dict = dict()
        for t in tiles:
            if t in tiles_dict:
                tiles_dict[t] += 1
            else:
                tiles_dict[t] = 1

        def back_track(tiles_dict):
            count = 0
            for key in tiles_dict.keys():
                if tiles_dict[key] > 0:
                    count += 1
                    tiles_dict[key] -= 1
                    count += back_track(tiles_dict)
                    tiles_dict[key] += 1
            return count

        return back_track(tiles_dict)
