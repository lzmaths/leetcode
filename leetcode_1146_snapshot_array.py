import sys
import bisect

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snapshot = 0
        self.nums = {i:[[-1, 0]] for i in range(length)}
        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.nums[index][-1][0] == self.snapshot:
            self.nums[index][-1][1] = val
        else:
            self.nums[index].append([self.snapshot, val])
        
            
    def snap(self):
        """
        :rtype: int
        """
        self.snapshot += 1
        return self.snapshot - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        cands = self.nums[index]
        idx = bisect.bisect(cands, [snap_id+1]) - 1
        return cands[idx][1]
        


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0, 5)
param_2 = obj.snap()
print(param_2)
#param_2 = obj.snap()
#print(param_2)
obj.set(0, 6)

param_3 = obj.get(0, 0)
print(param_3)