class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ""
        for i in digits:
            print(i)
            string = string+str(i)
        new_num = int(string) + 1 
        ans = [int(i) for i in str(new_num)]
        return(ans)