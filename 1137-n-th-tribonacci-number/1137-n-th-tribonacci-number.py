class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        ls=[0,1,1]
        if(n==0):
            return ls[0]
        for i in range(n):
            if(n==1):
                return ls[1]
            elif(n==2):
                return ls[1]
            else:
                if(i==n-1):
                    return ls[i+1]
                ls.append(ls[i]+ls[i+1]+ls[i+2])
                print(ls)

        