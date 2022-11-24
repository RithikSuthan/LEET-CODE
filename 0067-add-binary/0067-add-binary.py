class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=list(a)
        b=list(b)
        count=0
        result=""        
        while a or b or count:
            if a:
                count =count+int(a.pop())
            if b:
                count =count+int(b.pop())
            result=result+str(count%2)
            
            count=count//2
                
        return result[::-1]
