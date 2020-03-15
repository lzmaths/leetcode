"""
Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
"""

import sys

class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.nums = v
        self.row = 0
        self.col = 0
        

    def next(self):
        """
        :rtype: int
        """
        #print(self.nums, self.row, self.col)
        if not self.hasNext():
            return None
        curr = self.nums[self.row][self.col]
        self.col += 1
        return curr
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.nums):
            if self.col < len(self.nums[self.row]):
                return True
            
            self.col = 0
            self.row += 1
        return False
        

    #def remove(self):
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
