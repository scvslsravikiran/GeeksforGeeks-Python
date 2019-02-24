"""
Created on Feb 24 2019 06:46 PM
@author : S C V S L S RAVI KIRAN
"""

'''
Jumping through While - Python
Question : https://practice.geeksforgeeks.org/problems/jumping-through-while-python/1/?track=python-module-2
'''
"""
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}
"""

import math
''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    i = 1
    # Loop to jump in powers of 2
    while(i < x):
        ##Your code here
        
        print (i**2, end = " ")
        
        ##Your code here
        i += 1
        if i > math.sqrt(x):
            break