#!/usr/bin/python3

from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


s = "anagram"
t = "nagaram"
result = Solution.isAnagram(None, s, t)
print (result)

s = "anagram"
t = "nagara"
result = Solution.isAnagram(None, s, t)
print (result)



class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"
result = Solution2.isAnagram(None, s, t)
print (result)

s = "anagram"
t = "nagara"
result = Solution2.isAnagram(None, s, t)
print (result)


class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
result = Solution3.isAnagram(None, s, t)
print (result)

s = "anagram"
t = "nagara"
result = Solution3.isAnagram(None, s, t)
print (result)

