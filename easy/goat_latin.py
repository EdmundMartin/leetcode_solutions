"""
824. Goat Latin
A sentence S is given, composed of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:
If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter
and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end,
the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.

Example 1:
Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:
Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:
S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""


# Runtime: 24 ms, faster than 94.58% of Python3 online submissions for Goat Latin.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Goat Latin.
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        final_sent = ""
        for idx, word in enumerate(S.split(' ')):
            if word[0].lower() in vowels:
                new_word = f"{word}ma"
            else:
                ch = word[0]
                word = word[1:]
                new_word = f"{word}{ch}ma"
            extra_ch = (idx + 1) * "a"
            final_sent += f"{new_word}{extra_ch} "
        return final_sent.rstrip()
