class Solution:
	def maxp3(self, A):
        A = sorted(A)
        
        a = A[-1] * A[-2] * A[-3]
        b = A[0] * A[1] * A[-1]
        return max(h,l)
