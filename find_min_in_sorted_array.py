class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = 9999
        
        for i, num in enumerate(nums):
            if num < min_val:
                min_val = num
        return min_val