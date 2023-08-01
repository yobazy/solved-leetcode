class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return true if t is an anagram of s 
        t_letters = list(t)
        if len(s) != len(t):
            return False
        for letter in s:
            if letter not in t_letters:
                return False
            t_letters.remove(letter)
        return True