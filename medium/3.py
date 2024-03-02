class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        for i in range(len(s)):
            l=[]
            c=0
            for j in range(i,len(s)):
                if s[j] not in l:
                    l.append(s[j])
                    c+=1
                    m=max(m,c)
                else:
                    break
        return m
