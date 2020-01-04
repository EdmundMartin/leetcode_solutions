from typing import List


# Runtime: 36 ms, faster than 46.59% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Verifying an Alien Dictionary.
class Solution:

    def compare_words(self, word_one: str, word_two: str, alpha_dict):
        smallest = min(len(word_one), len(word_two))
        for idx in range(smallest):
            if alpha_dict[word_one[idx]] < alpha_dict[word_two[idx]]:
                return True
            elif alpha_dict[word_one[idx]] == alpha_dict[word_two[idx]]:
                continue
            else:
                return False
        if len(word_two) < len(word_one):
            return False

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True

        alpha_dict = {}
        for idx, value in enumerate(order):
            alpha_dict[value] = idx

        for idx in range(len(words) - 1):
            if not self.compare_words(words[idx], words[idx + 1], alpha_dict):
                return False
        return True

