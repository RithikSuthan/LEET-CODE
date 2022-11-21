class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        k=0
        x1=x
        count=1
        while(x!=0):
            k=k*count+int(x%10)
            count=1
            count=count*10
            x=x//10
            print("k=",k)
            print("x=",x)
        print(k)
        if(k==x1):
            return True
        else:
            return False