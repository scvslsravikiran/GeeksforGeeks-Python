"""
Created on Feb 4 2019 07:57 AM
@author : S C V S L S RAVI KIRAN
"""

'''
Concatenating Strings - Python
Question : https://practice.geeksforgeeks.org/problems/concatenating-strings-python/1/?track=fork-python
'''
"""
{
#Initial Template for Python 3
#Position this line where user code will be pasted.
# Python Code to concatenate given strings
def main():
    testcases = int(input())
    
    while(testcases > 0):
        string1 = input()
        string2 = input()
        print_fun(string1, string2)
        
        testcases -= 1
if __name__ == '__main__':
    main()
}
"""

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to concatenate given two strings and print
def print_fun(string1, string2):
    print (string1 + string2)