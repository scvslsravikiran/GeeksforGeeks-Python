"""
Created on Feb 24 2019 06:30 PM
@author : S C V S L S RAVI KIRAN
"""

'''
Zero Converter - Python
Question : https://practice.geeksforgeeks.org/problems/zero-converter-python/1/?track=python-module-2
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        numbah=int(input())
        if(numbah>0):
            pos(numbah)
        elif(numbah<0):
            neg(numbah)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        
if __name__=='__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def pos(n):
    ## Write the code
    while(n > 0):
        print(n-1, end=" ")
        n -= 1
        if(n == 0):
            break
    
def neg(n):
    ##Write the code
    while(n <= 0):
        print(n, end=" ")
        n += 1
        if(n > 0):
            break