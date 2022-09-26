class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        cost = 0
        
        for bulb in A:
            if cost%2==0:
                bulb = bulb
            else:
                bulb = not bulb
            
            if bulb == 1:
                continue
            else:
                cost+=1
        return cost