class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                result += int(num1[~i]) * 10**i * int(num2[~j]) * 10**j
        return str(result)