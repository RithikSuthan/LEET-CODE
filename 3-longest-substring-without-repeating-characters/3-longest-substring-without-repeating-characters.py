class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        e=0
        l=0
        set1=set()
        while(i<len(s)):
            if s[i] in set1:
                set1.remove(s[e])
                e+=1
            else:
                set1.add(s[i])
                i=i+1
                l=max(l,i-e)
        return l
