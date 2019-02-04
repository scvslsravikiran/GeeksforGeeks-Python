"""
Created on Feb 4 2019 07:49 AM
@author : S C V S L S RAVI KIRAN
"""

'''
Repetitive Printing - Python
Question : https://practice.geeksforgeeks.org/problems/repeatitive-printing-python/1
'''
"""
{
#Initial Template for Python 3
# Python Code to print given string
# multiple times
# Position this line where user code will be pasted.
# Driver Code
def main():
    testcases = int(input())
    
    # Loop for testcases
    while(testcases > 0):
        string = input()
        x = int(input())
        print_fun(string, x)
        testcases -= 1
if __name__ == '__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print given string 'x' times
def print_fun(string, x):
    # Your code here
    print(x*string)