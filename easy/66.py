class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        i = 10**(len(digits)-1)
        for x in range(0,len(digits)):
            num += digits[x]*i
            i=i/10
        num+=1
        digits=list(map(int,str(num)))
        return digits
