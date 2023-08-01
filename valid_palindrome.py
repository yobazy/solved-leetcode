class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ## remove non-abc
        s_rem = ''.join(c for c in s if c.isalnum())
        s_cut = s_rem.lower()
        print(s_cut)
        
        i = len(s_cut)

        ## check if same forwards and backwards
        for a in range(i):
            b = i - a - 1
            print("b is "+str(b))
            
            print(s_cut[a])
            print(s_cut[b])

            if (s_cut[a] != s_cut[b]):
                return False;
        return True;