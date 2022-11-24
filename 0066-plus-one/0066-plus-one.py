class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        count=1
        for i in range(len(digits)-1,-1,-1):
            digits[i]=digits[i]*count
            count=count*10
            num=num+digits[i]
        num=str((num+1))
        num1=[]
        for i in num:
            num1.append(int(i))
        return num1