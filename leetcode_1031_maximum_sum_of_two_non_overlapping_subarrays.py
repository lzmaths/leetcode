import sys

class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        #print(self.helperDP(A, L, M), self.helperDP(A, M, L))
        return max(self.helperDP(A, L, M), self.helperDP(A, M, L))
        
        
    def helperDP(self, A, L, M):
        n = len(A)
        dp_left_l = [0] * n
        dp_right_m = [0] * n
        
        dp_left_l[L-1] = sum(A[:L])
        dp = [0] * n
        dp[L-1] = dp_left_l[L-1]
        for i in range(L, n):
            curr_sum = dp[i-1] - A[i-L] + A[i]
            dp[i] = curr_sum
            dp_left_l[i] = max(dp_left_l[i-1], dp[i])
            #print("left", i, dp_left_l)
            
        dp_right_m[n-M] = sum(A[n-M:])
        dp = [0] * n
        dp[n-M] = dp_right_m[n-M]
        for i in range(n-M-1, -1, -1):
            curr_sum = dp[i+1] - A[i+M] + A[i]
            dp[i] = curr_sum
            dp_right_m[i] = max(dp_right_m[i+1], dp[i])
            #print("right", i, dp_right_m)
            
        ans = 0
        for i in range(L, n-M+1):
            ans = max(ans, dp_left_l[i-1] + dp_right_m[i])
            #print(ans)
        return ans


solution = Solution()
A = [0,6,5,2,2,5,1,9,4]
L = 1
M = 2
print(solution.maxSumTwoNoOverlap(A, L, M))

A = [3,8,1,3,2,1,8,9,0]
L = 3
M = 2
print(solution.maxSumTwoNoOverlap(A, L, M))

A = [2,1,5,6,0,9,5,0,3,8]
L = 4
M = 3
print(solution.maxSumTwoNoOverlap(A, L, M))


# for elegant solution, check the post here: https://preview.tinyurl.com/w4jolax

class ElegantSolution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res 