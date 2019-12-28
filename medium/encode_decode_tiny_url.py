"""
535. Encode and Decode TinyURL
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode
algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
can be decoded to the original URL.
"""


# Runtime: 32 ms, faster than 58.43% of Python3 online submissions for Encode and Decode TinyURL.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Encode and Decode TinyURL.
class Codec:
    mapping = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        res = str(hash(longUrl))
        self.mapping[res] = longUrl
        return "http://tinyurl.com/{}".format(res)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        hash_value = shortUrl.split('/')[-1]
        return self.mapping[hash_value]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))