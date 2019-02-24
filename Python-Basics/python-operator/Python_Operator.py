"""
Created on Feb 4 2019 08:57 AM
@author : S C V S L S RAVI KIRAN
"""

'''
Operators in Python
Question : https://practice.geeksforgeeks.org/problems/operators-in-python/1/?track=fork-python
'''
"""
{
#Initial Template for Python 3
#Position this line where user code will be pasted.
# Python Code to perform mathematical operation
def main():
    testcase = int(input())
    
    while(testcase > 0):
        input1 = input().split()
        x = int(input1[0])
        y = int(input1[1])
        do_operation(x, y)
        
        testcase -= 1
        
if __name__ == '__main__':
    main()   
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to perform mathematical operation on X and Y
def do_operation(x, y):
    # Your code here
    add = x + y
    sub = x - y
    product = x * y
    div = x / y
    power = x ** y
    floordiv = x // y
    print (add)
    print (sub)
    print (product)
    print (div)
    print (power)
    print (floordiv)
   