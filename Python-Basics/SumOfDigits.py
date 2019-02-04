"""
Created on Feb 4 2019 11:47 AM
@author : S C V S L S RAVI KIRAN
"""

'''
Sum of Digits - Python
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        print(digitsSum(a))
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def digitsSum(n):
    '''
    sum = 0
    while (n != 0): 
      
        sum = sum + int(n % 10) 
        n = int(n/10) 
      
    return sum
    '''
    n = str(n)
    output = int(n[0:1]) + int(n[1:2])
    return output
    ##Your code here