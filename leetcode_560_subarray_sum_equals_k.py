import sys, collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # hashtable
        s = 0
        ans = 0
        dic = collections.defaultdict(int)
        dic[0] = 1
        for num in nums:
            s += num
            ans += dic[s-k]
            dic[s] += 1
        return ans