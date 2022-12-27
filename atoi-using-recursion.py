#Problem:
#The function takes a string(str) as argument and converts it to an integer and returns it.

#Input: 123,--123,-123,90a,-56 40

#Output: 123,-1,-123,-1,-56



#Code:

#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def helper(self,string,num,i,signFlag):
        if i==len(string) or (string[i]==" " and num>0):                                      #Base condition
            if signFlag==1:
                num =num*(-1)
            return num
          
        if string[i].isnumeric()==False:                      
            if string[i]=="-" and num==0 and signFlag==0:
                signFlag=1            
            else:
                signFlag=0
                return -1
              
        if string[i].isnumeric()==True:                       # Small calulation
            num = (num*10)+int(string[i])
        
        return self.helper(string, num, i+1, signFlag)       # Recursive Call
                
    def atoi(self,string):
        # Code here
        return self.helper(string,0,0,0)


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends
