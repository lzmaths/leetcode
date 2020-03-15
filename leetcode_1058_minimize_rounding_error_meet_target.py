import math, sys

class Solution(object):
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
        prices = [float(num) for num in prices]
        ceil_sum = sum([math.ceil(num) for num in prices])
        floor_sum = sum([math.floor(num) for num in prices])
        k = ceil_sum - target
        if target > ceil_sum or target < floor_sum:
            return "-1"
        
        k = int(ceil_sum - target)
        print(k)
        decimals = [num - math.floor(num) for num in prices if num - math.floor(num) > 0]
        decimals.sort()
        ans = sum(decimals[:k]) + sum([1-num for num in decimals[k:]])
        return str("{0:.3f}".format(ans))
