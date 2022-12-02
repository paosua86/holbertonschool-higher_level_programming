#!/usr/bin/python3

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashtable = set()

        for n in nums:
            if n in hashtable:
                return True
            hashtable.add(n)
        return False


nums = [1,2,3,1]
result = Solution.containsDuplicate(None, nums)
print(result)
