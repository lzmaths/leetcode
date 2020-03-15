import sys

class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        https://leetcode.com/problems/ip-to-cidr/discuss/417971/Decimal-to-base-256-method-Python-Easy-to-understand-explanation-w-unit-test
        """
        num = self.ipToNum(ip)
        ans = []

        while n > 0:
            trailing_zeros = self.trailing_0s(num)
            ip = self.numToIp(num)

            while trailing_zeros > n:
                trailing_zeros //= 2

            cnt = self.idx_of_trailing_one(trailing_zeros)
            ans.append(f"{ip}/{32-cnt}")
            n -= trailing_zeros
            num += trailing_zeros
        return ans
            

    def ipToNum(self, ip):
        a, b, c, d = ip.split('.')
        return int(a) * 256**3 + int(b) * 256**2 + int(c) * 256**2 + int(d)

    def numToIp(self, num):
        a, b, c, d = num // 256**3 % 256, num // 256**2 % 256, num // 256**1 % 256, num // 256**0 % 256
        
        return ".".join(map(str, [a, b, c, d]))

    def trailing_0s(self, num):
        return num & -num

    def idx_of_trailing_one(self, num):
        cnt = 0
        while num & 1 == 0:
            num >>= 1
            cnt += 1
        return cnt