

class Solution:
    def validIPAddress(self, IP: str) -> str:
        is_ip4 = self.valid_ip4(IP)
        if is_ip4:
            return "IPv4"
        is_ip6 = self.valid_ip6(IP)
        if is_ip6:
            return "IPv6"
        return "Neither"

    def valid_ip4(self, IP: str) -> bool:
        parts = IP.split('.')
        if len(parts) != 4:
            return False
        for p in parts:
            if p[0] == '0':
                return False
            val = int(p)
            if val < 0 or val > 255:
                return False
        return True

    def leading_zero(self, substring: str) -> bool:
        if substring[0] == '0':
            try:
                int(substring)
            except Exception:
                return False
            return True
        return False

    def valid_ip6(self, IP: str) -> bool:
        import pdb; pdb.set_trace()
        parts = IP.split(':')
        if len(parts) != 8:
            return False
        for p in parts:
            if len(p) == 0:
                return False
            if self.leading_zero(p):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    res = s.valid_ip6("2001:0db8:85a3:0:0:8A2E:0370:7334")