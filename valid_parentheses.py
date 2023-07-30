class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            "}":"{",
            ")":"(",
            "]":"[",
        }
        
        stack = []
        
        for x in s:
            if x in pairs:
                if stack and stack[-1] == pairs[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
            
        if not stack:
            return True
        else:
            return False