class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while True:
            p = self.partition(nums, start, end)
            if p == len(nums)-k:
                return nums[p]
            elif p > len(nums) - k:
                end = p-1
            else:
                start = p + 1

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low
        for j in range(low, high+1):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[high] = nums[high], nums[i]

        return i