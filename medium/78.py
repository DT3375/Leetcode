class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in nums:
            for j in range(len(result)):
                result += [result[j]+[i]]
        return result
