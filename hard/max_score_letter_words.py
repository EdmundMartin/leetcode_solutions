"""
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot
be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once.
Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"],
       score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.

Example 2:
Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"],
       score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.

Example 3:
Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"],
       score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.

Constraints:
1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
"""
from string import ascii_lowercase
from typing import Dict, List
import itertools


class SolutionToSlow:

    def letters_score(self, score) -> Dict:
        alphabet = ascii_lowercase
        result = {}
        for idx, sc in enumerate(score):
            result[alphabet[idx]] = sc
        return result

    def can_make_word(self, word: str, letters: List[str]):
        unique_chs = set(word)
        for ch in unique_chs:
            if word.count(ch) > letters.count(ch):
                return False
        return True

    def score_word(self, all_words, letters: List[str], scores: Dict[str, int]):
        score = 0
        for current_word in all_words:
            if len(current_word) > len(letters):
                continue
            if self.can_make_word(current_word, letters):
                current_score = 0
                for ch in current_word:
                    first_idx = letters.index(ch)
                    current_score += scores[ch]
                    letters.pop(first_idx)
                score += current_score
        return score

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_score = self.letters_score(score)
        top_score = 0
        res = itertools.permutations(words)
        for perm in res:
            letter_copy = letters.copy()
            current_score = self.score_word(perm, letter_copy, letters_score)
            if current_score > top_score:
                top_score = current_score
        return top_score


# Runtime: 40 ms, faster than 94.60% of Python3 online submissions for Maximum Score Words Formed by Letters.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Maximum Score Words Formed by Letters.
class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        mapping = {}
        for ch in letters:
            if ch not in mapping:
                mapping[ch] = 1
            else:
                mapping[ch] += 1

        self.result = 0

        def backtrack(accum, words, letter_map, score):
            if not words or not letter_map:
                return

            backtrack(accum, words[1:], letter_map, score)

            tmp_letters = {}
            for w in words[0]:
                if w not in tmp_letters:
                    tmp_letters[w] = 1
                else:
                    tmp_letters[w] += 1

            keys = tmp_letters.keys()
            for k in keys:
                if k not in letter_map or tmp_letters[k] > letter_map[k]:
                    return

            res = 0
            for k in keys:
                res += tmp_letters[k] * score[ord(k) - ord('a')]
                letter_map[k] -= tmp_letters[k]

            res += accum

            self.result = max(self.result, res)

            backtrack(res, words[1:], letter_map, score)

            for k in tmp_letters.keys():
                letter_map[k] += tmp_letters[k]

        backtrack(0, words, mapping, score)

        return self.result


if __name__ == '__main__':
    words = ["ad","dbacbbedc","ae","adbdacad","dcdecacdcb","ddbba","dbcdbeaade","aeccdcb","bce"]
    letters = ["a","a","a","a","a","a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","d","d","d","d","e","e","e","e","e","e"]
    score = [1,8,3,1,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    s = Solution()
    res = s.maxScoreWords(words=words, letters=letters, score=score)
    print(res)