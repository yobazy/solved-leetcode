class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hist = set()
        for item in nums:
            if item in hist:
                return True
            hist.add(item)
        return False
