class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            if A[i][0] <= B[j][0] <= A[i][1] or B[j][0] <= A[i][0] <= B[j][1]:
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res