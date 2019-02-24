"""
Created on Feb 24 2019 06:30 PM
@author : S C V S L S RAVI KIRAN
"""

'''
AweSum - Python
Question : https://practice.geeksforgeeks.org/contest-problem/awesum/1/
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        print(aweSum(a,b))
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def aweSum(a, b):
    ##Your code here
    c = a+b
    if (c >= 20 and c<= 40):
        return 42
    return c